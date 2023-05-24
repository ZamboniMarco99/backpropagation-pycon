import pyparsing


def parse_expression(expression: str) -> list:
    """
    Infix parsing of the expression
    """

    ppc = pyparsing.pyparsing_common

    pyparsing.ParserElement.enablePackrat()

    integer = ppc.integer
    real = ppc.real
    variable = pyparsing.Word(pyparsing.alphas, exact=1)
    operand = real | integer | variable

    expop = pyparsing.Literal("^")
    factop = pyparsing.Literal("!")
    ident = pyparsing.Word(pyparsing.alphas, pyparsing.alphanums + "_$")
    signop = pyparsing.oneOf("+ -")
    multop = pyparsing.oneOf("* /")
    plusop = pyparsing.oneOf("+ -")

    expr = pyparsing.infixNotation(
        operand,
        [
            (ident, 1, pyparsing.opAssoc.RIGHT),
            (factop, 1, pyparsing.opAssoc.LEFT),
            (expop, 2, pyparsing.opAssoc.RIGHT),
            (signop, 1, pyparsing.opAssoc.RIGHT),
            (multop, 2, pyparsing.opAssoc.LEFT),
            (plusop, 2, pyparsing.opAssoc.LEFT),
        ],
    )

    return expr.parse_string(expression).as_list()[0]
