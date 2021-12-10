from parser_models import ParserData

firsts = {
    "Program": ['$', 'int', 'void'],
    "Declaration-list": ['epsilon', 'int', 'void'],
    "Declaration": ['int', 'void'],
    "Declaration-initial": ['int', 'void'],
    "Declaration-prime": ['(', ';', '['],
    "Var-declaration-prime": [';', '['],
    "Fun-declaration-prime": ['('],
    "Type-specifier": ['int', 'void'],
    "Params": ['int', 'void'],
    "Param-list": [',', 'epsilon'],
    "Param": ['int', 'void'],
    "Param-prime": ['[', 'epsilon'],
    "Compound-stmt": ['{'],
    "Statement-list": ['epsilon', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM'],
    "Statement": ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM'],
    "Expression-stmt": ['break', ';', 'ID', '(', 'NUM'],
    "Selection-stmt": ['if'],
    "Else-stmt": ['endif', 'else'],
    "Iteration-stmt": ['repeat'],
    "Return-stmt": ['return'],
    "Return-stmt-prime": [';', 'ID', '(', 'NUM'],
    "Expression": ['ID', '(', 'NUM'],
    "B": [':', '[', '(', '*', '+', '-', '<', '==', 'epsilon'],
    "H": [':', '*', 'epsilon', '+', '-', '<', '=='],
    "Simple-expression-zegond": ['(', 'NUM'],
    "Simple-expression-prime": ['(', '*', '+', '-', '<', '==', 'epsilon'],
    "C": ['epsilon', '<', '=='],
    "Relop": ['<', '=='],
    "Additive-expression": ['(', 'ID', 'NUM'],
    "Additive-expression-prime": ['(', '*', '+', '-', 'epsilon'],
    "Additive-expression-zegond": ['(', 'NUM'],
    "D": ['epsilon', '+', '-'],
    "Addop": ['+', '-'],
    "Term": ['(', 'ID', 'NUM'],
    "Term-prime": ['(', '*', 'epsilon'],
    "Term-zegond": ['(', 'NUM'],
    "G": ['*', 'epsilon'],
    "Factor": ['(', 'ID', 'NUM'],
    "Var-call-prime": ['(', '[', 'epsilon'],
    "Var-prime": ['[', 'epsilon'],
    "Factor-prime": ['(', 'epsilon'],
    "Factor-zegond": ['(', 'NUM'],
    "Args": ['epsilon', 'ID', '(', 'NUM'],
    "Arg-list": ['ID', '(', 'NUM'],
    "Arg-list-prime": [',', 'epsilon'],
    "ID": ['ID'],
    "NUM": ['NUM'],
    "if": ['if'],
    "else": ['else'],
    "void": ['void'],
    "int": ['int'],
    "repeat": ['repeat'],
    "break": ['break'],
    "until": ['until'],
    "return": ['return'],
    "endif": ['endif'],
    ";": [';'],
    ":": [':'],
    ",": [','],
    "[": ['['],
    "]": [']'],
    "(": ['('],
    ")": [')'],
    "{": ['{'],
    "}": ['}'],
    "+": ['+'],
    "-": ['-'],
    "*": ['*'],
    "<": ['<'],
    "=": ['='],
    "==": ['=='],
    "epsilon": ['epsilon']
}

follows = {
    "Program": [],
    "Declaration-list": ['$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}'],
    "Declaration": ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}'],
    "Declaration-initial": ['(', ';', '[', ',', ')'],
    "Declaration-prime": ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}'],
    "Var-declaration-prime": ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}'],
    "Fun-declaration-prime": ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}'],
    "Type-specifier": ['ID'],
    "Params": [')'],
    "Param-list": [')'],
    "Param": [',', ')'],
    "Param-prime": [',', ')'],
    "Compound-stmt": ['int', 'void', '$', '{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'endif',
                      'else', 'until'],
    "Statement-list": ['}'],
    "Statement": ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'endif', 'else', 'until'],
    "Expression-stmt": ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'endif', 'else', 'until'],
    "Selection-stmt": ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'endif', 'else', 'until'],
    "Else-stmt": ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'endif', 'else', 'until'],
    "Iteration-stmt": ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'endif', 'else', 'until'],
    "Return-stmt": ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'endif', 'else', 'until'],
    "Return-stmt-prime": ['{', 'break', ';', 'if', 'repeat', 'return', 'ID', '(', 'NUM', '}', 'endif', 'else', 'until'],
    "Expression": [';', ')', ']', ','],
    "B": [';', ')', ']', ','],
    "H": [';', ')', ']', ','],
    "Simple-expression-zegond": [';', ')', ']', ','],
    "Simple-expression-prime": [';', ')', ']', ','],
    "C": [';', ')', ']', ','],
    "Relop": ['(', 'ID', 'NUM'],
    "Additive-expression": [';', ')', ']', ','],
    "Additive-expression-prime": ['<', '==', ';', ')', ']', ','],
    "Additive-expression-zegond": ['<', '==', ';', ')', ']', ','],
    "D": ['<', '==', ';', ')', ']', ','],
    "Addop": ['(', 'ID', 'NUM'],
    "Term": ['+', '-', ';', ')', '<', '==', ']', ','],
    "Term-prime": ['+', '-', '<', '==', ';', ')', ']', ','],
    "Term-zegond": ['+', '-', '<', '==', ';', ')', ']', ','],
    "G": ['+', '-', '<', '==', ';', ')', ']', ','],
    "Factor": ['*', '+', '-', ';', ')', '<', '==', ']', ','],
    "Var-call-prime": ['*', '+', '-', ';', ')', '<', '==', ']', ','],
    "Var-prime": ['*', '+', '-', ';', ')', '<', '==', ']', ','],
    "Factor-prime": ['*', '+', '-', '<', '==', ';', ')', ']', ','],
    "Factor-zegond": ['*', '+', '-', '<', '==', ';', ')', ']', ','],
    "Args": [')'],
    "Arg-list": [')'],
    "Arg-list-prime": [')'],
}

non_terminals = list(follows.keys())

parser_data = ParserData()