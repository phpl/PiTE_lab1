import os.path


class FileValidator:
    @staticmethod
    def validate(filename: str):
        if not os.path.isfile(filename):
            raise FileNotFoundError
