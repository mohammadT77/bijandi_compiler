import sys
from src.models import *

OPTIONS = {
    'help': {
        'default': """
        -h , --help : Help
        -g , --grammar: Set Grammar by text 
        """
    },
    'grammar': {}
}

print()
exit()

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
    print("Enter your grammar (max rules: %d, `$` for escape) :\n" % Grammar.MAX_RULES)
    grammar_str_array = []
    for i in range(Grammar.MAX_RULES):
        r = input("rule %d#:\t" % (i + 1))
        if r == '$': break
        grammar_str_array.append(r)
    grammar = None
    try:
        grammar = Grammar(grammar_str_array)
    except Exception as e:
        print("Error: ", e)
        exit()
    name = input("Enter Grammar name (Optional): ")
    if name:
        grammar.set_name(name)

    print(grammar)


def main(args):
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