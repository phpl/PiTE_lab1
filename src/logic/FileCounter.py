class FileCounter:
    filename = None

    def count(self, filename, flag):
        self.filename = filename

        if flag is 'chars':
            self._count_chars()
        elif flag is 'lines':
            self._count_lines()
        elif flag is 'words':
            self._count_words()

    def _count_lines(self):
        pass

    def _count_chars(self):
        pass

    def _count_words(self):
        pass
