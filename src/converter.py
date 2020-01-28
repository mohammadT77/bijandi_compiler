

class GrammarConverter:
    DEFAULT_SEPARATE = "=>"
    EP = "@"
    __in_string:str

    def __init__(self, in_string: str) -> None:
        super().__init__()
        self.__in_string = in_string

    def get_lark(self):
        return self.__in_string.replace(GrammarConverter.DEFAULT_SEPARATE, ":") + """
%import common.WS
%import common.NUMBER
%import common.LETTER
%ignore WS
        """

    def get_ll1(self):
        return self.__in_string.replace(GrammarConverter.DEFAULT_SEPARATE, "->")
