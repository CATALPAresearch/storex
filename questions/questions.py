
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

KE6_problems = [
    {'question': "Was ist das Problem der Substituierbarkeit?",
     'keywords': ['Zuweisungskompatibilität', 'nichtkonforme Verhaltensänderung', 'keine Prüfung der Substituierbarkeit'],
     'follow-up': [KE6_solutions[0]]},
    # {'question': "Welche Probleme gibt es bei Subtyping unter Wertsemantik?", 'keywords': []},
    {'question': "Was ist das Fragile-Base-Class-Problem?",
     'keywords': ['Vererbung', 'starke Abhängigkeit', 'anfällige Subklasse', 'unvollständige Dokumentation',
                  'unerwartetes Verhalten'], 'follow-up': [KE6_solutions[1]]},
    {'question': "Was ist das Problem der schlechten Tracebarkeit?",
     'keywords': ['dynamischer Programmablauf', 'Goto-Anweisung', 'durchbrochenes Lokalitätsprinzip',
                  'Unterprogrammaufrufe', 'dynamisches Binden', 'schweres Debuggen']},
    {'question': "Was ist das Problem der eindimensionalen Strukturierung?",
     'keywords': ['Verlangen der Strukturierung nach mehreren Kriterien', 'unzureichende Trennung der Belange']},
    {'question': "Was ist das Problem der mangelnden Kapselung?",
     'keywords': ['Vererbung', 'starke Abhängigkeit', 'Aliasing-Problem', 'Geheimnisprinzip'], 'follow-up': [KE6_solutions[2]]},
    {'question': "Was ist das Aliasing-Problem?",
     'keywords': ['Zugriff auf gekapselte Objekte', 'Referenz auf Repräsentationsobjekte',
                  'Umgehen des Geheimnisprinzips', 'verschiedene Typen']},
    {'question': "Was ist das Problem der mangelnden Skalierbarkeit?", 'keywords': ['mangelnde Komponenten']},
    {'question': "Was ist das Problem der mangelnden Eignung?", 'keywords': ['geeignete Programmiersprache',
                                                                             'Abwägungsproblem']}
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
