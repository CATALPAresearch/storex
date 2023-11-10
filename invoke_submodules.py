"""
Script for invoking the submodules as standalone for development purposes.
"""
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.disabled = False


# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-m", "--module", help="Module name to test.")
args = vars(parser.parse_args())

# Check if a name was given
if not args["module"]:
    raise ValueError("No module given.")

match args["module"]:
    case "get_questions":
        from questions.question_manager import QuestionManager
        qm = QuestionManager()
        print(qm.get_question())

    case "speech_recognition":
        from audio.speech_recognition import SpeechRecognition
        transcription = SpeechRecognition()
        print(transcription.get_audio_to_text())

    case "text_to_speech":
        from audio.text_to_speech import TextToSpeech
        text_input = """Hallo, wie geht es dir? Dies ist ein Test-Text. Auf geht's!"""
        audio = TextToSpeech()
        audio.get_audio(text_input)

    case _:
        raise ValueError("Given module does not exist.")
