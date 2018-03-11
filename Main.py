from src.logic.ArgParser import ArgParser
from src.logic.FileCounter import FileCounter
from src.validators.FileValidator import FileValidator
from src.validators.FlagsValidator import FlagsValidator

if __name__ == '__main__':
    parser = ArgParser()
    arguments = parser.parse_arguments_to_dictionary()

    FileValidator.validate(arguments['filename'])
    FlagsValidator.validate(arguments['flag'])

    file_counter = FileCounter()
    file_counter.count(**arguments)
