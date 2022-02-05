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
    index: int


@dataclass
class Symbol:
    lexeme: str
    address: int
    type: str
    no_args: int
    data_type: str
    scope: str
    no_args_computed: int = 0


@dataclass
class Scope:
    scope_name: str
    has_set_fun_pointer: bool


current_scope = Scope("0", False)
temps = TemporaryIndex(1000)
arrays = TemporaryIndex(2000)
no_params = TemporaryIndex(0)
no_inner_condition = TemporaryIndex(0)
