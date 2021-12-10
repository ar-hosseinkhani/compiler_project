from dataclasses import dataclass


@dataclass
class Token:
    type: str
    line: int
    lexeme: str

    def __str__(self):
        return f'({self.type}, {self.lexeme})'


@dataclass
class Error:
    type: str
    line: int
    lexeme: str

    def __str__(self):
        return f'({self.lexeme}, {self.type})'


@dataclass
class Symbol:
    lexeme: str


class ScannerData:
    def __init__(self):
        self.start = 0
        self.forward = 0
        self.line = 1
        # TODO: this should be read from file
        f = open('../input.txt', 'r')
        # program = f.read() + chr(5)
        program = f.read() + '$'

        self.program = program


class InvalidNumber(Exception):
    pass


class InvalidInput(Exception):
    pass
