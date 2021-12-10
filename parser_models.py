from scanner_part.scanner import get_next_token


class ParserData:

    def __init__(self):
        self.stack = []
        self.lookahead = None

    def set_next_token(self):
        self.lookahead = get_next_token()
