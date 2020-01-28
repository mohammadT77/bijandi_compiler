from unittest import TestCase
from src.models import *
from src.converter import GrammarConverter
from lark import *

class LarkTest(TestCase):

    def test_lark(self):
        g = open("C:\\Users\\Mohammad Amin\\PycharmProjects\\bijandi_compiler\\grammars\\test3_grammar.lark")
        g_convert = GrammarConverter(g)

        p = Lark(g, start='exp')
        tree = p.parse("_e = 1 + 2 * 3")
        from src.utils import find_lark_tree_tokens
        print(find_lark_tree_tokens(tree))
        print(tree)
