/*
 * Front end of the oral exam simulation.
 *
 * The server runs the exam conversation in a background thread and exposes it as
 * an event log. This page polls that log, speaks the examiner's turns and
 * records the student's answers.
 *
 * Recording stops after three seconds of silence, the same rule the command line
 * version applies to the local microphone.
 */
'use strict';

const SILENCE_LIMIT_MS = 3000;   // stop after this much silence
const SILENCE_THRESHOLD = 0.012; // RMS below this counts as silence
const MIN_RECORDING_MS = 700;    // never stop before the student could speak
const MAX_RECORDING_MS = 90000;  // hard stop, matches the server side answer timeout

const state = {
  examId: null,
  since: 0,
  tts: 'browser',
  polling: false,
  recorder: null,
  stopRecording: null,
  speaking: Promise.resolve(),
};

const element = (id) => document.getElementById(id);

const dom = {
  setup: element('setup'),
  subject: element('subject'),
  courseField: element('course-field'),
  course: element('course'),
  startForm: element('start-form'),
  setupError: element('setup-error'),
  exam: element('exam'),
  stateLabel: element('state'),
  clock: element('clock'),
  dialogue: element('dialogue'),
  stop: element('stop-recording'),
  textForm: element('text-form'),
  textAnswer: element('text-answer'),
  cancel: element('cancel'),
  examError: element('exam-error'),
  meter: element('meter'),
  meterLevel: element('meter-level'),
};

/* ---------------------------------------------------------------- courses */

async function loadCourses() {
  const response = await fetch('/api/courses');
  if (!response.ok) throw new Error('Die Kursliste konnte nicht geladen werden.');
  const payload = await response.json();
  if (!payload.courses.length) throw new Error('Es ist kein Kurs eingerichtet.');

  dom.course.replaceChildren(...payload.courses.map((course) => {
    const option = document.createElement('option');
    option.value = course.id;
    option.textContent = `${course.title} (${course.units} Einheiten, ${course.questions} Fragen)`;
    option.selected = course.id === payload.default;
    return option;
  }));

  const showSubject = () => {
    const chosen = payload.courses.find((course) => course.id === dom.course.value);
    dom.subject.textContent = chosen ? chosen.title : '';
  };
  showSubject();
  dom.course.addEventListener('change', showSubject);
  // With a single course there is nothing to choose, but the value is still sent
  dom.courseField.hidden = payload.courses.length < 2;
}

/* ---------------------------------------------------------------- helpers */

function addLine(who, text, cssClass) {
  const item = document.createElement('li');
  item.className = cssClass;
  const label = document.createElement('span');
  label.className = 'who';
  label.textContent = who;
  item.append(label, document.createTextNode(text));
  dom.dialogue.append(item);
  item.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
}

function setState(text, recording = false) {
  dom.stateLabel.textContent = text;
  dom.stateLabel.classList.toggle('recording', recording);
}

function showError(text) {
  dom.examError.textContent = text;
  dom.examError.hidden = !text;
}

function formatClock(seconds) {
  if (seconds === null || seconds === undefined) return '';
  const total = Math.max(0, Math.round(seconds));
  return `${String(Math.floor(total / 60)).padStart(2, '0')}:${String(total % 60).padStart(2, '0')} verbleibend`;
}

/* -------------------------------------------------------------- speaking */

function pickGermanVoice() {
  const voices = window.speechSynthesis ? window.speechSynthesis.getVoices() : [];
  return voices.find((voice) => voice.lang && voice.lang.toLowerCase().startsWith('de')) || null;
}

function speakInBrowser(text) {
  return new Promise((resolve) => {
    if (!window.speechSynthesis) {
      resolve();
      return;
    }
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'de-DE';
    const voice = pickGermanVoice();
    if (voice) utterance.voice = voice;
    utterance.onend = resolve;
    // A failed utterance must not stall the dialogue
    utterance.onerror = resolve;
    window.speechSynthesis.speak(utterance);
  });
}

function speakFromServer(seq) {
  return new Promise((resolve) => {
    const audio = new Audio(`/api/tts/${state.examId}/${seq}`);
    audio.onended = resolve;
    audio.onerror = resolve;
    audio.play().catch(resolve);
  });
}

function speak(event) {
  // Utterances are chained, so the next one never starts before this one ended
  state.speaking = state.speaking.then(() =>
    state.tts === 'piper' ? speakFromServer(event.seq) : speakInBrowser(event.text));
  return state.speaking;
}

/* ------------------------------------------------------------- recording */

