from utils.helpers import EvaluationType

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

answer = ('EIFFEL ist eine Sprache für objektorientierte Analyse und Design, eine Sprache für kommerzielle '
          'Programmierung und eine akademische Lehrsprache.')
answer_ke1_1 = ('Objekte sind in der objektorientierten Programmierung Daten, die im Speicher abgelegt sind und in der '
                'Lage sind, Informationen zu speichern und Aktionen auszuführen. Sie repräsentieren Dinge aus der '
                'realen Welt und können miteinander in Beziehung stehen.')
answer_ke1_2 = ('Zu-n-Beziehungen werden meistens über Zwischenobjekte umgesetzt, deren Aufgabe es ist, mittels ihrer '
                'indizierten Instanzvariablen jeweils eine Beziehung zu mehreren anderen Objekten herzustellen.')
answer_ke1_3 = ('Bei Zuweisungen unter Wertsemantik muss eine Kopie des Objekts angefertigt werden, da die Variable '
                'das Objekt selbst speichert. Bei Zuweisungen unter Verweissemantik wird nur der Verweis auf das '
                'Objekt kopiert und in der Variable gespeichert. Dies hat Auswirkungen darauf, ob Änderungen an einem '
                'Objekt in einer Variable sich auf dasselbe Objekt in einer anderen Variable auswirken.')
answer_ke2_1 = ('Eine Metaklasse ist eine Klasse, die für die Erstellung von Klassen verantwortlich ist. Sie ist eine '
                'Klasse der Klassen und ermöglicht es, die Verhaltensweisen von Klassen zu ändern oder zu erweitern.')
answer_ke2_2 = ('Der Zweck der Vererbung ist es, die Definition einer Superklasse auf eine Subklasse zu übertragen, um '
                'die Wiederverwendung von Code zu erhöhen und die Wartbarkeit des Codes zu verbessern.')
answer_ke2_3 = ('Nein, das Entfernen von Instanzvariablen oder Methoden ist unvereinbar mit der Spezialisierung. Die '
                'Richtung von Spezialisierung und Generalisierung würde beliebig werden, wenn in beide Richtungen nach '
                'Belieben hinzugefügt und entfernt werden dürfte.')
answer_ke3_1 = ('Parametrischer Polymorphismus ist eine Technik in der objektorientierten Programmierung, bei der eine '
                'Typvariable innerhalb einer Typdefinition verwendet wird. Diese Typvariable kann später durch einen '
                'konkreten Typ ersetzt werden, wenn die Typdefinition instanziiert wird.')
answer_ke3_2 = ('Zwei Typen sind zuweisungskompatibel, wenn sie identisch sind oder wenn sie eine Typäquivalenz '
                'aufweisen, d.h. wenn sie bis auf ihre Namen gleich sind.')
answer_ke3_3 = ('Strukturelle Typkonformität besteht, wenn der konforme Typ alle Elemente des Typs, zu dem er konform '
                'sein soll, enthält. Nominale Typkonformität hingegen bezieht sich auf die Übereinstimmung von '
                'Typnamen, unabhängig davon, ob die Typen strukturell identisch sind oder nicht.')
answer_ke4_1 = ('Interfaces in Java spielen eine wichtige Rolle bei der Abstraktion und der Schaffung von '
                'Schnittstellen, die von mehreren Klassen implementiert werden können. Sie ermöglichen es, die '
                'Abhängigkeiten zwischen Klassen zu verringern und die Code-Wiederverwendung zu erhöhen. Interfaces '
                'können auch als Verträge zwischen Klassen betrachtet werden, die sicherstellen, dass eine Klasse eine '
                'bestimmte Funktionalität bereitstellt.')
answer_ke4_2 = ('In Java gewähren Klassen sich untereinander privilegierten Zugriff, während nach außen nur öffentlich '
                'deklarierte Programmelemente sichtbar sind.')
answer_ke4_3 = ('Ja, C++ unterstützt Objektorientierung, indem es neben den aus C übernommenen Strukturen (structs) '
                'auch Klassen anbietet. Diese beinhalten, genau wie in SMALLTALK und Java, neben Feldern '
                '(Instanzvariablen) auch Methoden. Klassenfelder und -methoden werden mit dem Schlüsselwort static in '
                'einer Klasse eingeführt.')
