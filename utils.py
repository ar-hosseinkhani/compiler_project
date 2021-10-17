from vars import *


def is_digit(char):
    return char in Digits


def is_letter(char):
    return char in Letters


def is_keyword(text):
    return text in Keywords


def is_symbol(char):
    return char in Symbols


def is_blank(char):
    return char in Blanks


def is_final_state(state):
    return state in Final_States


def is_eof(char):
    pass


def create_token(final_state, line_number, lexeme):
    return True


def handle_error(error_type, line, lexeme):
    create_error(error_type, line, lexeme)
    scanner_data.program = scanner_data.program[scanner_data.forward + 1:]
    scanner_data.forward = 0


def create_error(error_type, line_number, lexeme):
    errors.append(Error(error_type, line_number, lexeme))
