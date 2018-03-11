import argparse


class ArgParser:
    _result_dictionary = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Own implementation of word counter.')
        self.parser.add_argument('filename', type=str)
        self.parser.add_argument('-m', '--chars', action='store_true')
        self.parser.add_argument('-l', '--lines', action='store_true')
        self.parser.add_argument('-w', '--words', action='store_true')

    def parse_arguments_to_dictionary(self):
        arguments = vars(self.parser.parse_args())

        self._result_dictionary = {'filename': arguments['filename']}
        self._add_flag_to_dictionary(arguments)

        return self._result_dictionary

    def _add_flag_to_dictionary(self, arguments):
        for key, value in arguments.items():
            if self._can_add_parameter_to_dictionary(value):
                self._result_dictionary['flag'] = key

    def _can_add_parameter_to_dictionary(self, value):
        return type(value) is bool and value is True

