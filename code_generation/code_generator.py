from code_generation.models import ProgramLine
from code_generation.models import Symbol
from code_generation.models import temps as t
from code_generation.models import arrays as a
from code_generation.models import current_scope as cs
from code_generation.models import no_params as np

tree_list = []

pb = []
ss = []
symbols = []
repeat_breaks = []


def get_temp():
    ss.append(t.index)
    ss.append('#0')
    code_gen('#assign')
    t.index += 4
    ss.pop()
    return t.index - 4


def get_space_for_array(num: int):
    for i in range(num):
        ss.append(a.index)
        ss.append('#0')
        code_gen('#assign')
        a.index += 4
        ss.pop()
    return str(a.index - 4 * num)


def get_symbol(lexeme: str, scope: str):
    for s in symbols:
        if s.lexeme == lexeme and s.scope == scope:
            return s
    return "none"


def get_symbol_by_address(address: int):
    for s in symbols:
        if s.address == address:
            return s
    return "none"


def code_gen(action_symbol):
    if action_symbol == '#assign':
        tl = len(ss)
        pb.append(ProgramLine('ASSIGN', ss[tl - 1], ss[tl - 2], ''))
        ss.pop()
    # elif action_symbol in ['#add', '#sub', '#mult', '#eq', '#lt']:
    elif action_symbol == '#big':
        temp = get_temp()
        tl = len(ss)
        pb.append(ProgramLine(ss[tl - 2], ss[tl - 3], ss[tl - 1], temp))  # خودمون به صورت درست وارد استک میکنیم
        ss.pop()
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
        pb.append(ProgramLine('JP', str(ln + 2), '', ''))
        pb.append('?')
        repeat_breaks.append(ln+1)
    elif action_symbol == '#set_break':
        pb.append(ProgramLine('JP', repeat_breaks[len(repeat_breaks)-1], '', ''))
    elif action_symbol == '#jp':
        pb[int(ss.pop())] = ProgramLine('JP', str(len(pb)), '', '')
    elif action_symbol == '#jpf_if':
        temp = ss.pop()
        pb[int(temp)] = ProgramLine('JPF', ss.pop(), str(len(pb) + 1), '')
        ss.append(len(pb))
        pb.append('?')
    elif action_symbol == '#jpf_repeat':
        address = repeat_breaks.pop()
        pb.append(ProgramLine('JPF', ss.pop(), str(address + 1), ''))
        ln = len(pb)
        pb[int(address)] = ProgramLine('JP', str(ln), '', '')
    elif action_symbol == "#gp_id":
        ss.append(tree_list[len(tree_list) - 1][
                  tree_list[len(tree_list) - 1].index(',') + 2: len(tree_list[len(tree_list) - 1]) - 1])
    elif action_symbol == "#add_id":
        tl = len(ss)
        symbols.append(Symbol(ss[tl - 1], int(get_temp()), "var", 0, ss[tl - 2], cs.scope_name))
        ss.pop()
        ss.pop()
    elif action_symbol == "#add_array":
        no_args = int(ss.pop())
        tl = len(ss)
        array_address = get_space_for_array(no_args)
        address = get_temp()
        pb.append(ProgramLine('ASSIGN', f'#{array_address}', address, ''))
        symbols.append(Symbol(ss[tl - 1], int(address), "array", no_args, ss[tl - 2], cs.scope_name))
        ss.pop()
        ss.pop()
    elif action_symbol == "#add_fun":
        tl = len(ss)
        address = get_temp()
        symbols.append(Symbol(ss[tl - 1], int(address), "fun", 0, ss[tl - 2], cs.scope_name))
        cs.scope_name = ss[tl - 1]
        cs.has_set_fun_pointer = False
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
        s = get_symbol(cs.scope_name, "0")
        s.no_args = np.index
    elif action_symbol == "#set_fun_pointer":
        if not cs.has_set_fun_pointer:
            cs.has_set_fun_pointer = True
            s = get_symbol(cs.scope_name, "0")
            ln = len(pb)
            if cs.scope_name == 'main':
                pb.append(ProgramLine("ASSIGN", f'#{ln + 1}', s.address, ''))
            else:
                pb.append(ProgramLine("ASSIGN", f'#{ln + 2}', s.address, ''))
                ss.append(ln + 1)
                pb.append('?')
    elif action_symbol == "#pop":
        ss.pop()
    elif action_symbol == '#return_jp':
        s = get_symbol(cs.scope_name, "0")
        pb.append(ProgramLine('JP', f'@{(s.address + 8)}', '', ''))
    elif action_symbol == '#return_sjp':
        s = get_symbol(cs.scope_name, "0")
        pb.append(ProgramLine('ASSIGN', ss.pop(), str(s.address + 4), ''))
        pb.append(ProgramLine('JP', f'@{(s.address + 8)}', '', ''))
    elif action_symbol == "#get_id":
        s = get_symbol(tree_list[len(tree_list) - 1][
                       tree_list[len(tree_list) - 1].index(',') + 2: len(tree_list[len(tree_list) - 1]) - 1],
                       cs.scope_name)
        if s == 'none':
            s = get_symbol(tree_list[len(tree_list) - 1][
                           tree_list[len(tree_list) - 1].index(',') + 2: len(tree_list[len(tree_list) - 1]) - 1], "0")
        ss.append(str(s.address))
    elif action_symbol == '#get_array_item':
        temp1 = get_temp()
        pb.append(ProgramLine('MULT', "#4", ss.pop(), temp1))
        temp2 = get_temp()
        pb.append(ProgramLine('ADD', temp1, ss.pop(), temp2))
        ss.append(f'@{temp2}')
    elif action_symbol == '#get_num':
        alt = tree_list[len(tree_list) - 1][
              tree_list[len(tree_list) - 1].index(',') + 2: len(tree_list[len(tree_list) - 1]) - 1]
        ss.append(f'#{alt}')
        print("hello")
    elif action_symbol == '#reset_no':
        s = get_symbol_by_address(int(ss[len(ss) - 1]))
        s.no_args_computed = 0
    elif action_symbol == "#add_arg":
        s = get_symbol_by_address(int(ss[len(ss) - 2]))
        temp1 = get_temp()
        pb.append(ProgramLine('MULT', "#4", f'#{s.no_args_computed}', temp1))
        s.no_args_computed = s.no_args_computed + 1
        temp2 = get_temp()
        lt = len(ss)
        pb.append(ProgramLine('ADD', f'#{ss[lt - 2]}', "#12", temp2))
        temp3 = get_temp()
        pb.append(ProgramLine('ADD', temp1, temp2, temp3))
        pb.append(ProgramLine('ASSIGN', ss[lt - 1], f'@{temp3}', ''))
        ss.pop()
    elif action_symbol == "#call_fun":
        temp1 = get_temp()
        lt = len(ss)
        pb.append(ProgramLine('ADD', f'#{ss[lt - 1]}', "#8", temp1))
        ln = len(pb)
        pb.append(ProgramLine('ASSIGN', f'#{ln + 2}', f'@{temp1}', ''))
        pb.append(ProgramLine('JP', f'@{ss[lt - 1]}', '', ''))  # nemidoonam adresdehi doroste ya na???!!!
        temp2 = get_temp()
        pb.append(ProgramLine('ADD', f'#{ss[lt - 1]}', "#4", temp2))
        temp3 = get_temp()
        pb.append(ProgramLine("ASSIGN", f'@{temp2}', temp3, ''))
        ss.pop()
        ss.append(temp3)
    elif action_symbol == '#init':
        address = get_temp()
        symbols.append(Symbol("output", address, "fun", 1, "void", "0"))
        pb.append(ProgramLine("ASSIGN", '#3', address, ''))
        pb.append(ProgramLine('JP', '#5', '', ''))
        pb.append(ProgramLine('PRINT', str(address + 12), '', ''))
        pb.append(ProgramLine('JP', f'@{address + 8}', '', ''))
        get_temp()
        get_temp()
        get_temp()
    elif action_symbol == '#reset_scope':
        if cs.scope_name != 'main':
            s = get_symbol(cs.scope_name, "0")
            pb.append(ProgramLine('JP', f'@{(s.address + 8)}', '', ''))
            ln = len(pb)
            pb[int(ss.pop())] = ProgramLine('JP', str(ln), '', '')
        cs.scope_name = "0"
        cs.has_set_fun_pointer = False
    else:
        print('ERROR!', action_symbol)