answer_ke6_1 = ('Das Fragile-Base-Class-Problem bezieht sich auf eine Gruppe von Problemen in der Vererbung von '
                'Klassen. Wenn zwischen einer Klasse und ihren Subklassen aufgrund der Vererbung von Eigenschaften '
                'starke Abhängigkeiten bestehen, können Änderungen an der Basisklasse zu unerwarteten und '
                'unerwünschten Auswirkungen in der abgeleiteten Klasse führen.')
answer_ke6_2 = ('Das Geheimnisprinzip kann umgangen werden, indem Repräsentationsobjekte, deren Namen verborgen werden '
                'sollen, noch andere Namen besitzen, zum Beispiel wenn ein Objekt seine Repräsentationsobjekte bei '
                'seiner Erzeugung von außen geliefert bekommt oder wenn das Objekt selbst eine Referenz auf ein '
                'Repräsentationsobjekt herausgibt, beispielsweise durch einen Getter.')
answer_ke6_3 = ('Der Nachteil des Liskov-Substitutionsprinzips ist, dass es sich in der Praxis als zu restriktiv '
                'erweist und eine Typüberprüfung darstellt, die gültige Programme ablehnt. Die Tatsache, dass die '
                'Einhaltung des LSP im Allgemeinen nicht automatisch überprüft werden kann, ist ein recht hoher Preis '
                'für die strenge Anforderung.')


