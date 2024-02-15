# Dialoge system as a trainer for oral exams
## Course: Object-oriented Programming
Find the German version below.

### Preparation:
1. Clone the repository **theses / DialogSystems / oral-exam-simulation**
   `git clone git@gitlab.pi6.fernuni-hagen.de:theses/dialogsystems/oral-exam-simulation.git`
2. Change into the directory ***oral-exam-simulation***
   `cd oral-exam-simulation`
3. Install the python packages in ***requirements.txt***. The last four packages are not necessary for execution only..
   `pip install -r requirements.txt`
4. Make the file ***start_exam*** executable, for example via `chmod +x start_exam`
5. Create a Hugging Face Account or log into an existing account under: https://huggingface.co/
6. Create a Hugging Face API Token with the account under: https://huggingface.co/settings/tokens
7. Copy the Hugging Face API Token into ***hf_token.py*** instead of 'hf_xxx'


### Execution of an oral exam simulation:
Start the exam with ***start_exam*** followed by arguments.

This argument is mandatory:
```
-n <name> | --name <name>    with <name> being the name which is used during the oral
                             exam simulation
```

The following arguments are optional:
```
-t <time> | --time <time> wobei <time> die Trainingszeit in Minuten ist.
                          Default: 25.
-f | --female             um die Ansprache als weiblich festzulegen
-m | --male               um die Ansprache als männlich festzulegen

-h | --help               um den Hilfstext anzeigen zu lassen  

--log                     um Logging zu aktivieren
--mute                    um die Audioausgabe auszuschalten
```

An example is the following: `start_exam -n Luna -f`

### Content of the repository
- The main folder contains the start script ***start_exam***, the exam manager, the evaluation manager, the feedback manager, the text generation component and the test script ***invoke_submodules.py***.
- The ***audio*** folder contains the Input Decoder and Output Decoder components
- The ***questions*** folder contains the components for question generation, assistance generation and the question manager.
- The ***utils*** folder contains helpers and functions for pre-processing scripts for the dialog system.
- The ***finetuning*** folder contains scripts for fine-tuning the T5 and Flan-T5 models.
- The ***data*** folder contains the raw and post-processed teaching materials, lists of technical terms, training data sets and vector databases.
- The ***dataprocessing*** folder contains scripts for data processing.
- The ***testing*** folder contains test results of the evaluation of the dialog system.


### Minimum requirements:
The dialog system was tested on Linux under Ubuntu 22.04.3 LTS with:
- 32 GB Memory 
- AMD® Ryzen 7 5800x 8-core processor × 16
- NVIDIA Corporation GP107 [GeForce GTX 1050 Ti]



# Dialogsteuerung eines Trainers für mündliche Prüfungen
## Kurs: Objektorientierte Programmierung

### Vorbereitungen:
1. Clone das Repository **theses / DialogSystems / oral-exam-simulation**
   `git clone git@gitlab.pi6.fernuni-hagen.de:theses/dialogsystems/oral-exam-simulation.git`
2. Wechsel in den Ordner ***oral-exam-simulation**
   `cd oral-exam-simulation`
3. Installiere die Python Packages in ***requirements.txt***. Die unteren vier Packages werden nicht für die Ausführung benötigt.
   `pip install -r requirements.txt`
4. Mache die Datei ***start_exam*** ausführbar, beispielsweise mittels `chmod +x start_exam`
5. Erstelle einen Hugging Face Account oder logge in einen Account ein unter: https://huggingface.co/
6. Erstelle einen Hugging Face API Token mit diesem Account unter: https://huggingface.co/settings/tokens
7. Kopiere den Hugging Face API Token in ***hf_token.py*** an die Stelle von 'hf_xxx'


### Ausführung einer Trainingsprüfung:
Beginne eine Trainingsprüfung durch Aufrufen von ***start_exam*** im Terminal gefolgt von Argumenten.

Die folgenden Argumente sind obligatorisch anzugeben:

```
-n <name> | --name <name>    wobei <name> der eigenen Namen ist, der für die
                             Trainingsprüfung verwendet werden soll
```

Die folgenden Argumente sind optional:
```
-t <time> | --time <time> wobei <time> die Trainingszeit in Minuten ist.
                          Default: 25.
-f | --female             um die Ansprache als weiblich festzulegen
-m | --male               um die Ansprache als männlich festzulegen

-h | --help               um den Hilfstext anzeigen zu lassen  

--log                     um Logging zu aktivieren
--mute                    um die Audioausgabe auszuschalten
```

Ein Beispielaufruf lautet `start_exam -n Luna -f`

### Inhalt des Repositories
- Im Hauptordner befindet sich das startscript ***start_exam***, der Prüfungsmanager, der Evaluierungsmanager, der Feedbackmanager, die Komponente der Textgenerierung und das Testscript ***invoke_submodules.py***.
- Im Ordner ***audio*** befinden sich die Komponenten Input Decoder und Output Decoder
- Im Ordner ***questions*** befinden sich die Komponenten für die Fragegenerierung, Generierung von Hilfestellungen und der Fragemanager.
- Im Ordner ***utils*** befinden sich Helpers und Funktionen für die Vorverarbeitung für das Dialogsystem.
- Im Ordner ***finetuning*** befinden sich Scripte für das Finetuning der Modelle T5 und Flan-T5.
- Im Ordner ***data*** befinden sich die rohen und nachbearbeiteten Lehrmaterialien, Listen der Fachbegriffe, Trainingsdatensätze und Vektordatenbanken.
- Im Ordner ***dataprocessing*** befinden sich Scripte für die Datenverarbeitung.
- Im Ordner ***testing*** befinden sich die Testergebnisse der Evaluierung des Dialogsystems.


### Mindestanforderungen:
Getestet wurde das Dialogsystem auf Linux unter Ubuntu 22.04.3 LTS mit:
- 32 GB Memory 
- AMD® Ryzen 7 5800x 8-core processor × 16
- NVIDIA Corporation GP107 [GeForce GTX 1050 Ti]
