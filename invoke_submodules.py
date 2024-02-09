"""
Script for invoking the submodules as standalone functionalities for development and testing purposes.
"""
import os
import random
import re

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from datetime import datetime

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.disabled = False

date = datetime.now().strftime("%d-%m-%Y--%H-%M-%S")
directory = os.path.dirname(__file__)
OUTPUT_FILE = os.path.join(directory, f"testing/test_results_submodule_{date}")


# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-m", "--module", help="Module name to test.")
args = vars(parser.parse_args())

students = [{'name': "Luna", 'nominative': "Die Studentin", 'accusative': 'eine Studentin',
             'dative': "einer Studentin", 'possessive': "ihre"},
            {'name': "Alice", 'nominative': "Die Studentin", 'accusative': 'eine Studentin',
             'dative': "einer Studentin", 'possessive': "ihre"},
            {'name': "Defne", 'nominative': "Die Studentin", 'accusative': 'eine Studentin',
             'dative': "einer Studentin", 'possessive': "ihre"},
            {'name': "Linus", 'nominative': "Der Student", 'accusative': 'einen Studenten',
             'dative': "einem Studenten", 'possessive': "seine"},
            {'name': "Kiano", 'nominative': "Der Student", 'accusative': 'einen Studenten',
             'dative': "einem Studenten", 'possessive': "seine"},
            {'name': "Baschar", 'nominative': "Der Student", 'accusative': 'einen Studenten',
             'dative': "einem Studenten", 'possessive': "seine"},
            {'name': "Niam", 'nominative': "Der*die Student*in", 'accusative': 'eine*n Studenten*in',
             'dative': "einem*r Studenten*in", 'possessive': "seine*ihre"},
            {'name': "Farah", 'nominative': "Der*die Student*in", 'accusative': 'eine*n Studenten*in',
             'dative': "einem*r Studenten*in", 'possessive': "seine*ihre"},
            {'name': "Charlie", 'nominative': "Der*die Student*in", 'accusative': 'eine*n Studenten*in',
             'dative': "einem*r Studenten*in", 'possessive': "seine*ihre"},
            ]

# Check if a name was given
if not args["module"]:
    raise ValueError("No module given.")

