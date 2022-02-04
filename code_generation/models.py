from dataclasses import dataclass


@dataclass
class ProgramLine:
    command: str
    addr1: str
    addr2: str
    addr3: str

    def __str__(self):
        return f'({self.command}, {self.addr1}, {self.addr2}, {self.addr3})'


@dataclass
class TemporaryIndex:
    temp_index: int


@dataclass
class Symbol:
    lexeme: str
    address: int
    type: str
    no_args: int
    data_type: str
    scope: str


temps = TemporaryIndex(1000)
arrays = TemporaryIndex(2000)
