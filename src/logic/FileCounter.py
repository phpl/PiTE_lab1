import string
from collections import Counter


class FileCounter:
    _filename = None

    def count(self, filename, flag):
        self._filename = filename

        if flag is 'chars':
            self._count_chars()
        elif flag is 'lines':
            self._count_lines()
        elif flag is 'words':
            self._count_words()

    def _count_chars(self):
        with open(self._filename) as file:
            letter_count = Counter()
            alphabet = string.ascii_letters

            for char in file.read():
                if char in alphabet:
                    letter_count[char] += 1

            print('Chars: ')
            print(letter_count)

    def _count_lines(self):
        with open(self._filename) as file:
            lines_count = Counter(file.read().lower().split('\n'))
            print('Lines: ')
            print(lines_count)

    def _count_words(self):
        with open(self._filename) as file:
            word_count = Counter(file.read().lower().split())
            print('Words: ')
            print(word_count)
