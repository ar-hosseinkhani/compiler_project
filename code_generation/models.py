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


temps = TemporaryIndex(1000)
