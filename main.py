import sys
from lark import *
from src.models import *
from src.converter import GrammarConverter

OPTIONS = {
    'help': {
        'default': """
        -h , --help : Help
        -g , --grammar: Set Grammar by text 
        """
    },
    'grammar': {}
}


def print_option(option_name, attr=None, _continue=False):
    content = OPTIONS[option_name]
    if attr: content = content[attr]
    print(option_name, ":\n", content)
    if not _continue:
        exit()


def get_arg_option_name(arg):
    if arg[0:2] == '--':
        for opt in OPTIONS.keys():
            if arg[2:] == opt:
                return opt
        return None
    elif arg[0] == '-':
        for opt in OPTIONS.keys():
            if opt[0] == arg[1]:
                return opt
        return None
    else:
        return None


def help_mode():
    print()


def grammar_mode():
    from src.utils import find_lark_tree_tokens as find_tokens
    from os.path import isfile
    MAX_GRAMMAR_RULES = 10
    print("Enter your grammar rules or Grammar file address(end with !!!, Max : 10):")
    g = ""
    for i in range(MAX_GRAMMAR_RULES):
        _in = input()
        if isfile(_in) or isfile(_in[1:-1]):
            g = open(_in if isfile(_in) else _in[1:-1], 'r').read()
            break
        if _in == '!!!':
            break
        g += _in + "\n"

    start = input("Enter your start rule name: ")

    g_convert = GrammarConverter(g)

    p = Lark(g_convert.get_lark(), start=start.strip())
    try:
        p_tree = p.parse(input("Enter text: "))
        print(">>> Valid input String\n")
        print(">>> Tokens:\n", find_tokens(p_tree), "\n")
        print(">>> Tree map:\n", p_tree, "\n")
        print(">>> Tree:\n", p_tree.pretty(), "\n")
    except UnexpectedCharacters as e:
        print("\n", ">>> Invalid input String!\n", e)

    exit()


def main(args):
    print("\n===> Alireza Bijandi 952023044 : Compiler Project { Parser } <===\n")
    args = args[1:]
    if not args:
        print_option('help', 'default')
    if get_arg_option_name(args[0]) == 'help':
        print_option('help', 'default')
    elif get_arg_option_name(args[0]) == 'grammar':
        grammar_mode()
    else:
        print_option('help', 'default')


main(sys.argv)
