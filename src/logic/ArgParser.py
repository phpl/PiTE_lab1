import argparse


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Own implementation of word counter.')
        self.parser.add_argument('filename', type=str)
        self.parser.add_argument('-m', '--chars', action='store_true')
        self.parser.add_argument('-l', '--lines', action='store_true')
        self.parser.add_argument('-w', '--words', action='store_true')

    def parse_arguments_to_dictionary(self):
        return vars(self.parser.parse_args())
