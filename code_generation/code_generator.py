from code_generation.models import ProgramLine
from code_generation.models import Symbol
from code_generation.models import temps as t
from code_generation.models import arrays as a
from compiler import tree_list
from code_generation.models import current_scope as cs
from code_generation.models import no_params as np

pb = []
ss = []
symbols = []


def get_temp():
    ss.append(t.index)
    ss.append('#0')
    code_gen('#assign')
    t.index += 4
    ss.pop()
    return str(t.index - 4)


def get_space_for_array(num: int):
    for i in range(num):
        ss.append(a.index)
        ss.append('#0')
        code_gen('#assign')
        a.index += 4
        ss.pop()
    return str(a.index - 4 * num)

def get_symbol(lexeme: str, typ: str, scope: str):
    for s in symbols:
        if s.lexeme == lexeme and s.type == typ and s.scope == scope:
            return s
    return "none"

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
        ss.append(action_symbol[6:])

    elif action_symbol == '#save':
        ss.append(len(pb))
        pb.append('?')
    elif action_symbol == '#save_r':
        ln = len(pb)
        pb.append(ProgramLine('JP', str(ln+2), '', ''))
        ss.append(ln+1)
        pb.append('?')
    elif action_symbol == '#set_break':
        pb.append(ProgramLine('JP', ss[len(ss)-1], '', ''))
    elif action_symbol == '#jp':
        pb[int(ss.pop())] = ProgramLine('JP', str(len(pb)), '', '')
    elif action_symbol == '#jpf_if':
        temp = ss.pop()
        pb[int(temp)] = ProgramLine('JPF', ss.pop(), str(len(pb) + 1), '')
        ss.append(len(pb))
        pb.append('?')
    elif action_symbol == '#jpf_repeat':
        tl = len(ss)
        pb.append(ProgramLine('JPF', ss[tl-1], str(int(ss[tl - 2]) + 1), ''))
        pb[int(ss[tl-2])] = ProgramLine('JP', str(len(pb)), '', '')
        ss.pop()
        ss.pop()
    elif action_symbol == "#gp_id":
        ss.append(tree_list[len(tree_list)-1])
    elif action_symbol == "#add_id":
        tl = len(ss)
        symbols.append(Symbol(ss[tl-1], get_temp(), "var", 0, ss[tl-2], cs.scope_name))
        ss.pop()
        ss.pop()
    elif action_symbol == "#add_array":
        tl = len(ss)
        no_args = int(ss.pop())
        array_address = get_space_for_array(no_args)
        address = get_temp()
        pb.append(ProgramLine('ASSIGN', f'(#{array_address})', address, ''))
        symbols.append(Symbol(ss[tl-1], address, "array", no_args, ss[tl-2], cs.scope_name))
        ss.pop()
        ss.pop()
    elif action_symbol == "#add_fun":
        tl = len(ss)
        address = get_temp()
        symbols.append(Symbol(ss[tl - 1], address, "fun", 0, ss[tl - 2], cs.scope_name))
        cs.scope_name = ss[tl-1]
        np.index = 0
        get_temp()
        get_temp()
        ss.pop()
        ss.pop()
    elif action_symbol == "#add_pararr":
        tl = len(ss)
        symbols.append(Symbol(ss[tl - 1], get_temp(), "arr", 0, ss[tl - 2], cs.scope_name))
        ss.pop()
        ss.pop()
    elif action_symbol == "#inc_par":
        np.index += 1
    elif action_symbol == "#set_nopar":
        s = get_symbol(cs.scope_name, "fun", "0")
        s.no_args = np.index
    elif action_symbol == "#pop":
        ss.pop()
