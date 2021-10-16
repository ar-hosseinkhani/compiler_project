from vars import *
from utils import *
from models import *

tokens = []
errors = []
symbols = Keywords.copy()
scanner_data = ScannerData()


def get_next_token():
    state = START

    while True:
        start, forward, line, program = scanner_data.start, scanner_data.forward, scanner_data.line, scanner_data.program
        char = scanner_data.program[forward]
        if char == '\n':
            line += 1
        if char not in Valid_Inputs and state not in [CMT2, CMT3, CMT4]:
            errors.append(Error('Invalid input', line, program[start:forward + 1]))
            scanner_data.program = program[forward + 1:]
            state = START


def get_next_state(state, c):
    if state == START:
        if is_eof(c):
            pass  # TODO: later
        elif is_blank(c):
            return BLANK
        elif is_letter(c):
            return LET1
        elif is_digit(c):
            return DIG1
        elif is_symbol(c):
            return SYMBOL
        elif c == '=':
            return EQ1
        elif c == '/':
            return CMT1

    elif state == LET1:
        if is_digit(c) or is_letter(c):
            return LET1
        # TODO: get next state inputs should be valid
        return LET2

    elif state == DIG1:
        if is_digit(c):
            return DIG1
        # TODO: same as letter (bad inputs should be checked)
        elif is_letter(c):
            raise InvalidNumber
        return DIG2

    elif state == EQ1:
        if c == '=':
            return EQEQ
        return EQ2

    elif state == CMT1:
        if c == '*':
            return CMT2
        elif c == '/':
            return CMT4
        raise InvalidInput()

    elif state == CMT2:
        if c == '*':
            return CMT3
        return CMT2

    elif state == CMT3:
        if c == '/':
            return CMTMF
        elif c == '*':
            return CMT3
        return CMT2

    elif state == CMT4:
        if c == '\n':
            return CMTSF
        elif is_eof(c):
            return CMTEF
        return CMT4


def create_token(final_state, lexeme, line_number):
    return True
