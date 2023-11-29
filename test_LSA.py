import os
import re
import numpy
import glob
from nltk.probability import FreqDist
from gensim import corpora, models, similarities
from gensim.parsing.preprocessing import preprocess_string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


import logging
logger = logging.getLogger()

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
stop_words = []


def setup_stopwords():
    """
    Set up the list of german stopwords from file.
    """
    directory = os.path.dirname(__file__)
    file_sw = (os.path.join(directory, 'data/german_stop_words.txt'))
    with open(file_sw, 'r') as sw:
        global stop_words
        stop_words = sw.readlines()
        stop_words = [word.strip('\n') for word in stop_words]


def preprocess_text(text):
    """
    Preprocess the answer by removing non-alphanumeric characters, extra whitespaces, german umlauts and stopwords and
    making all words lowercase.

    :param text: Unprocessed answer.
    :return: Preprocessed answer.
    """
    # Remove non-alphanumeric characters (except for whitespaces)
    text = re.sub(r'[^ \w+]', '', text)
    custom_filters = [lambda x: x.lower(),             # Make all words lowercase
                      lambda x: x.strip(),             # Strip extra whitespace
                      lambda x: x.replace("ä", "ae"),  # Replace german umlauts
                      lambda x: x.replace("ö", "oe"),
                      lambda x: x.replace("ü", "ue"),
                      lambda x: x.replace("ß", "ss")]
    text = preprocess_string(text, custom_filters)
    # Remove stopwords
    text = [word for word in text if word not in stop_words]
    # TODO: Stemming/ Lemmatization
    return text


def setup_semantic_room():
    """
    Semantic room from complete course text (not useful?)
    """
    directory = os.path.dirname(__file__)
    # Load course material
    course_material = []
    directory_cm = (os.path.join(directory, 'data/chapters/processed_chapters'))
    for file_cm in glob.glob(directory_cm + '/*.txt'):
        with open(file_cm, 'r') as cm:
            lines = cm.readlines()
            lines = lines[lines.index('\n') + 1:]
            paragraph = ''.join(lines[:lines.index('\n')])
            paragraph = ' '.join(preprocess_text(paragraph))
            course_material.append(paragraph)
    # Create a document-term matrix
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(course_material)
    terms = tfidf_vectorizer.get_feature_names_out()

    # Apply Latent Semantic Analysis (LSA) using TruncatedSVD
    num_topics = 2  # Number of topics for LSA
    lsa_model = TruncatedSVD(n_components=num_topics)
    lsa_topic_matrix = lsa_model.fit_transform(tfidf_matrix)

    return lsa_model, tfidf_vectorizer


def answers_in_semantic_room(student_answer, correct_answer):
    """
    Represent answers in the semantic room of the complete course test to get their similarity (not useful?).
    """
    lsa_model, tfidf_vectorizer = setup_semantic_room()

    # Fold student and correct answers into the semantic room
    student_vector = tfidf_vectorizer.transform([student_answer])
    correct_vector = tfidf_vectorizer.transform([correct_answer])

    student_lsa = lsa_model.transform(student_vector)
    correct_lsa = lsa_model.transform(correct_vector)

    # Calculate cosine similarity between student and correct answers
    cosine_sim = cosine_similarity(student_lsa, correct_lsa)
    similarity = cosine_sim[0][0]

    print(f"Cosine Similarity: {similarity:.4f}", cosine_sim)


