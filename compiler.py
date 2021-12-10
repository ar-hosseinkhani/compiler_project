from parser_vars import *
from parser_vars import parser_data as data


while (True):
    data.set_next_token()
    print(data.lookahead)
    if data.lookahead.lexeme == '$':
        break
