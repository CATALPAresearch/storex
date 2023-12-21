"""
Script for invoking the submodules as standalone functionalities for development and testing purposes.
"""
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

import logging
logging.basicConfig(level=logging.DEBUG)
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
    case "manager":
        from questions.question_managing import QuestionManager
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

    case "evaluation":  # TODO: Broken
        from evaluation import Evaluator

        # Sample student answer, correct answer and keywords
        test_student = "Das Problem der schlechten Tracebarkeit entsteht durch das Brechen des Lokalitätsprinzips."
        test_correct = ("Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Die "
                        "Goto-Anweisung erlaubt Sprünge von beliebigen Stellen eines Programms zu anderen Stellen und "
                        "bricht dabei das Lokalitätsprinzip von Programmen, bei dem zusammengehörende Anweisungen im "
                        "Programmtext nahe beieinander stehen. Dies führte zu einer Unübersichtlichkeit im"
                        "Programmtext und erschwerte das Verstehen und Debuggen von Programmen.")
        test_keywords = {'terms': ['dynamisch', 'Goto', 'Lokalitätsprinzip', 'Binden', 'Debuggen'],
                         'common': ['Unterprogramm']}

        evaluator = Evaluator()
        # evaluator.get_missing_keys(test_correct, test_student)
        evaluator.evaluate_keywords(test_keywords, test_student)

    case "generator":
        from questions.question_generation import QuestionGenerator
        from utils.preprocessing import setup_word_lists
        setup_word_lists()
        test_keyword = "kapselung"
        generator = QuestionGenerator()
        # generator.generate_question(test_keyword)
        generator.generate_question_answer(test_keyword)

    case _:
        raise ValueError("Given module does not exist.")