def similarity_lsa(correct_tokens, student_tokens):
    """
    Similarity between two inputs.
    """
    # Create a term dictionary of the corpus, where every unique term is assigned an index
    dictionary = corpora.Dictionary([student_tokens, correct_tokens])
    # Converting corpus into Document Term Matrix
    corpus = [dictionary.doc2bow(tokens) for tokens in [student_tokens, correct_tokens]]

    # Get the best number of topics between 2 and 12
    # coherence_values = []
    # model_list = []
    # for num_topics in range(2, 12):
    #     # generate LSA model
    #     model = LsiModel(corpus, num_topics=num_topics, id2word=dictionary)  # train model
    #     model_list.append(model)
    #     coherence_model = CoherenceModel(model=model, texts=[student_tokens, correct_tokens], dictionary=dictionary, coherence='c_v')
    #     coherence_values.append(coherence_model.get_coherence())
    # num_topics = coherence_values.index(max(coherence_values))
    # if num_topics == 0:
    #     num_topics = 2

    num_topics = 5  # TODO: What is a good number of topics?

    # Create an LSA model
    lsa = models.LsiModel(corpus, id2word=dictionary, num_topics=num_topics)  # train model
    logger.info(f"Topics (with three word each): {lsa.print_topics(num_topics=num_topics, num_words=3)}")

    # Transform the student and correct answer into the LSA space
    student_lsa = lsa[corpus[0]]
    correct_lsa = lsa[corpus[1]]

    # Convert LSA representations to NumPy arrays
    student_lsa_array = numpy.array(student_lsa)
    correct_lsa_array = numpy.array(correct_lsa)
    # Calculate cosine similarity
    similarity_matrix = cosine_similarity(student_lsa_array, correct_lsa_array)
    # Set a threshold to identify low similarity tokens
    threshold = 0.2  # Adjust the threshold as needed
    # Identify tokens with low similarity to any tokens from the other answer
    low_similarity_tokens_student = [token for token, similarity in zip(student_tokens, similarity_matrix[0]) if
                                     similarity < threshold]
    low_similarity_tokens_correct = [token for token, similarity in zip(correct_tokens, similarity_matrix[0]) if
                                     similarity < threshold]

    # Calculate the cosine similarity
    similarity = numpy.dot(student_lsa, correct_lsa) / (numpy.linalg.norm(student_lsa) * numpy.linalg.norm(correct_lsa))
    return similarity

    term_loading = lsa.projection.u
    threshold = 0.5
    differing_tokens = [term for i, term in enumerate(dictionary.values()) if abs(term_loading[i, 0]) < threshold]

    # Identify dimensions with low similarity
    low_similarity_dimensions = [i for i, sim in enumerate(similarity) if sim < threshold]

    # Examine term loadings in low similarity dimensions
    term_loadings = lsa.projection.u

    # Identify differing tokens with high absolute term loadings
    differing_tokens = set()
    for dim in low_similarity_dimensions:
        for term, loading in enumerate(term_loadings):
            if abs(loading[dim]) > 0.2:  # Adjust the threshold as needed
                differing_tokens.add(dictionary[term])

    print("Differing tokens:", differing_tokens)


def extract_keywords(text, n):
    """
    Extract the n most used words from a paragraph.
    """
    # Calculate word frequencies
    freq_dist = FreqDist(text)

    # Get the n most common words
    common_words = freq_dist.most_common(n)

    return common_words


