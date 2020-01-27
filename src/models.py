EPSILON_SYMBOL = '$'


class Token:
    __t = EPSILON_SYMBOL

    def __init__(self, t=EPSILON_SYMBOL) -> None:
        super().__init__()
        self.__t = t

    def __str__(self) -> str:
        return self.__t

    def __eq__(self, o: object) -> bool:
        return str(o) == str(self)

    def is_nonterminal(self) -> bool:
        return str(self.__t).isupper()

    def get_t(self):
        return self.__t


EPSILON_TOKEN = Token()


class NonTerminal(Token):

    def __init__(self, name: str) -> None:
        super().__init__(name.upper())


class Terminal(Token):
    pass

# class RHSItem:
#     __tokens: list = [EPSILON_TOKEN]
#
#     def __init__(self, tokens: (str,list) = None) -> None:
#         super().__init__()
#         if tokens:
#             self.set_tokens(tokens)


    # def set_tokens(self, tokens:(str,list)):
    #     res = []
    #     tokens = tokens if isinstance()
    #     for s in string.split('|'):
    #         res.append([Token(c) for c in s])
    #     return res


class Rule:
    SPLITTER_SYMBOL = '=>'

    __lhs: NonTerminal
    __rhs: list = [EPSILON_TOKEN]

    def __init__(self, lhs: (NonTerminal, str), rhs: list = None) -> None:
        super().__init__()
        self.__lhs = lhs if isinstance(lhs, NonTerminal) else NonTerminal(lhs)
        if rhs is not None:
            self.set_rhs(rhs)

    @staticmethod
    def parse_rhs_item(string: str):
        return [Token(t) for t in string]

    @staticmethod
    def parse_rhs(string: str):
        return [Rule.parse_rhs_item(r_item) for r_item in string.split('|')]

    @staticmethod
    def from_string(string: str):
        if not string:
            return None
        string_array = string.replace(' ', '').split(Rule.SPLITTER_SYMBOL)
        r = Rule(NonTerminal(string_array[0]), Rule.parse_rhs(string_array[1]))
        return r

    def set_rhs(self, rhs: (list, str)) -> None:
        if isinstance(rhs, list):
            self.__rhs = [Rule.parse_rhs_item(r_item) for r_item in rhs]
        elif isinstance(rhs, str):
            self.__rhs = Rule.parse_rhs(rhs)
        else:
            raise Exception('Invalid Type')

    def get_lhs(self) -> NonTerminal:
        return self.__lhs

    def get_rhs(self) -> list:
        return self.__rhs

    def __str__(self) -> str:
        rhs_str = ""
        for r in self.get_rhs():
            for t in r:
                rhs_str += str(t.get_t())
            rhs_str += "|"
        rhs_str = str(rhs_str[0:-1])
        return "%s %s %s" % (self.__lhs, Rule.SPLITTER_SYMBOL, rhs_str)


class Grammar:
    MAX_RULES = 10
    __name: str = None
    __rules: list

    def __init__(self, rules: (list, str) = [], name: str = None) -> None:
        super().__init__()
        self.set_rules(rules)
        self.set_name(name)
        if len(self.__rules) > 10:
            raise Exception("Max number of rules : " + str(Grammar.MAX_RULES))

    def get_rules(self):
        return self.__rules.copy()

    def set_rules(self, rules: (list, str)):
        if isinstance(rules, str):
            rules = rules.replace(' ', '').splitlines()
        res = []
        for r in rules:
            if isinstance(r, Rule):
                res.append(r)
            elif isinstance(r, str):
                res.append(Rule.from_string(r))
            else:
                raise Exception("Invalid Rule")
        for i in res:
            if i is None:
                res.remove(i)
        self.__rules = res

    def add_rule(self, rule: (Rule, str)):
        self.__rules.append(rule if isinstance(rule, Rule)
                            else Rule.from_string(rule))

    def set_name(self, name: str):
        self.__name = name

    @staticmethod
    def from_string(string: str):
        g = Grammar()
        g.set_rules(string)
        return g

    def __str__(self) -> str:
        res = self.__name + ":\n" if self.__name else ""
        for r in self.__rules:
            res += str(r) + "\n"
        return res

    def find_rule_by_lhs(self, lhs: (str, NonTerminal)):
        for r in self.__rules:
            if r.get_lhs() == lhs:
                return r
        return None


    # def get_rhs_derivations(self, rhs:list):
    #     for r in rhs:
    #         d1 = []
    #         for t in r:
    #             d2 = []
    #             if not t.is_nonterminal:
    #                 d2.append(t)
    #             else:
    #                 d2.append(self.find_rule_by_lhs(t))
    #             d1.append(d2)
    #


    def print_all_derivations(self, rule=None):
        if rule:
            if isinstance(rule, str) or isinstance(rule, NonTerminal):
                rule = self.find_rule_by_lhs(rule)
            elif isinstance(rule, int):
                rule = self.__rules[rule]

        if rule:
            if not isinstance(rule, Rule):
                return None
            rhses = rule.get_rhs()
            for rhs in rhses:
                pass