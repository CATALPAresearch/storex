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

    case "evaluation":
        from evaluation import Evaluator
        # Sample student answer and correct answer
        test_student = "Das Problem der schlechten Tracebarkeit entsteht durch das Brechen des Lokalitätsprinzips."
        test_correct = ("Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Die "
                        "Goto-Anweisung erlaubt Sprünge von beliebigen Stellen eines Programms zu anderen Stellen und "
                        "bricht dabei das Lokalitätsprinzip von Programmen, bei dem zusammengehörende Anweisungen im "
                        "Programmtext nahe beieinander stehen. Dies führte zu einer Unübersichtlichkeit im Programmtext "
                        "und erschwerte das Verstehen und Debuggen von Programmen.")
        test_english = ("Supervised learning is the machine learning task of learning a function that maps an input to "
                        "an output based on example input-output pairs. It infers a function from labeled training data "
                        "consisting of a set of training examples. In supervised learning, each example is a pair "
                        "consisting of an input object (typically a vector) and a desired output value (also called the "
                        "supervisory signal). A supervised learning algorithm analyzes the training data and produces an "
                        "inferred function, which can be used for mapping new examples. An optimal scenario will allow "
                        "for the algorithm to correctly determine the class labels for unseen instances. This requires "
                        "the learning algorithm to generalize from the training data to unseen situations in a "
                        "'reasonable' way (see inductive bias).")
        evaluator = Evaluator()
        evaluator.get_missing_keys(test_correct, test_student)

    case _:
        raise ValueError("Given module does not exist.")
