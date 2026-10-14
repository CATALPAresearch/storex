"""
Runs one component of the dialogue system on its own.

    python -m oral_exam.diagnostics --course oop --module qa_selection

Useful to check a change without holding a whole exam. The report is written to
the run directory. Modules that need a microphone or speakers only work outside
the container.
"""
import logging
import random

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from datetime import datetime

import courselib

from tests.fixtures import students, evaluation_data
from oral_exam.utils.paths import run_file

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

date = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")


def main():
    # Parse command line arguments
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--course", default=None,
                        help="Id of the course whose content is used. Default: the first course.")
    parser.add_argument("-m", "--module", help="""Name of one of the following modules:
        'speech_recognition',
        'text_to_speech'
        'evaluation'
        'qa_generation'
        'qa_selection'
        'paraphrasing'
        'feedback'
        'other_prompts'""")
    args = vars(parser.parse_args())

    # Check if a name was given
    if not args["module"]:
        raise ValueError("No module given.")

    course = courselib.get(args["course"] or courselib.default_course_id())
    logger.info("Using course %s", course.summary())

    OUTPUT_FILE = run_file(f"components_{args['module']}_{date}.txt", course.id)
    logger.info("Writing the report to %s", OUTPUT_FILE)

    match args["module"]:
        case "speech_recognition":
            from oral_exam.audio.transcription import SpeechRecognition
            transcription = SpeechRecognition()
            print(transcription.get_audio_to_text())

        case "text_to_speech":
            from oral_exam.audio.playback import TextToSpeech
            text_input = """Hallo, wie geht es dir? Dies ist ein Test-Text. Auf geht's!"""
            audio = TextToSpeech()
            audio.get_audio(text_input)

        case "evaluation":
            from oral_exam.evaluation import Evaluator

            evaluator = Evaluator()
            with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                file.write("Answer Evaluation Testing\n\n")

            for answers in evaluation_data:
                result = evaluator.evaluate_answer(answers['correct_answer'], answers['student_answer'])
                match = 'yes' if result == answers['expected'] else 'no'
                with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                    file.write(f"""Correct answer:    {answers['correct_answer']}
    Student answer:    {answers['student_answer']}
    Expected result:   {answers['expected'].name}
    Evaluation result: {result.name}
    Match:             {match}\n\n""")

        case "qa_generation":
            from oral_exam.questions.generation import QuestionGenerator
            from oral_exam.utils import preprocessing
            from oral_exam.text_generation import TextGenerator

            text_gen = TextGenerator()
            generator = QuestionGenerator(text_gen, course)

            with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                file.write("Question Answer Generation Testing\n\n")

            for _ in range(30):
                # A term may be a list of synonyms, so ask for its canonical label
                test_keyword = preprocessing.term_label(random.choice(course.materials.technical_terms))
                question_answer = generator.generate_question_answer(test_keyword)
                if question_answer is None:
                    logger.warning("No question generated for '%s'.", test_keyword)
                    continue
                with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                    file.write(f"""Keyword:  {test_keyword}
    Question: {question_answer['question']}
    Answer:   {question_answer['answer']}\n\n""")

        case "qa_selection":
            from oral_exam.questions.managing import QuestionManager, TopicManager
            from oral_exam.utils import preprocessing

            topic_manager = TopicManager(course)
            qa_manager = QuestionManager(topic_manager, course)
            evaluated = [[] for _ in course.units]

            with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                file.write("""Question Selection Testing\n\n""")

            for index, unit in enumerate(course.units):
                for level in unit.questions:
                    if level:
                        evaluated[index].append(random.choice(level))

            for i, unit in enumerate(course.units):
                # Remove open question
                qa_manager.get_question()
                with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                    file.write(f"_____{unit.title}_____\n\n")
                for question in evaluated[i]:
                    keywords = preprocessing.extract_keywords(question['answer'],
                                                              course.materials.technical_terms)
                    if not keywords:
                        continue
                    test_keyword = random.choice(keywords)
                    logger.debug("Test Keyword: %s", test_keyword)
                    selected_question = qa_manager.select_question(test_keyword)
                    with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                        file.write(f"""Keyword:  {test_keyword}
    Question: {selected_question['question']}
    Answer:   {selected_question['answer']}\n\n""")

                topic_manager.increase_topic()

        case "paraphrasing":
            from oral_exam.questions.paraphrasing import QuestionParaphraser

            paraphraser = QuestionParaphraser(course)
            question_answer = []
            generations = []
            for unit in course.units:
                for level in unit.questions:
                    if level:
                        question_answer.append(random.choice(level))
            for answer in question_answer:
                generations.append(paraphraser.paraphrase(answer['answer']))

            with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                file.write("""Paraphrasing / Help Testing

    Course: {course.title}
    Model:  {course.materials.paraphrase_model or 'text generation backend'}\n\n""")
                for answer, generation in zip(question_answer, generations):
                    file.write(f"""Input (answer):      {answer['answer']}
    Output (generation): {generation}
    Previous question:   {answer['question']}\n\n""")

        case "feedback":
            from oral_exam.feedback import FeedbackManager, check_feedback
            from oral_exam.utils.helpers import Level
            from oral_exam.text_generation import TextGenerator

            text_gen = TextGenerator()

            with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                file.write("""Feedback Prompt Testing

    Feedback Prompt: [INST] Du bist ein Professor an einer deutschen Universität.
                     Du hältst online mündliche Prüfungen ab.
                     Gib {student['dative']} namens {student['name']} mündlich ein konstruktives Feedback in 3 Sätzen für {student['possessive']} Leistungen im Anschluss an eine mündliche Prüfung.
                     Nutze folgende Informationen zu {student['possessive']}n Leistungen:
                     {feedback_rules}
                     Gib nur das Feedback zurück:[/INST]\n\n""")

            question_no = 25

            for student in students:
                with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                    file.write(f"{student['nominative']}:        {student['name']}")
                for _ in range(3):
                    feedback = FeedbackManager(course.unit_titles)
                    for _ in range(question_no):
                        feedback.add_question()
                    # Draw a random count per category. This used to choose from a
                    # list that was being popped at the same time, which ran into
                    # IndexError for plausible draws.
                    for _ in range(random.randrange(question_no)):
                        feedback.add_reiteration()
                    for _ in range(random.randrange(question_no)):
                        feedback.add_contradiction()
                    for _ in range(random.randrange(question_no)):
                        feedback.add_irrelevant()
                    for _ in range(random.randrange(question_no)):
                        feedback.add_missed(random.choice([0, 1, 2, 3, 4, 5]), 5)
                    ke_questions = list(range(max(1, int(question_no / len(course.units)))))
                    for i in range(len(course.units)):
                        feedback.add_feedback(random.choice(ke_questions), i, random.choice(list(Level)))

                    feedback_rules = feedback.construct_feedback(student['nominative'])
                    feedback_query = (f"""Gib {student['dative']} namens {student['name']} mündlich ein konstruktives Feedback in 3 Sätzen für {student['possessive']} Leistungen im Anschluss an eine mündliche Prüfung.
    Nutze folgende Informationen zu {student['possessive']}n Leistungen:
    {feedback_rules}
    Gib nur das Feedback zurück:""")
                    feedback = text_gen.get_text(feedback_query)
                    feedback = check_feedback(feedback)
                    with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                        file.write(f"""Feedback rules:       {feedback_rules}
    Generiertes Feedback: {feedback}\n""")

        case "other_prompts":
            from oral_exam.text_generation import TextGenerator
            text_gen = TextGenerator()

            with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                file.write("""Begrüßung und Verabschiedung Prompt Testing

    Prompt Begrüßung:      [INST] Du bist ein Professor an einer deutschen Universität.
                           Du hältst online mündliche Prüfungen ab.
                           Begrüße {student['accusative']} namens {student['name']} in 2 Sätzen zu einer mündlichen Prüfung.
                           Sage in der Begrüßung, dass ihr als Erstes das Mikrofon testen müsst und {student['name']} dafür gleich hineinsprechen soll.
                           Gib nur die Begrüßung zurück:[/INST]

    Prompt Verabschiedung: [INST] Du bist ein Professor an einer deutschen Universität.
                           Du hältst online mündliche Prüfungen ab.
                           Verabschiede {student['accusative']} namens {student['name']} in 1 Satz nach einer mündlichen Prüfung.
                           Gib nur die Verabschiedung zurück:[/INST]\n\n""")

            for student in students:
                greeting_query = (f"""Begrüße {student['accusative']} namens {student['name']} in 2 Sätzen zu einer mündlichen Prüfung.
    Sage in der Begrüßung, dass ihr als Erstes das Mikrofon testen müsst und {student['name']} dafür gleich hineinsprechen soll.
    Gib nur die Begrüßung zurück:""")
                greeting = text_gen.get_text(greeting_query)
                goodbye_query = (f"""Verabschiede {student['accusative']} namens {student['name']} in 1 Satz nach einer mündlichen Prüfung.
    Gib nur die Verabschiedung zurück:""")
                goodbye = text_gen.get_text(goodbye_query)

                with open(OUTPUT_FILE, 'a', encoding='utf-8', newline='') as file:
                    file.write(f"""{student['nominative']}:               {student['name']}
    Generierte Begrüßung:      {greeting}
    Generierte Verabschiedung: {goodbye}\n\n""")

        case _:
            raise ValueError("Given module does not exist.")


if __name__ == "__main__":
    main()
