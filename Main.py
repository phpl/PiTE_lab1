import datetime

from src.logic.ArgParser import ArgParser
from src.logic.FileCounter import FileCounter
from src.validators.FileValidator import FileValidator
from src.validators.FlagsValidator import FlagsValidator
import logging


def parse():
    logging.log(logging.INFO, 'Start parsing:' + str(datetime.datetime.now()))
    parser = ArgParser()
    arguments = parser.parse_arguments_to_dictionary()
    logging.log(logging.INFO, 'End parsing:' + str(datetime.datetime.now()))

    return arguments


def validate():
    logging.log(logging.INFO, 'Start validating:' + str(datetime.datetime.now()))
    FileValidator.validate(parsed_arguments['filename'])
    FlagsValidator.validate(parsed_arguments['flag'])
    logging.log(logging.INFO, 'End validating:' + str(datetime.datetime.now()))


def count():
    logging.log(logging.INFO, 'Start counting:' + str(datetime.datetime.now()))
    file_counter = FileCounter()
    file_counter.count(**parsed_arguments)
    logging.log(logging.INFO, 'End counting:' + str(datetime.datetime.now()))


if __name__ == '__main__':
    logging.basicConfig(filename='logs.log', level=logging.INFO)

    parsed_arguments = parse()
    validate()
    count()