evaluation_data = [
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer,
     'student_answer': 'Die Sonderstellung von Eiffel ist, dass es eine akademische Lehrsprache ist, die nicht '
                       'wirklich als kommerzielle Programmiersprache verwendet wird.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke1_1,
     'student_answer': 'Objekte sind im Speicher abgelegt Daten. Sie speichern Informationen und führen Aktionen aus. '
                       'Verschiedene Objekte können untereinander in Beziehung stehen.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke1_1,
     'student_answer': 'Objekte sind die grundlegenden Bausteine, aus denen objektorientierte Programme aufgebaut '
                       'sind. Sie sind im Speicher abgelegt. Ein Objekt repräsentiert eine Instanz einer Klasse, die '
                       'sowohl Daten als auch Methoden enthält, um diese Daten zu verarbeiten. Objekte stehen '
                       'miteinander in Beziehung und können sich Nachrichten senden.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke1_1,
     'student_answer': 'Objekte speichern Informationen und führen Aktionen aus.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke1_1,
     'student_answer': 'Objekte sind im Speicher abgelegt Daten.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke1_1,
     'student_answer': 'Objekte können keine Daten speichern.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke1_1,
     'student_answer': 'Objekte repräsentieren Instanzen einer Klasse.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke1_1,
     'student_answer': 'Objekte repräsentieren Dinge aus der realen Welt.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke1_2,
     'student_answer': 'Zu-n-Beziehungen können direkt über indizierte Instanzvariablen oder über Zwischenobjekte '
                       'umgesetzt werden, welche mittels ihrer indizierten Instanzvariablen jeweils eine Beziehung zu '
                       'n Objekten herzustellen.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke1_2,
     'student_answer': 'Zu-n-Beziehungen werden immer über eine benannte Instanzvariable umgesetzt, welche eine '
                       'Referenz auf ein Objekt enthält.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke1_2,
     'student_answer': 'Eine zu-eins-Beziehung wird über eine benannte Instanzvariable umgesetzt, welche eine Referenz '
                       'auf ein Objekt enthält.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke1_2,
     'student_answer': 'Objekte können Variablen speichern.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke1_2,
     'student_answer': 'Zu-n-Beziehungen können über indizierte Instanzvariablen umgesetzt werden.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke1_3,
     'student_answer': 'Bei Zuweisungen unter Wertsemantik wird eine Kopie des Objekts angefertigt, da die Variable '
                       'das Objekt speichert. Bei Zuweisungen unter Verweissemantik wird der Verweis auf das Objekt '
                       'kopiert und der Verweis in der Variable gespeichert. Aliase entstehen somit bei der Zuweisung '
                       'unter Verweissemantik.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke1_3,
     'student_answer': 'Zuweisungen unter Wertsemantik und unter Verweissemantik unterscheiden sich nicht.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke1_3,
     'student_answer': 'Bei Zuweisungen unter Wertsemantik wird eine Kopie des Objekts angefertigt, da die Variable '
                       'das Objekt speichert.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke1_3,
     'student_answer': 'Bei Zuweisungen unter Verweissemantik wird der Verweis auf das Objekt kopiert und in der '
                       'Variable gespeichert.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke2_1,
     'student_answer': 'Eine Metaklasse ist die Klasse einer Klasse. Metaklassen sind für die Erstellung von Klassen '
                       'verantwortlich und definieren diese.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke2_1,
     'student_answer': 'Eine Metaklasse ist eine Instanz einer Klasse.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke2_1,
     'student_answer': 'Die Klasse Object ist die Wurzel der Vererbungshierarchie.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke2_1,
     'student_answer': 'Metalassen können in einer Vererbungshierarchie stehen.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke2_1,
     'student_answer': 'In Smalltalk gibt es Metaklassen.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke2_1,
     'student_answer': 'Eine Metaklasse ist für Klassen verantwortlich.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke2_2,
     'student_answer': 'Vererbung soll die Wiederverwendbarkeit und die Wartbarkeit von Code verbessern. Dafür '
                       'vererben Superklasse Definitionen an ihre Subklassen.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke2_2,
     'student_answer': 'Vererbung hat nur Nachteile.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke2_2,
     'student_answer': 'Mehrfachvererbung ist beispielsweise in EIFFEL umgesetzt.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke2_2,
     'student_answer': 'Superklassen vererben Definitionen an ihre Subklassen.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke2_3,
     'student_answer': 'Nein, die Entfernen von Instanzvariablen oder Methoden ist unvereinbar mit Spezialisierungen.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke2_3,
     'student_answer': 'Ja, Spezialisierungen können Instanzvariablen oder Methoden entfernen.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke2_3,
     'student_answer': 'In Java können Instanzvariablen oder Methoden von Subklassen gelöscht werden.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke2_3,
     'student_answer': 'Vererbungshierarchien können von den Programmierenden frei erstellt werden.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke2_3,
     'student_answer': 'Generalisierungen können Instanzvariablen entfernen.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke2_3,
     'student_answer': 'Spezialisierungen können das nicht.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke3_1,
     'student_answer': 'Bei Parametrischem Polymorphismus wird in einer Typdefinition eine Typvariable verwendet, um '
                       'diese variabel zu halten. Bei der Instanziierung wird die Typvariable dann durch einen '
                       'konkreten Typ ersetzt.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke3_1,
     'student_answer': 'Parametrischem Polymorphismus wird über Typvariablen realisiert.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke3_1,
     'student_answer': 'Parametrischem Polymorphismus ist eine konkrete Typdefinition.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke3_1,
     'student_answer': 'Ein parametrischer Typ wird im Gleichheitstest verwendet.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke3_1,
     'student_answer': 'Bei der Instanziierung wird die Typvariable durch einen konkreten Typ ersetzt.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke3_2,
     'student_answer': 'Zwei Typen sind zuweisungskompatibel, wenn sie identisch oder typäquivalent sind.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke3_2,
     'student_answer': 'Zwei Typen sind zuweisungskompatibel, wenn sie sich sehr stark voneinander unterscheiden.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke3_2,
     'student_answer': 'Gleichheit und Identität von Objekten ist nicht das Gleiche.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke3_2,
     'student_answer': 'Es gibt strukturelle und nominale Typkonformität.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke3_2,
     'student_answer': 'Zwei Typen sind zuweisungskompatibel, wenn sie komplett identisch sind.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke3_3,
     'student_answer': 'Strukturelle Typkonformität besteht, wenn der konforme Typ alle Elemente des Typs, zu dem er '
                       'konform sein soll, enthält. Nominale Typkonformität besteht, wenn eine Übereinstimmung der '
                       'Typnamen besteht.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke3_3,
     'student_answer': 'Nominale Typkonformität besteht, wenn der konforme Typ alle Elemente des Typs, zu dem er '
                       'konform sein soll, enthält. Strukturelle Typkonformität heißt, dass die Typnamen übereinstimmen.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke3_3,
     'student_answer': 'In Java gibt es Wildcards.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke3_3,
     'student_answer': 'Es gibt strukturelle und nominale Typkonformität.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke3_3,
     'student_answer': 'Strukturelle Typkonformität besteht, wenn der konforme Typ alle Elemente des Typs, zu dem er '
                       'konform sein soll, enthält.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke3_3,
     'student_answer': 'Nominale Typkonformität besteht, wenn eine Übereinstimmung der Typnamen besteht.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke4_1,
     'student_answer': 'Interfaces in Java schaffen Schnittstellen, die von Klassen implementiert werden können.'
                       'Sie ermöglichen Code-Wiederverwendung, können als Verträge zwischen Klassen betrachtet werden'
                       'und stellen sicher, dass eine Klasse eine bestimmte Funktionalität bereitstellt.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke4_1,
     'student_answer': 'Interfaces in Java sind mit abstrakten Klassen gleichzusetzen.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke4_1,
     'student_answer': 'C++ erlaubt Mehrfachvererbung.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke4_1,
     'student_answer': 'Interfaces in Java ermöglichen die Wiederverwendung von Code.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke4_2,
     'student_answer': 'In Java gewähren Klassen sich untereinander privilegierten Zugriff, während nach außen nur '
                       'öffentlich deklarierte Programmelemente sichtbar sind.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke4_2,
     'student_answer': 'In Java haben Klassen keinen Zugriff aufeinander.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke4_2,
     'student_answer': 'In Java gibt es Zugriffskontrollmodifikatoren.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke4_3,
     'student_answer': 'Ja, C++ unterstützt objektorierte Programmierung. C++ bietet neben structs auch Klassen mit '
                       'Feldern und Methoden an.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke4_3,
     'student_answer': 'Nein, a, C++ unterstützt Objektorientierung nicht.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke4_3,
     'student_answer': 'EIFFEL unterstützt Mehrfachvererbung.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke4_3,
     'student_answer': 'Objektorientierung wird unterstützt.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke6_1,
     'student_answer': 'Das Fragile-Base-Class-Problem kann auftreten, wenn zwischen einer Klasse und ihren Subklassen '
                       'aufgrund der Vererbung von Eigenschaften eine hohe Abhängigkeiten besteht. Änderungen an der '
                       'Basisklasse können zu unerwünschten Auswirkungen in der abgeleiteten Klasse führen.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke6_1,
     'student_answer': 'Das Fragile-Base-Class-Problem ist das Problem, fragiler Basisklassen.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke6_1,
     'student_answer': 'Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke6_1,
     'student_answer': 'Das Fragile-Base-Class-Problem ist das Problem, dass unerwartete Ergebnissen auftreten.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke6_2,
     'student_answer': 'Das Geheimnisprinzip kann umgangen werden, indem Repräsentationsobjekte, deren Namen verborgen '
                       'werden sollen, noch andere Namen besitzen.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke6_2,
     'student_answer': 'Das Geheimnisprinzip kann nicht umgangen werden.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke6_2,
     'student_answer': 'Demeters Gesetz besagt, "Sprich nicht mit Fremden".'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke6_2,
     'student_answer': 'Das Geheimnisprinzip kann umgangen werden.'},
    {'expected': EvaluationType.CORRECT, 'correct_answer': answer_ke6_3,
     'student_answer': 'Der Nachteil des Liskov-Substitutionsprinzips ist, dass es sich in der Praxis als zu '
                       'restriktiv erweist. Das LSP lässt sich nicht automatisch überprüfen und weist auch '
                       'funktionierende Programme zurück.'},
    {'expected': EvaluationType.CONTRADICTS, 'correct_answer': answer_ke6_3,
     'student_answer': 'Das Liskov-Substitutionsprinzip ist gut geeignet, um die Funktionalität von Programmen zu '
                       'überprüfen.'},
    {'expected': EvaluationType.OFF_TOPIC, 'correct_answer': answer_ke6_3,
     'student_answer': 'Die Frage der Substituierbarkeit bezieht sich darauf, ob ein Objekt durch ein anderes Objekt '
                       'ersetzt werden kann.'},
    {'expected': EvaluationType.MISSING_TOPIC, 'correct_answer': answer_ke6_3,
     'student_answer': 'Das LSP lässt sich nicht automatisiert überprüfen.'}
]
