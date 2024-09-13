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
Start the exam with `start_exam` (Windows) or `python start_exam`(Linux, MacOS)  followed by arguments.

This argument is mandatory:
```
-n <name> | --name <name>    with <name> being the name which is used during the oral
                             exam simulation
```

The following arguments are optional:
```
-t <time> | --time <time> whereas <time> is the time for the exam training.
                          Default: 25.
-f | --female             set a female voice for the speaker
-m | --male               set a male voice for the speaker

-h | --help               display this help text 

--log                     activate logging
--mute                    mute audio output
```

An example is the following: `start_exam -n Luna -f`

After starting the exam, answer each question, when the red text ***start_recording*** appears.
Each recording stops, after three seconds of silence or with a keyboard interrupt.

### Content of the repository
- The main folder contains the start script ***start_exam***, the exam manager, the evaluation manager, the feedback manager, the text generation component and the test script ***invoke_submodules.py***.
- The ***audio*** folder contains the Input Decoder and Output Decoder components
- The ***questions*** folder contains the components for question generation, assistance generation and the question manager.
- The ***utils*** folder contains helpers and functions for pre-processing scripts for the dialog system.
- The ***finetuning*** folder contains scripts for fine-tuning the T5 and Flan-T5 models.
- The ***data*** folder contains the raw and post-processed teaching materials, lists of technical terms, training data sets and vector databases.
- The ***dataprocessing*** folder contains scripts for data processing.
- The ***testing*** folder contains test results of the evaluation of the dialog system.


### Minimal system requirements:
The dialogue system has been tested with 
* Ubuntu 22.04.3 LTS, 32 GB Memory, AMD® Ryzen 7 5800x 8-core processor × 16, NVIDIA Corporation GP107 (GeForce GTX 1050 Ti)
* MacOS 14.4.1, Apple M1 (2020), MacBookPro, 16 GB Memory, 8 CPU cores, 8‑Core GPU, 16‑Core Neural Engine

# Roadmap
* include into demo
* provide web interface
* describe how content integration works
* install GPU support for mac: https://github.com/ggerganov/whisper.cpp



