class Lexer:
    def __init__(self, expression: str):
        self.expression = expression
        self.alph_numbers = '0123456789.'
        self.alph_operators = '+-*/'
        self.alph_brackets = '()'
        self.dict_operator_token = {
            '+': 'plus',
            '-': 'minus',
            '*': 'multiply',
            '/': 'divide',
        }
        self.dict_bracket_token = {
            '(': 'open_br',
            ')': 'close_br',
        }
        self.alphabet_main = '0123456789+-*/(). '

    def check_alphabet_expression(self):
        """Проверка символов выражения на соответствие алфавиту"""
        for char in self.expression:
            if char not in self.alphabet_main:
                raise ValueError(f"Недопустимый символ: '{char}'")

    def check_typo_expression(self):
        """Проверка на опечатки в выражении"""
        s = self.expression.strip()

        if not s:
            raise ValueError("Выражение пустое")

        s_rep = s.replace('-', '+').replace('*', '+').replace('/', '+')
        if '++' in s_rep:
            raise ValueError("Два оператора подряд")

        if s[0] in '*/':
            raise ValueError("Выражение не может начинаться с '*' или '/'")

        if s[-1] in '+-*/':
            raise ValueError("Выражение не может заканчиваться оператором")

        if s.count('(') != s.count(')'):
            raise ValueError("Несовпадение скобок")

        if '()' in s:
            raise ValueError("Пустые скобки")

    def convert_num(self, str_num: str):
        """Конвертация строки в число"""
        try:
            if '.' not in str_num:
                return int(str_num)
            else:
                return float(str_num)
        except ValueError:
            raise ValueError(f"Некорректное число: '{str_num}'")

    def tokenize(self):
        """Проверка и токенизация выражения"""
        self.check_alphabet_expression()
        self.check_typo_expression()

        s = self.expression
        res_list = []
        num = ''

        for i in range(len(s)):
            temp_char = s[i]
            if temp_char == ' ':
                continue
            elif temp_char in self.alph_numbers:
                num += temp_char
                if i == (len(s) - 1) or s[i + 1] not in self.alph_numbers:
                    token = 'number'
                    res_list.append((token, self.convert_num(num)))
                    num = ''
            elif temp_char in self.alph_operators:
                token = self.dict_operator_token.get(temp_char)
                res_list.append((token, temp_char))
            elif temp_char in self.alph_brackets:
                token = self.dict_bracket_token.get(temp_char)
                res_list.append((token, temp_char))

        res_list.append(('EOF', 'EOF'))
        return res_list