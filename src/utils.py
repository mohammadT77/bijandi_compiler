from lark import *


def find_lark_tree_tokens(tree: Tree) -> list:
    res = []
    for t in tree.children:
        if isinstance(t, Token):
            res.append(t)
        else:
            res = res + find_lark_tree_tokens(t)
    return res