match args["module"]:
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

    case "qa_generating":
        from questions.question_generation import QuestionGenerator
        from utils import preprocessing
        from text_generation import TextGenerator

        preprocessing.setup_word_lists()
        text_gen = TextGenerator()
        generator = QuestionGenerator(text_gen)

        with open(OUTPUT_FILE, 'a', newline='') as file:
            file.write("Question Answer Generation Testing\n\n")

        for _ in range(30):
            test_keyword = random.choice(preprocessing.technical_terms)
            if test_keyword.startswith('['):
                test_keyword = (re.split(' ', test_keyword)[0])[1:1]
            question_answer = generator.generate_question_answer(test_keyword)
            with open(OUTPUT_FILE, 'a', newline='') as file:
                file.write(f"""Keyword:  {test_keyword}
Question: {question_answer['question']}
Answer:   {question_answer['answer']}\n\n""")

    case "qa_selecting":
        from questions.question_managing import QuestionManager, TopicManager
        from questions.questions import KE1_questions, KE2_questions, KE3_questions, KE4_questions, KE6_questions
        from utils import preprocessing

        preprocessing.setup_word_lists()
        topic_manager = TopicManager()
        qa_manager = QuestionManager(topic_manager)
        evaluated = [[], [], [], [], []]

        with open(OUTPUT_FILE, 'a', newline='') as file:
            file.write("""Question Selection Testing\n\n""")

        for i in range(3):
            evaluated[0].append(random.choice(KE1_questions[i]))
            evaluated[1].append(random.choice(KE2_questions[i]))
            evaluated[2].append(random.choice(KE3_questions[i]))
            evaluated[3].append(random.choice(KE4_questions[i]))
            evaluated[4].append(random.choice(KE6_questions[i]))

        for i in range(len(evaluated)):
            # Remove open question
            qa_manager.get_question()
            with open(OUTPUT_FILE, 'a', newline='') as file:
                file.write(f"_____Kurseinheit {i + 1}_____\n\n")
            for question in evaluated[i]:
                keywords = preprocessing.extract_keywords(question['answer'])
                if not keywords:
                    continue
                test_keyword = random.choice(keywords)
                if test_keyword.startswith('['):
                    test_keyword = (re.split(' ', test_keyword)[0])[1:1]
                logger.debug(f"Test Keyword: {test_keyword}")
                selected_question = qa_manager.select_question(test_keyword)
                with open(OUTPUT_FILE, 'a', newline='') as file:
                    file.write(f"""Keyword:  {test_keyword}
Question: {selected_question['question']}
Answer:   {selected_question['answer']}\n\n""")

            topic_manager.increase_topic()

    case "paraphrasing":
        from questions.paraphrasing import QuestionParaphraser
        from questions.questions import KE1_questions, KE2_questions, KE3_questions, KE4_questions, KE6_questions

        paraphraser = QuestionParaphraser()
        question_answer = []
        generations = []
        for i in range(3):
            question_answer.append(random.choice(KE1_questions[i]))
            question_answer.append(random.choice(KE2_questions[i]))
            question_answer.append(random.choice(KE3_questions[i]))
            question_answer.append(random.choice(KE4_questions[i]))
            question_answer.append(random.choice(KE6_questions[i]))
        for answer in question_answer:
            generations.append(paraphraser.paraphrase(answer['answer']))

        with open(OUTPUT_FILE, 'a', newline='') as file:
            file.write("""Paraphrasing / Help Testing

Finetuned Model: 'LunaticTanuki/oop-de-qg-flan-t5-base-v6'\n\n""")
            for answer, generation in zip(question_answer, generations):
                file.write(f"""Input (answer):      {answer['answer']}
Output (generation): {generation}
Previous question:   {answer['question']}\n\n""")

    case "feedback":
        from feedback_managing import FeedbackManager, check_feedback
        from utils.helpers import KE, Level
        from text_generation import TextGenerator

        text_gen = TextGenerator()

        with open(OUTPUT_FILE, 'a', newline='') as file:
            file.write("""Feedback Prompt Testing

Feedback Prompt: [INST] Du bist ein Professor an einer deutschen Universität.
                 Du hältst online mündliche Prüfungen ab.
                 Gib {student['dative']} namens {student['name']} mündlich ein konstruktives Feedback in 3 Sätzen für {student['possessive']} Leistungen im Anschluss an eine mündliche Prüfung.
                 Nutze folgende Informationen zu {student['possessive']}n Leistungen:
                 {feedback_rules}
                 Gib nur das Feedback zurück:[/INST]\n\n""")

        question_no = 25

        for student in students:
            with open(OUTPUT_FILE, 'a', newline='') as file:
                file.write(f"{student['nominative']}:        {student['name']}")
            possible_value = []
            for _ in range(3):
                feedback = FeedbackManager()
                for i in range(question_no):
                    possible_value.append(i)
                    feedback.add_question()
                for _ in range(random.choice(possible_value)):
                    feedback.add_reiteration()
                for _ in range(random.choice(possible_value)):
                    feedback.add_contradiction()
                    possible_value.pop()
                for _ in range(random.choice(possible_value)):
                    feedback.add_irrelevant()
                    possible_value.pop()
                for i in range(random.choice(possible_value)):
                    feedback.add_missed(random.choice([0, 1, 2, 3, 4, 5]), 5)
                    possible_value.pop()
                ke_questions = []
                for i in range(int(question_no / len(KE))):
                    ke_questions.append(i)
                for i in KE:
                    feedback.add_feedback(random.choice(ke_questions), i, random.choice(list(Level)))

                feedback_rules = feedback.construct_feedback(student['nominative'])
                feedback_query = (f"""Gib {student['dative']} namens {student['name']} mündlich ein konstruktives Feedback in 3 Sätzen für {student['possessive']} Leistungen im Anschluss an eine mündliche Prüfung.
Nutze folgende Informationen zu {student['possessive']}n Leistungen:
{feedback_rules}
Gib nur das Feedback zurück:""")
                feedback = text_gen.get_text(feedback_query)
                feedback = check_feedback(feedback)
                with open(OUTPUT_FILE, 'a', newline='') as file:
                    file.write(f"""Feedback rules:       {feedback_rules}
Generiertes Feedback: {feedback}\n""")

    case "greeting":
        from text_generation import TextGenerator
        text_gen = TextGenerator()

        with open(OUTPUT_FILE, 'a', newline='') as file:
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

            with open(OUTPUT_FILE, 'a', newline='') as file:
                file.write(f"""{student['nominative']}:               {student['name']}
Generierte Begrüßung:      {greeting}
Generierte Verabschiedung: {goodbye}\n\n""")

    case _:
        raise ValueError("Given module does not exist.")
