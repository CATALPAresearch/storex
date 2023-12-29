import glob
import os

from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

directory = os.path.dirname(os.path.dirname(__file__))
INPUT_PATH = os.path.join(directory, 'data/chapters_processed/')
OUTPUT_PATH = os.path.join(directory, 'data/chapters_processed_auto/')


def read_txt(chapter_file):
    with open(chapter_file, 'r') as f:
        content = f.readlines()
        title = content.pop(0)
        content = [line for line in content if line != '\n' and not (line.startswith("Frage:") or
                                                                     line.startswith("Antwort:"))]
    return content, title


def write_txt(question_chapter, chapter_no):
    outpath = OUTPUT_PATH + chapter_no + '.txt'
    with open(outpath, 'w') as outfile:
        for lines in question_chapter:
            outfile.write("%s\n" % lines)


class QuestionAnswerGenerator:
    def __init__(self):
        template = (
            """
            Erstelle Frage-Antwort Paare für eine mündliche Prüfung an einer deutschen Universität.
            Nutze nur Informationen aus folgendem Text:
            Kontext: {context}

            {question-answer}
            """)
        self.example_prompt = PromptTemplate(input_variables=['context', 'question-answer'],
                                             template=template)

        remember_prompt = self.get_remember_prompt()
        apply_prompt = self.get_apply_prompt()
        analyze_prompt = self.get_analyze_prompt()

        llm = HuggingFaceHub(repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
                             model_kwargs={'max_new_tokens': 512, 'raw_response': True})

        self.remember_chain = LLMChain(prompt=remember_prompt,
                                       llm=llm)

        self.apply_chain = LLMChain(prompt=apply_prompt,
                                    llm=llm)

        self.analyze_chain = LLMChain(prompt=analyze_prompt,
                                      llm=llm)

    def get_remember_prompt(self):
        remember_examples = [
            {
                'context': "Ein Literal (von lat. littera, der Buchstabe) ist eine Repräsentation eines Objekts, die "
                           "in der Syntax der Programmiersprache ausgedrückt wird. Literale sind somit textuelle "
                           "Spezifikationen von Objekten. Wenn der Compiler ein Literal übersetzt, erzeugt er bei der "
                           "Übersetzung das entsprechende Objekt im Speicher. Dies unterscheidet sich von "
                           "objekterzeugenden Anweisungen eines Programms, da diese erst zur Laufzeit des Programms "
                           "ausgeführt werden. Wohlgemerkt: Literale repräsentieren Objekte, es sind nicht selbst "
                           "welche.",
                'question-answer':
                    """
                    Frage: Was ist ein Literal?
                    Antwort: Ein Literal ist eine Repräsentation eines Objekts, die in der Syntax der Programmiersprache ausgedrückt wird. Literale sind somit textuelle Spezifikationen von Objekten.
                    """
            },
            {
                'context': "In einem objektorientierten Programm repräsentieren Objekte nicht nur Literale und "
                           "Variablen, sondern auch Ausdrücke. Tatsächlich sind Literale und Variablen primitive "
                           "Ausdrücke, die nicht aus anderen Ausdrücken zusammengesetzt sind. Um mit den Objekten "
                           "jedoch Aktionen auszuführen und damit ein Programm tatsächlich auszuführen, benötigen wir "
                           "weitere Arten von Ausdrücken, nämlich Zuweisungsausdrücke und Nachrichtenausdrücke. Auch "
                           "diese repräsentieren jeweils ein Objekt und können daher an allen Stellen verwendet "
                           "werden, an denen Objekte erforderlich sind. Es ist sogar möglich, sie geschachtelt "
                           "anzuordnen.",
                'question-answer':
                    """
                    Frage: Welche Arten von Ausdrücken gibt es?
                    Antwort: Es gibt Literale, Variablen, Zuweisungsausdrücke und Nachrichtenausdrücke.
                    """
            },
            {
                'context': "In SMALLTALK beginnt der Lebenslauf eines Objekts mit seiner Erzeugung und endet mit "
                           "seiner Entsorgung durch eine Speicherbereinigung, die sogenannte 'Garbage Collection'. "
                           "Garbage Collection ist ein Mechanismus, der Objekte aus dem Speicher entfernt, wenn sie "
                           "nicht mehr zugreifbar sind. Da in SMALLTALK auf Objekte nach ihrer Erzeugung "
                           "ausschließlich über Variablen (Namen) zugegriffen werden kann, kann ein solches Objekt "
                           "genau dann entfernt werden, wenn keine Variable mehr auf es verweist. Es kann entfernt "
                           "werden, muss aber nicht; aus Sicht der Programmiererin ist es ausreichend, dass das Objekt "
                           "nicht mehr bekannt oder benannt ist — es kann somit nicht mehr aufgefunden und durch eine "
                           "Zuweisung einer Variable zugewiesen werden. Bei der Implementierung von "
                           "Garbage-Collection-Algorithmen besteht daher erhebliche Freiheit.",
                'question-answer':
                    """
                    Frage: Was ist die "Garbage Collection" in SMALLTALK?
                    Antwort: Die "Garbage Collection" ist ein Mechanismus in SMALLTALK, der Objekte aus dem Speicher entfernt, wenn sie nicht mehr über Variablen zugreifbar sind.
                    """
            },
            {
                'context': "Sollte eine Methode temporäre Variablen für ihre Berechnungen benötigen, müssen diese zu "
                           "Beginn der Methode (nach der Methodensignatur und vor der ersten Anweisung) deklariert "
                           "werden. Die Werte dieser Variablen werden standardmäßig mit nil initialisiert und sind "
                           "außerhalb der Methode nicht sichtbar. Die Variablen werden nach Abarbeitung der Methode "
                           "vom System wieder entfernt, und sie können sich daher zwischen zwei Ausführungen einer "
                           "Methode nichts merken. Temporäre Variablen können auch der besseren Lesbarkeit dienen, "
                           "indem sie Zwischenergebnissen Namen geben. Umgekehrt können temporäre Variablen, die nur "
                           "einmal verwendet werden, eingespart werden, indem man kaskadierte Nachrichtenausdrücke "
                           "verwendet.",
                'question-answer':
                    """
                    Frage: Was sind temporäre Variablen?
                    Antwort: Eine Methode kann temporäre Variablen für ihre Berechnungen benötigen. Temporäre Variablen existieren nur für die Dauer der Ausführung der Methode und werden vom System nach Beendigung der Methode entfernt. Die Werte sind außerhalb der Methode nicht sichtbar. Temporäre Variablen können auch der besseren Lesbarkeit dienen, indem sie Zwischenergebnissen Namen geben.
                    """
            },
        ]

        r_prompt = FewShotPromptTemplate(
            examples=remember_examples,
            example_prompt=self.example_prompt,
            suffix="Kontext: {input}",
            input_variables=['input']
        )
        return r_prompt

    def get_apply_prompt(self):
        apply_examples = [
            {
                'context': "In der objektorientierten Programmierung werden sämtliche Informationen als ein Geflecht "
                           "von Objekten dargestellt. Dieses Geflecht kann: navigiert werden, um von einem Datum "
                           "(Stück Information) zu einem anderen zu kommen, oder auch manipuliert werden, um die "
                           "repräsentierte Information zu verändern.",
                'question-answer':
                    """
                    Frage: Wie werden Informationen in der objektorientierten Programmierung dargestellt?
                    Antwort: In der objektorientierten Programmierung werden sämtliche Informationen als ein Geflecht von Objekten dargestellt. Dieses Geflecht kann navigiert und manipuliert werden.
                    """
            },
            {
                'context': "Aliase, also weitere Namen für ein bereits benanntes Objekt, entstehen immer bei der "
                           "Zuweisung. Dazu ist es notwendig, dass die Variable auf der linken Seite Verweissemantik "
                           "hat. Da in SMALLTALK die Semantik von Variablen nicht mit der Variablendeklaration "
                           "festgelegt wird, sondern von der Art eines Objekts abhängt, ist nicht immer klar, bei "
                           "welcher Zuweisung ein Alias entsteht. Dabei kann beides, die fälschliche Annahme von "
                           "Verweissemantik bei tatsächlicher Wertsemantik und die Entstehung von Aliasen, zu "
                           "erheblichen (und schwer zu findenden) Programmierfehlern führen.",
                'question-answer':
                    """
                    Frage: Wann entstehen Aliase?
                    Antwort: Aliase entstehen immer bei der Zuweisung, wenn die Variable auf der linken Seite Verweissemantik hat.
                    """
            },
            {
                'context': "Der Zustand eines Objektes setzt sich aus den Werten seiner Instanzvariablen zusammen. Da "
                           "Instanzvariablen Beziehungen ausdrücken, wird der Zustand eines Objekts ausschließlich "
                           "durch seine Verknüpfung mit anderen Objekten definiert. Darüber hinaus folgt daraus, dass "
                           "die einzige Möglichkeit, den Zustand eines Objekts zu ändern, in der Zuweisung von "
                           "Instanzvariablen liegt, was gleichbedeutend mit der Änderung seiner Beziehungen ist.",
                'question-answer':
                    """
                    Frage: Wie wird der Zustand eines Objekts verändern?
                    Antwort: Die einzige Möglichkeit, den Zustand eines Objekts zu ändern, besteht darin, die Werte seiner Instanzvariablen zuzuweisen, was gleichbedeutend mit der Änderung seiner Beziehungen ist.
                    """
            },
            {
                'context': "Sollte eine Methode temporäre Variablen für ihre Berechnungen benötigen, müssen diese zu "
                           "Beginn der Methode (nach der Methodensignatur und vor der ersten Anweisung) deklariert "
                           "werden. Die Werte dieser Variablen werden standardmäßig mit nil initialisiert und sind "
                           "außerhalb der Methode nicht sichtbar. Die Variablen werden nach Abarbeitung der Methode "
                           "vom System wieder entfernt, und sie können sich daher zwischen zwei Ausführungen einer "
                           "Methode nichts merken. Temporäre Variablen können auch der besseren Lesbarkeit dienen, "
                           "indem sie Zwischenergebnissen Namen geben. Umgekehrt können temporäre Variablen, die nur "
                           "einmal verwendet werden, eingespart werden, indem man kaskadierte Nachrichtenausdrücke "
                           "verwendet.",
                'question-answer':
                    """
                    Frage: Was sind temporäre Variablen?
                    Antwort: Eine Methode kann temporäre Variablen für ihre Berechnungen benötigen. Temporäre Variablen existieren nur für die Dauer der Ausführung der Methode und werden vom System nach Beendigung der Methode entfernt. Die Werte sind außerhalb der Methode nicht sichtbar. Temporäre Variablen können auch der besseren Lesbarkeit dienen, indem sie Zwischenergebnissen Namen geben.
                    """
            },
        ]

        ap_prompt = FewShotPromptTemplate(
            examples=apply_examples,
            example_prompt=self.example_prompt,
            suffix="Kontext: {input}",
            input_variables=['input']
        )
        return ap_prompt

    def get_analyze_prompt(self):
        analyze_examples = [
            {
                'context': "Die Zuweisung ist ein elementares Konstrukt der objektorientierten Programmierung sowie "
                           "der Programmierung überhaupt. Nur die wenigsten Sprachen kommen ohne sie aus. Neben der "
                           "expliziten Zuweisung durch den Zuweisungsoperator kommt auch eine implizite Zuweisung (bei "
                           "Methodenaufrufen) vor. Der oben geschilderte Unterschied zwischen Wert- und "
                           "Verweissemantik von Variablen hat erhebliche Konsequenzen für die Zuweisung: Bei einer "
                           "Zuweisung unter Wertsemantik muss eine Kopie angefertigt werden, da die Variable das "
                           "Objekt zum Inhalt hat (also in der Variable gespeichert ist), und ein Objekt nicht in zwei "
                           "Variablen gespeichert sein kann. Das hat zur Folge, dass die beiden Variablen 'x' und 'y' "
                           "nach der Zuweisung aus Zeile 21 nicht dasselbe (identische) Objekt bezeichnen (was unter "
                           "Wertsemantik, wie oben bereits gesagt, auch gar nicht geht), sodass z. B. Änderungen am in "
                           "'x' gespeicherten Objekt das in 'y' gespeicherte Objekt nicht betreffen. Bei einer "
                           "Zuweisung unter Verweissemantik wird jedoch nur der Verweis der rechten Seite kopiert und "
                           "in der Variablen auf der linken Seite gespeichert. Wenn die Variablen auf der linken und "
                           "der rechten Seite unterschiedliche Semantiken haben, dann liegt entweder eine unzulässige "
                           "Zuweisung (siehe Kapitel 18) vor, oder es muss, je nach Art der Variable auf der linken "
                           "Seite, eine Kopie eines Objekts oder ein Verweis auf ein Objekt angefertigt werden.",
                'question-answer':
                    """
                    Frage: Was unterscheidet Zuweisungen unter Wertsemantik und unter Verweissemantik?
                    Antwort: Bei Zuweisungen unter Wertsemantik muss eine Kopie des Objekts angefertigt werden, da die Variable das Objekt selbst speichert. Bei Zuweisungen unter Verweissemantik wird nur der Verweis auf das Objekt kopiert und in der Variable gespeichert. Dies hat Auswirkungen darauf, ob Änderungen an einem Objekt in einer Variable sich auf dasselbe Objekt in einer anderen Variable auswirken.
                    """
            },
            {
                'context': "Während es für Variablen charakteristisch ist, dass sich ihr Wert ändern kann, sieht "
                           "SMALLTALK dennoch einige vor, für die das nicht der Fall ist. Hier sind vor allem die "
                           "Variablen mit den Namen 'true', 'false' und 'nil' zu nennen, die auf Objekte "
                           "entsprechender Bedeutung verweisen. Für diese Variablen ist die Zuweisung nicht zulässig. "
                           "Eine ganze Reihe weiterer Variablen kann zwar ihren Wert ändern (also zu unterschiedlichen "
                           "Zeiten auf verschiedene Objekte verweisen), jedoch erhalten sie ihren Wert vom System; "
                           "auch diesen kann durch den Zuweisungsoperator := kein Wert zugewiesen werden. Dies sind "
                           "z. B. die Variablen mit den Namen 'self' und 'super', sowie alle formalen Parameter von "
                           "Methoden. Nicht zuletzt sind auch alle Klassennamen Variablen, denen man als Programmierer "
                           "nichts explizit zuweisen kann. All diese Variablen werden in SMALLTALK einheitlich "
                           "Pseudovariablen genannt.",
                'question-answer':
                    """
                    Frage: Warum werden Pseudovariablen als solche bezeichnet?
                    Antwort: Sie werden als Pseudovariablen bezeichnet, da sie ihren Wert entweder nicht ändern können oder ihren Wert vom System erhalten.
                    """
            },
            {
                'context': "Eine etwas eingeschränktere Sicht auf den Zustand eines Objekts berücksichtigt lediglich "
                           "seine Attributwerte. Dies setzt jedoch voraus, dass überhaupt eine klare Unterscheidung "
                           "zwischen Attributen und Beziehungen getroffen werden kann. In Ermangelung spezieller "
                           "Schlüsselwörter könnte dies, wie bereits oben diskutiert, allenfalls über die "
                           "Unterscheidung zwischen Variablen mit Wert- und Variablen mit Referenzsemantik erfolgen. "
                           "Diese Unterscheidung ist jedoch nicht immer eindeutig, und in einigen Programmiersprachen "
                           "ist sie gar nicht zutreffend (z.B., in JAVA, in dem Strings zwar unveränderlich sind und "
                           "daher eigentlich als Werte gelten, aber dennoch Referenzsemantik aufweisen). In SMALLTALK "
                           "hingegen, in dem alle Instanzvariablen Referenzen sein können, ist diese Einschränkung "
                           "nicht anwendbar.",
                'question-answer':
                    """
                    Frage: Was unterscheidet Attribute und Beziehungen
                    Antwort: Die Unterscheidung zwischen Attributen und Beziehungen kann in Ermangelung spezieller Schlüsselwörter allenfalls über die Unterscheidung zwischen Variablen mit Wert- und Variablen mit Referenzsemantik erfolgen. Diese ist jedoch in einigen Programmiersprachen nicht immer eindeutig ist und beispielsweise in Java gar nicht zutreffend.
                    """
            },
            {
                'context': "Wenn Objekte ihren Zustand kapseln, ist es ausschließlich ihr Verhalten, welches ihn "
                           "ändert, und somit das Verhalten, das Zustandsänderungen eines Objekts herbeiführt. "
                           "Umgekehrt hängt das Verhalten eines Objekts in der Regel von seinem Zustand ab. Wie aber "
                           "wird das Verhalten eines Objekts beschrieben? Bevor wir uns dieser Frage zuwenden, müssen "
                           "wir zuerst den Begriff des Ausdrucks klären.",
                'question-answer':
                    """
                    Frage: Warum hängt das Verhalten eines Objekts von seinem Zustand ab?
                    Antwort: Das Verhalten eines Objekts hängt in der Regel von seinem Zustand ab, weil der Zustand eines Objekts die Informationen enthält, die benötigt werden, um die richtigen Entscheidungen zu treffen und die entsprechenden Aktionen auszuführen. Das Verhalten eines Objekts basiert auf den Daten in seinem Zustand, und diese Daten beeinflussen, wie das Objekt auf Nachrichten reagiert.
                    """
            }
        ]

        an_prompt = FewShotPromptTemplate(
            examples=analyze_examples,
            example_prompt=self.example_prompt,
            suffix="Kontext: {input}",
            input_variables=['input']
        )
        return an_prompt

    def get_remember_question(self, query):
        return self.remember_chain.run(query)

    def get_apply_question(self, query):
        return self.apply_chain.run(query)

    def get_analyze_question(self, query):
        return self.analyze_chain.run(query)


qa_generator = QuestionAnswerGenerator()
files = glob.glob(INPUT_PATH + '*.txt')
for file in files:
    chapter, headline = read_txt(file)
    chapter_number = headline.split(' ', 1)[0]
    chapter_with_questions = [headline]
    for paragraph in chapter:
        chapter_with_questions.append(paragraph)
        questions = qa_generator.get_remember_question(paragraph).splitlines()
        questions.extend(qa_generator.get_apply_question(paragraph).splitlines())
        questions.extend(qa_generator.get_analyze_question(paragraph).splitlines())
        i = 0
        while i < len(questions):
            if questions[i].startswith("Kontext:") or questions[i] == questions[i - 1]:
                questions.pop(i)
            else:
                i += 1
        chapter_with_questions.extend(questions)
        chapter_with_questions.append('\n')
    write_txt(chapter_with_questions, chapter_number)
    exit(0)
