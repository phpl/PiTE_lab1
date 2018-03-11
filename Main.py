import datetime
import logging

from src.logic.ArgParser import ArgParser
from src.logic.FileCounter import FileCounter
from src.validators.FileValidator import FileValidator


def parse():
    logging.log(logging.INFO, 'Start parsing:' + str(datetime.datetime.now()))
    parser = ArgParser()
    arguments = parser.parse_arguments_to_dictionary()
    logging.log(logging.INFO, 'End parsing:' + str(datetime.datetime.now()))

    return arguments


def validate():
    try:
        logging.log(logging.INFO, 'Start validating:' + str(datetime.datetime.now()))
        FileValidator.validate(parsed_arguments['filename'])
        logging.log(logging.INFO, 'End validating:' + str(datetime.datetime.now()))
    except FileNotFoundError:
        logging.log(logging.WARN, 'File not found')
        print("File not found")


def count():
    try:
        logging.log(logging.INFO, 'Start counting:' + str(datetime.datetime.now()))
        file_counter = FileCounter()
        file_counter.count(**parsed_arguments)
        logging.log(logging.INFO, 'End counting:' + str(datetime.datetime.now()))
    except TypeError:
        logging.log(logging.WARN, 'Flags not found')
        print("Flags not found")


if __name__ == '__main__':
    logging.basicConfig(filename='logs.log', level=logging.INFO)

    parsed_arguments = parse()
    validate()
    count()
