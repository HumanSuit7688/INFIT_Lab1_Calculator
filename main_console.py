from Backend.parser import Parser
from Backend.lexer import Lexer


def calculate(expression):
    """Вычисление значения арифметического выражения"""
    lexer = Lexer(expression)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    result = parser.parse_expression()

    return result

if __name__ == '__main__':
    expression = input('Enter expression: ')
    while expression:
        result = calculate(expression)
        print(result)
        expression = input('Enter expression: ')