if __name__ == '__main__':
    setup_stopwords()

    # Sample student answer and correct answer
    correct_answer = ("Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Die "
                      "Goto-Anweisung erlaubt Sprünge von beliebigen Stellen eines Programms zu anderen Stellen und "
                      "bricht dabei das Lokalitätsprinzip von Programmen, bei dem zusammengehörende Anweisungen im "
                      "Programmtext nahe beieinander stehen. Dies führte zu einer Unübersichtlichkeit im Programmtext "
                      "und erschwerte das Verstehen und Debuggen von Programmen.")
    student_answer = ("Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Das "
                      "Lokalitätsprinzip wird gebrochen und dies für zur Unerbersichtlichkeit.")
    paragraph = """56 Das Problem der schlechten Tracebarkeit
                   Spätestens mit der Verfügbarkeit sogenannter Hochsprachen und den gleichzeitig immer größer werdenden Programmen kam die Frage auf, was "gute Programmierung" ausmacht. Eines der Hauptprobleme schlechter Programmierung war schnell identifiziert: die große Diskrepanz zwischen statischem, linearem Programmtext und dynamischem, stark verzweigendem und sich wiederholendem Programmablauf. Eine gute Programmiererin hatte ihre Programme so zu schreiben, dass der Programmtext und der Programmablauf einander möglichst ähnlich waren, genauer gesagt, dass die (statische) Struktur des Programms möglichst viele Rückschlüsse auf seinen (dynamischen) Ablauf zuließ. Man wollte also von den Programmiererinnen Klartext.
                   Ebenso schnell wie das Problem wurde sein Hauptverursacher ausgemacht: die Goto-Anweisung. Sie erlaubt Sprünge von beliebigen Stellen eines Programms an beliebige andere Stellen des Programms und durchbricht dabei auf brutale Art und Weise das äußerst nützliche Lokalitätsprinzip von Programmen: Dinge, die zusammengehören, stehen im Programmtext beieinander. So, und nur so, ist bei der Inspektion des Programmtextes unmittelbar klar, wie man an eine Stelle im Programm gelangt ist und, mindestens ebenso wichtig, wie eine Variable ihren Wert bekommen hat.
                   Zur Veranschaulichung soll die nachfolgende Abbildung dienen, die einen Programmtext als eine Folge von Anweisungen stilisiert. Anweisungen sind durch Kreise dargestellt, die (textuelle) Folge der Anweisungen im Programmtext durch die kleinen Pfeile. Ohne besondere, den Kontrollfluss beeinflussende Anweisungen entspricht die (dynamische) Reihenfolge der Ausführung der (statischen) Folge der Anweisungen im Programmtext. Bei Betrachtung des stärker umrandeten, mittleren Kreises (der entsprechenden Anweisung), z. B. während einer Debug-Sitzung, ist daher aus dem unmittelbaren Kontext heraus (der Ellipse; Lokalitätsprinzip!) klar, welche Anweisung davor ausgeführt wurde und welche als nächstes drankommt. Alles ist in bester Ordnung.
                   Handelt es sich nun bei einer der Anweisungen um ein Goto, dann ist die Sachlage längst nicht mehr so klar. Man hat vielmehr die folgenden Fälle zu unterscheiden: Die betrachtete Anweisung ist selbst ein Goto: In diesem Fall ist zwar klar, woher der Programmfluss kommt, und auch, wohin er geht, letzteres aber nur mit einer gewissen Einschränkung — das Ziel ist nicht der Nachbar im Programmtext, sondern befindet sich außerhalb des gewählten Kontextes. Nun kann man den Kontext natürlich so wählen, dass er das Ziel enthält, und kurze Sprünge sind vielleicht auch so innerhalb des betrachteten Kontextes möglich; allgemein gilt jedoch, dass jede gewählte Lokalität durch einen Sprung verletzt werden kann. Immerhin lässt sich aber das Ziel des Sprungs aus dem Kontext erkennen und der Kontext entsprechend wechseln. Die betrachtete Anweisung ist Ziel eines Gotos: Hier ist die Sachlage schon schwieriger. Der Programmfluss scheint bei Betrachtung des Kontextes genau wie im ersten Beispiel zu verlaufen. Wenn man den Kontext allerdings vergrößert, lernt man, dass die dynamischen Vorgänger in der betrachteten Anweisung auch andere sein können. Der Kontext selbst gibt jedoch keinen Hinweis darauf; zwar kann das Vorhandensein eines Sprunglabels einen Hinweis darauf geben, dass die so markierte Anweisung Ziel eines Gotos sein kann, sie muss es aber nicht; in Sprachen wie BASIC beispielsweise (damals noch weit verbreitet), in denen Zeilennummern gültige Sprungziele sind, muss jede Anweisung als mit einem Label versehen betrachtet werden und kann somit Sprungziel von irgendwoher sein. Außerdem kann eine Anweisung von verschiedenen Gotos angesprungen werden, so dass unklar bleibt, welches die (zeitliche) Vorgängeranweisung war. Die betrachtete Anweisung ist unmittelbare Nachfolgerin eines Gotos: Hier ist zwar aus dem Kontext ersichtlich, dass die statischen Vorgänger nicht die dynamischen sein können, ansonsten kann man aber nur mutmaßen, dass es sich vielleicht um toten Code handeln könnte (also um Code, der niemals ausgeführt wird). Es kann nämlich die Anweisung Sprungziel von Gotos außerhalb des Kontexts sein (wie in allen anderen Fällen auch).
                   Fazit: Die Verwendung von Goto-Anweisungen verursacht ein hohes Maß an Nichtwissen bei der Interpretation von Quelltext. Speziell beim Debugging von Programmen ist der Blick in den Quelltext des Programms so nur sehr bedingt von Nutzen. Von daher, so der allgemeine Konsens, ist die Benutzung von Gotos zu vermeiden.
                   Wenn man also kein Goto benutzen darf, wie steuert man dann den Ablauf von Programmen? Die sogenannte strukturierte Programmierung sieht dafür neben der Sequenz von Anweisungen (ausgedrückt durch die unmittelbare Nachbarschaft im Programmtext) die Verzweigung, die Wiederholung und den Unterprogrammaufruf vor. Von diesen behalten die ersten beiden das Lokalitätsprinzip bei, solange man den Kontext auf den Umfang der Fallunterscheidung bzw. Schleife, die damit ausgedrückt wird, ausdehnt. Für den Unterprogrammaufruf gilt das jedoch nicht mehr: Schon weil ein Unterprogramm in der Regel von mehreren Stellen eines Programms aus aufgerufen werden kann und weil diese Stellen nicht automatisch denselben Kontext haben, wird hier das Lokalitätsprinzip durchbrochen. Dies ist aber unvermeidlich, und man tröstet sich damit, dass ein Unterprogramm, genauer eine Prozedur oder eine Funktion, immer genau an die Stelle zurückkehrt, von der es aufgerufen wurde.
                   Bei Betrachtung des textuell unmittelbaren Vorgängers der betrachteten Anweisung sieht man sofort, dass es sich beim dynamischen Vorgänger um die Return-Anweisung des aufgerufenen Unterprogramms handeln muss. Dies ist zwar nicht lokal, aber wenn man sich sicher sein kann, dass das Unterprogramm nur die Variablen manipuliert, die bei seinem Aufruf als tatsächliche Parameter übergeben wurden, und wenn zudem das Unterprogramm bekannte Vor- und Nachbedingungen enthält, dann ist das kein Problem. Selbst wenn man nicht weiß, wie die Variablen manipuliert wurden, so ist die Unwissenheit, die durch einen Unterprogrammaufruf verursacht wird, im Vergleich zu der beim Goto gering. Ihr steht auf der anderen Seite ein großer Nutzen gegenüber: Man vermeidet die Duplizierung von Code, die nötig wäre, wenn man die Anweisungen des Unterprogramms im Aufrufkontext halten wollte und es mehrere solche Aufrufkontexte gibt (das sog. Inlining, das manche Compiler aus Optimierungsgründen durchführen). Man erlaubt der Programmiererin, ihre Programme in Abschnitte zu unterteilen, die sie getrennt untersuchen und verstehen kann.
                   Besonders der zweite Punkt ist wichtig: Aus Sicht der Programmiererin sollte es nämlich reichen, zu wissen, was ein Unterprogramm tut, um es korrekt benutzen zu können. Sie muss also insbesondere nicht in das Unterprogramm hineinschauen, also seine Anweisungen inspizieren, wenn ihr eigentliches Interesse dem Kontext der Aufrufstelle gilt. Umgekehrt muss sie, wenn sie das Unterprogramm interessiert, nicht wissen, von wo es überall aufgerufen wird — es reicht dann, zu wissen, mit welchen Parametern es versorgt wird, und die sind ihr per formale Parameterdeklaration bekannt. (Voraussetzung dieser Argumentation ist jedoch, dass es keine globalen Variablen gibt, die eine gegenseitige Beeinflussung von Aufrufstelle und Unterprogramm an den tatsächlichen und formalen Parametern vorbei erlauben. Diese globalen Variablen sind jedoch mindestens so sehr verpönt wie das Goto.)
                   Bei der objektorientierten Programmierung hat man es zunächst mit einer leicht veränderten Situation zu tun. Hier sind nämlich nicht allein das Vermeiden von doppeltem Code sowie die stufenweise Verfeinerung Kriterien für die Aufteilung in Unterprogramme, sondern auch die Disziplin, jede Teilfunktion der Klasse zuzuordnen, deren Daten sie manipuliert. Typische objektorientierte Programme teilen daher die Implementierung größerer Funktionen nicht nur in kleinere auf, sondern verteilen diese auch noch über viele Klassen. Auch wenn es sich dabei stets nur um Unterprogrammaufrufe handelt, die allen obengenannten Anforderungen genügen, so erfolgen die zum Programmverstehen notwendigen Kontextwechsel doch in so kurzer Folge, dass man schnell den Überblick darüber verliert.
                   Nun ergibt sich aber mit der Einführung von dynamisch gebundenen Unterprogrammaufrufen, wie sie ja für die objektorientierte Programmierung prägend sind, das Problem, dass aus dem Programmtext nicht unmittelbar ersichtlich ist, wohin der Sprung geht: Wie bereits in Kurseinheit 1, Abschnitt 4.3.2 bemerkt, verbindet das dynamische Binden den Unterprogrammaufruf mit der Verzweigung.
                   Es ist an der Stelle der betrachteten Anweisung nicht klar, von woher der in der Anweisung zuvor angestoßene Unterprogrammaufruf zurückkehrt — es könnte von jeder Implementierung der im Gosub genannten Methode sein. Um das Sprungziel und damit die Return-Anweisung, die unmittelbarer Vorgänger war, zu identifizieren, muss man die Klasse des Empfängerobjekts kennen, also die Klasse des Werts der Variable, auf der die Methode aufgerufen wurde. Das ist aber in der Regel nur auf Basis einer vollständigen Programmanalyse bestimmbar, die sich nicht lokal durchführen lässt. Das Lokalitätsprinzip wird also durch das dynamische Binden weiter aufgeweicht als durch den Unterprogrammaufruf allein.
                   Dieser Umstand hat dazu geführt, dass das dynamische Binden von Skeptikerinnen und Gegnerinnen der objektorientierten Programmierung schon als eine Art Goto der 90er Jahre betrachtet wurde. Dieser Vergleich ist jedoch nicht ganz fair, weil, genau wie beim statisch gebundenen Unterprogrammaufruf, die Aufruferin ja gar nicht wissen muss, welche genauen Anweisungen als Antwort darauf ausgeführt werden müssen — es reicht zu wissen, welchen Vertrag die aufgerufene Methode (das aufgerufene Unterprogramm) erfüllt. Dies sollte nach den Regeln des Subtyping (Abschnitt 54.2) stets unabhängig vom vertragserfüllenden Objekt sein.
                   Andererseits sind die Verträge in der Praxis gar nicht im Programmtext spezifiziert, oder kennen Sie ein Programm, in dem für jede dynamisch gebundene Methode Vor- und Nachbedingungen spezifiziert wären? Daher kann es bei der Betrachtung der Aufrufstelle sehr wohl interessant sein, was denn nun genau in der aufgerufenen Methode passiert ist, z. B. weil man sich eine bestimmte, resultierende Variablenbelegung nicht erklären kann. In diesen Fällen wird man sich also, beim Tracen oder beim Debuggen, auch den aufgerufenen Code anschauen wollen. Das Problem ist nur, dass man gar nicht weiß, an welcher Stelle man schauen muss. Es bleibt in der Praxis also nur, das Programm erneut auszuführen, vor dem dynamisch gebundenen Aufruf zu stoppen und sich den Variableninhalt anzusehen oder den Programmablauf Schritt für Schritt zu verfolgen, mit all den oben beschriebenen Problemen.
                   Es ist wohl unbestritten, dass objektorientierte Programme schwerer zu tracen und zu debuggen sind als prozedurale. Wie schon bei den statisch gebundenen Unterprogrammaufrufen (die ja ebenfalls ein Problem darstellen können) ist die Frage jedoch, ob das, was man durch das dynamische Binden hinzugewinnt, den Preis aufwiegt. Während diese Frage jede für sich selbst entscheiden muss, so scheint die Antwort für viele Programmiererinnen — weit mehr als eine Generation nach dem Aufkommen der Objektorientierung und damit vor dem Hintergrund genügend praktischer Erfahrung — überwiegend positiv zu sein. Man darf aber auch die Neinsagerinnen nicht als Ewiggestrige abstempeln — sie mögen gute Gründe haben."""
    # Preprocess answers for similarity search
    c_processed = preprocess_text(correct_answer)
    s_processed = preprocess_text(student_answer)
    paragraph_processed = preprocess_text(paragraph)

    # Extract the 20 most used keywords
    keywords = extract_keywords(paragraph_processed, 20)

    # Print keywords
    print("Keywords:")
    for keyword, frequency in keywords:
        print(f"{keyword}: {frequency}")

    # Similarity with LSA
    similarity = similarity_lsa(c_processed, s_processed)
    print(f"Similarity Score (LSA): \n {similarity}")

    # Similarity with sematic room over pdf
    # answers_in_semantic_room(student_answer, correct_answer)
