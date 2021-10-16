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


def is_eol(char):
    return char == '\n'


def is_eof(char):
    pass
