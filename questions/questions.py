"""
Questions
"""
from enum import IntEnum


class KE(IntEnum):
    KE1 = 0
    KE2 = 1
    KE3 = 2
    KE4 = 3
    KE5 = 4
    KE6 = 5
    KE7 = 6


KE1_questions = []
KE2_questions = []
KE3_questions = []
KE4_questions = []
KE5_questions = []
KE7_questions = []

# TODO: Bring keywords in preprocessed Form
KE6_solutions = [
    {'question': "Was ist das Liskov-Substitutionsprinzip?",
     'keywords': ['verhaltensbezogenes Subtyping', 'Subtypenrelation', 'Kontravarianz der Argumenttypen',
                  'Kovarianz des Ergebnistyps', 'Kovarianz der Ausnahmen', 'implizierte Vorbedingungen',
                  'implizierende Nachbedingungen', 'implizierende Invarianten', 'restriktiv']},
    {'question': "Welchen Lösungsansatz gibt es für das Fragile-Base-Class-Problem?",
     'keywords': ['explizites Vererbungsinterface', 'Zugriffsmodifikatoren']},
    {'question': "Welchen Lösungsansatz gibt es für das Problem der mangelnden Kapselung?",
     'keywords': ['Teil-Ganzes-Beziehung', 'kein Alias auf Wertobjekte']},
]

KE6_questions = [
    # {'question': "Was ist das Problem der Substituierbarkeit?",
    #  'keywords': ['Zuweisungskompatibilität', 'nichtkonforme Verhaltensänderung', 'keine Prüfung der Substituierbarkeit'],
    #  'follow-up': [KE6_solutions[0]]},
    # {'question': "Welche Probleme gibt es bei Subtyping unter Wertsemantik?", 'keywords': []},
    {'question': "Was ist das Fragile-Base-Class-Problem?",
     'keywords': ['Vererbung', 'starke Abhängigkeit', 'anfällige Subklasse', 'unvollständige Dokumentation',
                  'unerwartetes Verhalten'],
     'answer': 'Das Fragile-Base-Class-Problem bezieht sich auf eine Gruppe von Problemen in der Vererbung von Klassen.'
               'Wenn zwischen einer Klasse und ihren Subklassen aufgrund der Vererbung von Eigenschaften starke'
               'Abhängigkeiten bestehen, können Änderungen an der Basisklasse, welche etwa durch eine unvollständige'
               'Dokumentation nicht auffallen, zu unerwarteten und unerwünschten Auswirkungen in der abgeleiteten'
               'Klasse führen.', 'follow-up': [KE6_solutions[1]]},
    {'question': "Was ist das Problem der schlechten Tracebarkeit?",
     'keywords': ['dynamischer Programmablauf', 'Goto-Anweisung', 'durchbrochenes Lokalitätsprinzip',
                  'Unterprogrammaufrufe', 'dynamisches Binden', 'schweres Debuggen'],
     'answer': 'Das Problem der schlechten Tracebarkeit entsteht durch den dynamischen Programmablauf. Die'
               'Goto-Anweisung erlaubt Sprünge von beliebigen Stellen eines Programms zu anderen Stellen und bricht'
               'dabei das Lokalitätsprinzip von Programmen, bei dem zusammengehörende Anweisungen im Programmtext nahe'
               'beieinander stehen. Dies führte zu einer Unübersichtlichkeit im Programmtext und erschwerte das'
               'Verstehen und Debuggen von Programmen.'},
    {'question': "Was ist das Problem der eindimensionalen Strukturierung?",
     'keywords': ['Verlangen der Strukturierung nach mehreren Kriterien', 'unzureichende Trennung der Belange'],
     'answer': 'Bei größeren Programmen kann das Bedürfnis entstehen, ein Programm nach mehreren Kriterien gleichzeitig'
               'zu strukturieren, da verschiedene Vererbungshierarchien oder andere Strukturierungskriterien'
               'gleichzeitig relevant sein können. Die Trennung der Belange, auch als Separation of Concerns bekannt,'
               'wird in der objektorientierten Programmierung als unzureichend unterstützt angesehen, da es schwer ist,'
               'verschiedene Aspekte eines Systems sauber voneinander zu trennen.'},
    {'question': "Was ist das Problem der mangelnden Kapselung?",
     'keywords': ['Vererbung', 'starke Abhängigkeit', 'Aliasing-Problem', 'Geheimnisprinzip'], 'follow-up': [KE6_solutions[2]],
      'answer': 'Die Vererbung in der objektorientierten Programmierung beeinträchtigt die Kapselung von Klassen auf'
                'unangenehme Weise. Vererbung führte zu starken Abhängigkeiten zwischen Klassen und ihren Subklassen,'
                'einschließlich der Implementierungsdetails. Diese Abhängigkeiten führten dazu, dass Teile der'
                'Ausdrucksstärke und Flexibilität der objektorientierten Programmierung aufgegeben werden mussten. Das'
                'Aliasing-Problem tritt auf, wenn ein Objekt, das von einem anderen Objekt gekapselt wird, auch einen'
                'Alias besitzt, der nicht selbst dem kapselnden Objekt gehört. Dies bedeutet, dass von außen auf das'
                'gekapselte Objekt zugegriffen werden kann, indem man den Alias verwendet. Dies stellt eine'
                'Herausforderung für die Kapselung dar, da es die Geheimhaltung der Implementierung durchbrechen kann.'}
    # {'question': "Was ist das Aliasing-Problem?",
    #  'keywords': ['Zugriff auf gekapselte Objekte', 'Referenz auf Repräsentationsobjekte',
    #               'Umgehen des Geheimnisprinzips', 'verschiedene Typen']},
    # {'question': "Was ist das Problem der mangelnden Skalierbarkeit?", 'keywords': ['mangelnde Komponenten']},
    # {'question': "Was ist das Problem der mangelnden Eignung?", 'keywords': ['geeignete Programmiersprache',
    #                                                                          'Abwägungsproblem']}
]

KE6_open_questions = [
    {'question': "Was sind Probleme der objektorientierten Programmierung?",
     'keywords': ["Problem der Substituierbarkeit",
                  "Liskov-Substitutionsprinzip",
                  "Fragile-Base-Class-Problem",
                  "Problem der schlechten Tracebarkeit",
                  "Problem der eindimensionalen Strukturierung",
                  "Problem der mangelnden Kapselung",
                  "Problem der mangelnden Skalierbarkeit",
                  "Problem der mangelnden Eignung"]}
]
