# Trainer für mündliche Prüfungen
## Kurs: Objektorientierte Programmierung


Beginne eine Trainingsprüfung durch Aufrufen von ***python3 start_exam.py*** gefolgt von Argumenten.

Die folgenden Argumente sind obligatorisch anzugeben:

```
-n <name> | --name <name>    wobei <name> der eigenen Namen ist, der für die
                             Trainingsprüfung verwendet werden soll
```

Die folgenden Argumente sind optional:
```
-t <time> | --time <time>    wobei <time> die Trainingszeit in Minuten ist.
                             Default: 25.
-f | --female                um die Ansprache als weiblich festzulegen
-m | --male                  um die Ansprache als männlich festzulegen

-log | --logging             um Logging zu aktivieren
-na  | --no-audio            um Audio auszuschalten
```