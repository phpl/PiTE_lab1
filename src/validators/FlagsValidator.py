from src.excpetions.NoFlagsException import NoFlagsException


class FlagsValidator:
    @staticmethod
    def validate(flag: str):
        if not flag:
            raise NoFlagsException
