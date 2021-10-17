from dataclasses import dataclass


@dataclass
class Token:
    type: str
    line: int
    lexeme: str


@dataclass
class Error:
    type: str
    line: int
    lexeme: str


@dataclass
class Symbol:
    lexeme: str


class ScannerData:
    def __init__(self):
        self.start = 0
        self.forward = 0
        self.line = 1
        # TODO: this should be read from file
        program = '''
                void main ( void ) {
                int a = 0;
                // comment1
                a = 2 + 2;
                return;
            }
            '''
        self.program = program


class InvalidNumber(Exception):
    pass


class InvalidInput(Exception):
    pass


