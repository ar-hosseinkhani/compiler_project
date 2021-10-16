import string

START = 'start'
LET1 = 'let1'
LET2 = 'let2'
DIG1 = 'dig1'
DIG2 = 'dig2'
BLANK = 'blank'
SYMBOL = 'symbol'
EQ1 = 'eq1'
EQ2 = 'eq2'
EQEQ = 'eqeq'
CMT1 = 'cmt1'
CMT2 = 'cmt2'
CMT3 = 'cmt3'
CMT4 = 'cmt4'
CMTMF = 'cmtmf'
CMTSF = 'cmtsf'
CMTEF = 'cmtef'

Blanks = ['\f', '\t', ' ', '\n', '\v', '\r']
Symbols = [';', ':', ',', '[', ']', '(', ')', '{', '}', '+', '-', '*', '<', ]
Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Letters = [char for char in string.ascii_letters]
Keywords = ['if', 'else', 'void', 'int', 'repeat', 'break', 'until', 'return']

Accepting_States = [LET2, DIG2, BLANK, SYMBOL, EQ2, EQEQ, CMTMF, CMTSF, CMTEF]


class InvalidNumber(Exception):
    pass

class InvalidInput(Exception):
    pass