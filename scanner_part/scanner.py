from utils import *
from models import *
from vars import scanner_data as info


def get_next_token():
    state = START
    token = None

    mlc_start_line = 0

    while True:
        char = info.program[info.forward]
        if is_eof(char):
            if state in [CMT2, CMT3]:
                lexeme = info.program[info.start:info.forward]
                if len(lexeme) > 7:
                    lexeme = lexeme[:7] + '...'
                handle_error('Unclosed comment', mlc_start_line, lexeme)
            elif state in [LET1, DIG1, EQ1]:
                return create_token(state, info.line, info.program[info.start:info.forward])
            elif state == CMT1:
                handle_error('Invalid input', info.line, info.program[info.start:info.forward])
            return None

        if state == CMT2 and not mlc_start_line:
            mlc_start_line = info.line

        if char not in Valid_Inputs and state not in [CMT2, CMT3, CMT4]:
            if state == DIG1:
                handle_error('Invalid number', info.line, info.program[info.start:info.forward + 1])
            else:
                handle_error('Invalid input', info.line, info.program[info.start:info.forward + 1])
            state = START
            continue
        elif char == '*' and scanner_data.program[info.forward + 1] == '/' and state not in [CMT2, CMT4]:
            info.forward += 1
            handle_error('Unmatched comment', info.line, info.program[info.start:info.forward + 1])
            state = START
            continue

        try:
            state = get_next_state(state, char)

        except InvalidInput:
            handle_error('Invalid input', info.line, info.program[info.start:info.forward + 1])
            state = START
            continue
        except InvalidNumber:
            handle_error('Invalid number', info.line, info.program[info.start:info.forward + 1])
            state = START
            continue

        if is_star_state(state):
            info.forward -= 1
        if is_final_state(state):
            token = create_token(state, info.line, info.program[info.start:info.forward + 1])
            scanner_data.program = info.program[info.forward + 1:]
            scanner_data.forward = 0

        if char == '\n' and not is_star_state(state):
            info.line += 1

        if token:
            return token

        if state == CMTMF:
            mlc_start_line = 0

        if is_final_trash_state(state):
            state = START
            continue

        info.forward += 1


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
            if c == '*' and (
                    info.program[info.forward + 1] not in Valid_Inputs or info.program[info.forward + 1] == '/'):
                info.forward += 1
                raise InvalidInput
            # TODO test 9
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
            raise InvalidNumber()
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
        info.forward -= 1
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


while True:
    token = get_next_token()
    if token:
        # print(token)
        continue
    else:
        break