async function recordAnswer() {
  let stream;
  try {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  } catch (error) {
    showError('Kein Zugriff auf das Mikrofon. Sie können Ihre Antwort stattdessen eintippen.');
    dom.textForm.hidden = false;
    return;
  }

  const recorder = new MediaRecorder(stream);
  const chunks = [];
  recorder.ondataavailable = (event) => {
    if (event.data.size > 0) chunks.push(event.data);
  };

  // Watch the input level so that recording ends on silence, as in the CLI
  const context = new AudioContext();
  const analyser = context.createAnalyser();
  analyser.fftSize = 2048;
  context.createMediaStreamSource(stream).connect(analyser);
  const samples = new Float32Array(analyser.fftSize);

  const started = Date.now();
  let lastSound = Date.now();
  let finished = false;

  const finish = () => {
    if (finished) return;
    finished = true;
    clearInterval(watchdog);
    dom.stop.hidden = true;
    dom.meter.hidden = true;
    if (recorder.state !== 'inactive') recorder.stop();
  };

  const watchdog = setInterval(() => {
    analyser.getFloatTimeDomainData(samples);
    let sum = 0;
    for (const sample of samples) sum += sample * sample;
    const level = Math.sqrt(sum / samples.length);
    dom.meterLevel.style.width = `${Math.min(100, Math.round(level * 600))}%`;

    const elapsed = Date.now() - started;
    if (level >= SILENCE_THRESHOLD) lastSound = Date.now();
    if (elapsed > MIN_RECORDING_MS && Date.now() - lastSound > SILENCE_LIMIT_MS) finish();
    if (elapsed > MAX_RECORDING_MS) finish();
  }, 100);

  state.stopRecording = finish;
  dom.stop.hidden = false;
  dom.meter.hidden = false;
  setState('Aufnahme läuft, sprechen Sie jetzt …', true);

  const recorded = new Promise((resolve) => {
    recorder.onstop = () => resolve(new Blob(chunks, { type: recorder.mimeType }));
  });
  recorder.start();

  const blob = await recorded;
  stream.getTracks().forEach((track) => track.stop());
  context.close();
  state.stopRecording = null;
  setState('Antwort wird ausgewertet …');

  const body = new FormData();
  body.append('exam_id', state.examId);
  body.append('audio', blob, 'answer.webm');
  try {
    const response = await fetch('/api/answer', { method: 'POST', body });
    if (!response.ok) {
      const payload = await response.json().catch(() => ({}));
      throw new Error(payload.error || 'Die Antwort konnte nicht übertragen werden.');
    }
  } catch (error) {
    // The turn would otherwise be lost until the server times out, so offer
    // the typed fallback right away
    showError(`${error.message} Sie können sie stattdessen eintippen.`);
    dom.textForm.hidden = false;
    dom.textAnswer.focus();
  }
}

/* ----------------------------------------------------------------- events */

async function handleEvent(event) {
  switch (event.type) {
    case 'say':
      addLine('Prüfer', event.text, 'examiner');
      await speak(event);
      break;
    case 'listen':
      // Only start recording once the examiner has actually finished speaking
      await state.speaking;
      await recordAnswer();
      break;
    case 'transcript':
      addLine('Sie', event.text || '(keine Antwort erkannt)', 'student');
      break;
    case 'mic_failed':
    case 'error':
      showError(event.text);
      addLine('System', event.text, 'notice');
      break;
    case 'finished':
      addLine('System', event.text, 'notice');
      break;
    default:
      break;
  }
}

async function poll() {
  if (state.polling) return;
  state.polling = true;

  while (state.examId) {
    let data;
    try {
      const response = await fetch(`/api/events?exam_id=${state.examId}&since=${state.since}`);
      if (response.status === 404) {
        showError('Die Prüfung ist nicht mehr verfügbar.');
        break;
      }
      data = await response.json();
    } catch (error) {
      // A long-poll may be cut off; try again
      continue;
    }

    state.since = data.since;
    dom.clock.textContent = formatClock(data.remaining_seconds);

    for (const event of data.events) {
      await handleEvent(event);
    }

    if (data.state === 'thinking') setState('Antwort wird ausgewertet …');
    else if (data.state === 'speaking') setState('Der Prüfer spricht …');

    if (data.closed) {
      setState(data.state === 'error' ? 'Prüfung abgebrochen.' : 'Prüfung beendet.');
      dom.stop.hidden = true;
      dom.textForm.hidden = true;
      dom.cancel.hidden = true;
      break;
    }
  }

  state.polling = false;
}

/* ------------------------------------------------------------------- wire */

dom.startForm.addEventListener('submit', async (submitEvent) => {
  submitEvent.preventDefault();
  dom.setupError.hidden = true;
  const button = element('start');
  button.disabled = true;
  button.textContent = 'Prüfung wird vorbereitet …';

  // Chrome only fills the voice list after the first call
  if (window.speechSynthesis) window.speechSynthesis.getVoices();

  try {
    const response = await fetch('/api/exam', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: element('name').value,
        gender: element('gender').value,
        minutes: Number(element('minutes').value),
        course: dom.course.value,
      }),
    });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.error || 'Die Prüfung konnte nicht gestartet werden.');

    state.examId = payload.exam_id;
    state.tts = payload.tts;
    dom.setup.hidden = true;
    dom.exam.hidden = false;
    setState('Der Prüfer begrüßt Sie …');
    poll();
  } catch (error) {
    dom.setupError.textContent = error.message;
    dom.setupError.hidden = false;
    button.disabled = false;
    button.textContent = 'Prüfung beginnen';
  }
});

dom.stop.addEventListener('click', () => {
  if (state.stopRecording) state.stopRecording();
});

dom.textForm.addEventListener('submit', async (submitEvent) => {
  submitEvent.preventDefault();
  const text = dom.textAnswer.value.trim();
  if (!text) return;
  dom.textAnswer.value = '';
  const response = await fetch('/api/answer/text', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ exam_id: state.examId, text }),
  });
  if (!response.ok) {
    const payload = await response.json().catch(() => ({}));
    showError(payload.error || 'Die Antwort konnte nicht übertragen werden.');
  }
});

dom.cancel.addEventListener('click', async () => {
  if (!state.examId) return;
  const examId = state.examId;
  state.examId = null;
  if (state.stopRecording) state.stopRecording();
  await fetch(`/api/exam/${examId}`, { method: 'DELETE' });
  setState('Prüfung abgebrochen.');
  dom.stop.hidden = true;
  dom.textForm.hidden = true;
});

loadCourses().catch((error) => {
  dom.setupError.textContent = error.message;
  dom.setupError.hidden = false;
  element('start').disabled = true;
});

window.addEventListener('beforeunload', () => {
  if (state.examId) {
    navigator.sendBeacon?.(`/api/exam/${state.examId}`);
  }
});
