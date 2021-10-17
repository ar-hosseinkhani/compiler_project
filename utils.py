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


def is_star_state(state):
    return state in Star_States


def is_eof(char):
    pass


def is_final_trash_state(final_state):
    return final_state in [BLANK, CMTMF, CMTSF, CMTEF]


def get_token_type(final_state, lexeme):
    if final_state == LET2:
        return 'KEYWORD' if is_keyword(lexeme) else 'ID'
    elif final_state == DIG2:
        return 'NUM'
    elif final_state in [SYMBOL, EQ2, EQEQ]:
        return 'SYMBOL'
    raise NotImplementedError()


def create_token(final_state, line_number, lexeme):
    if is_final_trash_state(final_state):
        return None
    token_type = get_token_type(final_state, lexeme)
    token = Token(token_type, line_number, lexeme)
    tokens.append(token)
    return token


def handle_error(error_type, line, lexeme):
    create_error(error_type, line, lexeme)
    scanner_data.program = scanner_data.program[scanner_data.forward + 1:]
    scanner_data.forward = 0


def create_error(error_type, line_number, lexeme):
    errors.append(Error(error_type, line_number, lexeme))
