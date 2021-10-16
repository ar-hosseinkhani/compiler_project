from vars import *


def get_next_token():
    program = '''
        void main ( void ) {
        int a = 0;
        // comment1
        a = 2 + 2;
        return;
    }
    '''

    start = 0
    forward = 0
    line = 1
    state = START
    while True:
        char = program[forward]
        if char == '\n':
            line += 1
        state = get_next_state(state, char)
        if state in Accepting_States:
            token = create_token(state, program[start:forward+1], line)
            program = program[forward+1:]
            return token
        else:
            forward += 1


def get_next_state(state, c):
    if state == START:
        if c in Blanks:
            return WHS
        elif c in Symbols:
            return SYMBOL




def create_token(final_state, lexeme, line_number):
    return True
