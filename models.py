from dataclasses import dataclass


@dataclass
class Token:
    type: str
    line: int
    lexeme: str


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
        int b;
        int foo(int d, int e){
            int f;
            void foo2(int k[]){
                return k[0] + k[1];	
            }
            int fff[2];
            fff[0] = d;
            fff[1] = d + 1;
            f = foo2(fff);
            b = e + f;
            repeat{
                f = f + d;
                d = d - 1;
                if (d == )
                    break;
                else d = 1;
            }until(0 < d)
            //comment1
            return f + b;
        }
        int arr[3];
        void main(void){
            int a;
            a = -3 + +11;
            b = 5 * a + foo(a, a);
            arr[1] = b + -3;
            arr[2] = foo(arr[0], arr[1]);
            if (b /*comment2*/ == 3){
                arr[0] = -7;	
            }
            return;
        }
        
        int foo(int d, int e){
            int a;
            a = 5;
            repeat {if (a == 5) break; else a = a + 1;} until (10 < a)
        }
        '''
        self.program = program


class InvalidNumber(Exception):
    pass


class InvalidInput(Exception):
    pass
