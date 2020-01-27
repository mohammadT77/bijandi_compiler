from unittest import TestCase
from src.models import *


class NonTerminalTest(TestCase):
    def test_create_new(self):
        self.assertEqual(NonTerminal("n").__str__(), 'N')


class TerminalTest(TestCase):
    def test_create_new(self):
        self.assertEqual(Terminal("n").__str__(), 'n')


class RuleTest(TestCase):
    def test_rule_static_method_parse_rhs_item(self):
        print(Rule.parse_rhs_item("asAs"))
        self.assertListEqual(Rule.parse_rhs_item("asAs"),[Token('a'),Token('s'),Token('A'),Token('s')])

    def test_rule_static_method_parse_rhs(self):
        res = Rule.parse_rhs("asAs|ac|$")
        print([[str(c) for c in r] for r in res])
        self.assertListEqual(res[0], [Token('a'), Token('s'), Token('A'), Token('s')])
        self.assertListEqual(res[1], [Token('a'), Token('c')])
        self.assertListEqual(res[2], [EPSILON_TOKEN])

    def test_create_rule_by_list(self):
        r = Rule("h")
        r.set_rhs("a1B|a|B")
        # print([[str(c) for c in r] for r in r.get_rhs()])
        print(r)
        self.assertEqual(str(r.get_lhs()), 'H')
        self.assertListEqual(r.get_rhs()[0], [Token('a'), Token('1'), Token('B')])
        self.assertListEqual(r.get_rhs()[1], [Token('a')])
        self.assertListEqual(r.get_rhs()[2], [Token('B')])

    def test_create_from_string(self):
        string1 = "a => a|aB|c|$"
        r = Rule.from_string(string1)
        print(r)
        # self.assertEqual(r.get_lhs().__str__(), 'A')


class GrammarTest(TestCase):
    def test_create_grammar_by_string(self):
        g = Grammar("""
        A=> a|B
        B=> b|C
        C=>c|$
        """)
        g.set_name("test")
        print(g)

    def test_create_grammar_by_string_list(self):
        rules = [
            'A=> a|B',
            'B=> b|C',
            'C=>c|$'
        ]
        g = Grammar(rules)
        g.set_name("test")
        print(g)
