from code_generation.models import ProgramLine
from code_generation.models import temps as t

pb = []
ss = []


def get_temp():
    ss.append(t.temp_index)
    ss.append('#0')
    code_gen('#assign')
    t.temp_index += 4
    ss.pop()
    return str(t.temp_index - 4)


def code_gen(action_symbol):
    if action_symbol == '#assign':
        tl = len(ss)
        pb.append(ProgramLine('ASSIGN', ss[tl - 2], ss[tl - 1], ''))
        ss.pop()
    # elif action_symbol in ['#add', '#sub', '#mult', '#eq', '#lt']:
    elif action_symbol == '#big':
        temp = get_temp()
        tl = len(ss)
        pb.append(ProgramLine(ss[tl - 2], ss[tl - 3], ss[tl - 1], temp))  # خودمون به صورت درست وارد استک میکنیم
        ss.pop()
        ss.pop()
        ss.append(temp)
    elif action_symbol.startswith('#push_'):
        ss.append(action_symbol[6:].upper())

    elif action_symbol == '#save':
        ss.append(len(pb))
        pb.append('?')

    elif action_symbol == '#jp':
        pb[int(ss.pop())] = ProgramLine('JP', str(len(pb)), '', '')
    elif action_symbol == '#jpf_if':
        temp = ss.pop()
        pb[int(temp)] = ProgramLine('JPF', ss.pop(), str(len(pb) + 1), '')
        ss.append(len(pb))
        pb.append('?')
    elif action_symbol == '#jpf_repeat':
        temp = ss.pop()
        pb[int(ss.pop())] = ProgramLine('JPF', temp, str(len(pb)), '')
