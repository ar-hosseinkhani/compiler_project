from code_generation.models import ProgramLine
from code_generation.models import temps as t

pb = []
ss = []


def get_temp():
    ss.append(t.temp_index)
    ss.append('#0')
    code_gen('#assign')
    t.temp_index += 4
    return str(t.temp_index - 4)


def code_gen(action_symbol):
    if action_symbol == '#assign':
        tl = len(ss)
        pb.append(ProgramLine('ASSIGN', ss[tl - 2], ss[tl - 1], ''))
        ss.pop()
        ss.pop()
    elif action_symbol in ['#add', '#sub', '#mult', '#eq', '#lt']:
        temp = get_temp()
        tl = len(ss)
        pb.append(ProgramLine(action_symbol[1:].upper(), ss[tl - 2], ss[tl - 1], temp))
        ss.pop()
        ss.pop()
        ss.append(temp)


