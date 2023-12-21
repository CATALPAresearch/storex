"""
Script for starting a training exam.

Command line arguments are parsed and the training exam is started with the correct parameters.
"""
import logging
import sys

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from exam import ExamManager


# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--name", help="Name to be used to address you during the training exam.")
parser.add_argument("-t", "--time", default='25', help="Duration of the training exam in minutes between 10 and 60."
                                                       "Default: 25.")
parser.add_argument("-f", "--female", action='store_true',
                    help="Form of address 'Frau' will be used during the training exam.")
parser.add_argument("-m", "--male", action='store_true',
                    help="Form of address 'Herr' will be used during the training exam.")
parser.add_argument("-log", "--logging", action='store_true',
                    help="If set, logging info is enabled as console output.")
parser.add_argument("-na", "--no-audio", action='store_true',
                    help="If set, there will be no text-to-speech audio output. This can be set to increase the"
                         " performance.")
args = vars(parser.parse_args())

# Check if a name was given
if not args["name"]:
    print("No name is given. Please provide your name after -n.", file=sys.stderr)
    exit(1)

# Check if a maximum of one form of address was give
if args["female"] and args["male"]:
    print("Two forms of address were given.", file=sys.stderr)
    exit(1)

# Check and exit if number of players is not between 2 and 5 and therefore not legal
if int(args["time"]) > 60 or int(args["time"]) < 5:
    raise ValueError("The training exam can last between 10 to 60 minutes. Please choose a duration in that time frame.")

if args["logging"]:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.disabled = False

logging.info("Starting...")

# Run game with set arguments
exam = ExamManager(args)
exam.start_exam()

logging.info("Finished!")
