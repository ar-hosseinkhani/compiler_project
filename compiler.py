from parser_vars import *
from parser_vars import parser_data as data
from rules import *
from anytree import Node, RenderTree



tree_list = []
tree_list_father = []
stack_list = []
stack_list_index = []

tree_list_father.append("-1")
tree_list.append("Program")
stack_list.append("Program")
stack_list_index.append("0")
data.set_next_token()

def create_tree():
    tree = [Node("Program")]
    for iter in range(1, len(tree_list)):
        tree.append(Node(tree_list[iter], parent=tree[int(tree_list_father[iter])]))
    return tree[0]


while (True):
    if data.lookahead.lexeme == '$':
        break
    node = stack_list.pop()
    node_index = stack_list_index.pop()
    node_rules = productions.get(node)
    if node in non_terminals:
        valid = False
        for product in node_rules:
            if data.lookahead.lexeme in firsts.get(product[0]):
                valid = True
                for i in product[::-1]:
                    tree_list.append(i)
                    tree_list_father.append(node_index)
                    stack_list.append(i)
                    stack_list_index.append(len(tree_list) - 1)

        if not valid:
            if data.lookahead.lexeme in follows.get(node):
                found_eps = True
                for product in node_rules:
                    for lex in product:
                        if lex not in non_terminals:
                            found_eps = False
                            break
                        if 'epsilon' not in firsts.get(lex):
                            found_eps = False
                            break
                    if found_eps:
                        for i in product[::-1]:
                            tree_list.append(i)
                            tree_list_father.append(node_index)
                            stack_list.append(i)
                            stack_list_index.append(len(tree_list) - 1)
                        break

                if not found_eps:
                    if 'epsilon' in node_rules:
                        tree_list.append('epsilon')
                        tree_list_father.append(node_index)
                    else:
                        # missing node in line of lexeme
                        pass
                pass
            else:
                # illegal lexeme in line of lexeme
                data.set_next_token()
                stack_list.append(node)
                stack_list_index.append(node_index)

    else:
        if data.lookahead.lexeme == node:
            tree_list[node_index] = '(' + data.lookahead.type + ', ' + node + ')'
            data.set_next_token()
        else:
            # missing node in line
            tree_list[node_index] = '(' + data.lookahead.type + ', ' + node + ')'
            # data.set_next_token()


    if data.lookahead.lexeme == '$':
        break

for pre, _, node in RenderTree(create_tree()):
        print("%s%s" % (pre, node.name))