from parser import Parser
from lexer import Lexer

def calculate(expression):
    """Вычисление значения арифметического выражения"""
    lexer = Lexer(expression)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    result = parser.parse_expression()

    return result

def tokenize(expression):
    lexer = Lexer(expression)
    tokens = lexer.tokenize()
    return tokens

if __name__ == '__main__':
    tokens = tokenize(input('Enter expression: '))
    print(tokens)