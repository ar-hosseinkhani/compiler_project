from parser_vars import *
from parser_vars import parser_data as data
from rules import *
from anytree import Node, RenderTree

tree_list = []
tree_list_father = []
stack_list = []
stack_list_father = []

stack_list.append("Program")
stack_list_father.append("-1")
data.set_next_token()


def create_tree():
    tree = [Node("Program")]
    for iteration in range(1, len(tree_list)):
        tree.append(Node(tree_list[iteration], parent=tree[int(tree_list_father[iteration])]))
    return tree[0]


while True:
    node = stack_list.pop()
    father_index = stack_list_father.pop()
    node_rules = productions.get(node)
    tree_list.append(node)
    tree_list_father.append(father_index)
    index = len(tree_list) - 1
    look_ahead_lexeme = data.lookahead.lexeme
    if look_ahead_lexeme == '$':
        if node == '$':
            break
        else:
            # Error
            pass
    if data.lookahead.type in ["NUM", "ID"]:
        look_ahead_lexeme = data.lookahead.type
    if node in non_terminals:
        valid = False
        for product in node_rules:
            for i in product:
                if look_ahead_lexeme in firsts.get(i):
                    valid = True
                    for pr in product[::-1]:
                        stack_list.append(pr)
                        stack_list_father.append(index)
                    break
                elif 'epsilon' not in firsts.get(i):
                    break
            if valid:
                break
        if not valid:
            if look_ahead_lexeme in follows.get(node):
                found_eps = True
                for product in node_rules:
                    found_eps = True
                    for lex in product:
                        if 'epsilon' not in firsts.get(lex):
                            found_eps = False
                            break
                    if found_eps:
                        for i in product[::-1]:
                            stack_list.append(i)
                            stack_list_father.append(index)
                        break

                if not found_eps:
                    # missing node in line of lexeme
                    pass
                pass
            else:
                # illegal lexeme in line of lexeme
                data.set_next_token()
                stack_list.append(node)
                stack_list_father.append(father_index)

    else:
        if node == 'epsilon':
            pass
        elif look_ahead_lexeme == node:
            tree_list[index] = '(' + data.lookahead.type + ', ' + data.lookahead.lexeme + ')'
            data.set_next_token()
        else:
            # missing node in line
            tree_list[index] = '(' + data.lookahead.type + ', ' + data.lookahead.lexeme + ')'
            # data.set_next_token()

for pre, _, node in RenderTree(create_tree()):
    print("%s%s" % (pre, node.name))
