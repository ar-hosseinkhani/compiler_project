from dataclasses import dataclass


@dataclass
class Token:
    type: str
    line: int
    lexeme: str

    def __str__(self):
        return f'({self.type}, {self.lexeme})'


@dataclass
class Error:
    type: str
    line: int
    lexeme: str


@dataclass
class Symbol:
    lexeme: str


class ScannerData:
    def __init__(self):
        self.start = 0
        self.forward = 0
        self.line = 1
        # TODO: this should be read from file
        program = '''
// zero point

int hell(int id){
	re%peat {
		if (1000 < scars)
			break;
		else
			scars = 1scars + 1;
	} until (1 < 0)
	// now we have scars
	return party(id);
}

int party(int id) {
	repeat {
		scars = scars - 1;
		happiness = happiness + 1;
	} until (scars == 0)
	// The lower you fall the higher youll fly
	return party(id);
}

int ids[3000];
int configs[3000];
void main(void){
	int equity;
	int effort;
	int scars;
	int pr;
	effort  = 0;
	scars = 0;
	pr = 5;
	configs[1] = 0;
	equity  = 10;
	equity  = 10 + 3;
	ids[1] = 3333;
	ids[2] = 4444;
	if (configs[1] /*comment*/ == 1){
		// I dont want to die without any scars
		repeat {
			scars = scars + 1;
			effort = effort + 10;
			pr = pr + 50;
		} until (10 < scars)
		party(ids[1]);
	}
	else
	{
		repeat {
			effort = effort + 1;
			equity = equity + 10;
		} until (1000 < equity)
		// The things you used to own now they own you
		hell(ids[1]);
	}
	return;
}
        '''
        self.program = program


class InvalidNumber(Exception):
    pass


class InvalidInput(Exception):
    pass
