class Lexer:
    def __init__(self, expression: str):
        self.expression = expression
        self.alph_numbers = '0123456789.'
        self.alph_operators = '+-*/|,'
        self.alph_brackets = '()'
        self.alph_functions = 'min'
        self.dict_operator_token = {
            '+': 'plus',
            '-': 'minus',
            '*': 'multiply',
            '/': 'divide',
            '|': 'bitwise_or',
            ',': 'comma'
        }
        self.dict_bracket_token = {
            '(': 'open_br',
            ')': 'close_br',
        }
        self.dict_function_token = {
            'min': 'min',
        }
        self.alphabet_main = self.alph_numbers + self.alph_operators + self.alph_brackets + self.alph_functions + ' '

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

        s_rep = s.replace('-', '+').replace('*', '+').replace('/', '+').replace('|', '+')
        if '++' in s_rep:
            raise ValueError("Два оператора подряд")

        if s[0] in '*/|':
            raise ValueError("Выражение не может начинаться с '*' или '/'")

        if s[-1] in '+-*/|min':
            raise ValueError("Выражение не может заканчиваться оператором")

        if s.count('(') != s.count(')'):
            raise ValueError("Несовпадение скобок")

        if '()' in s:
            raise ValueError("Пустые скобки")

        if 'm' in s or 'i' in s or 'n' in s:
            import re
            matches = re.findall(r'min', s)
            if len(matches) * 3 != s.count('m') + s.count('i') + s.count('n'):
                raise ValueError("Неправильно введена функция")

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
        """Токенизация выражения"""
        self.check_alphabet_expression()
        self.check_typo_expression()

        s = self.expression
        s = s.replace(' ', '')
        res_list = []
        i = 0

        while i < len(s):
            temp_char = s[i]

            # 1. Числа (включая точку)
            if temp_char in self.alph_numbers:
                num = ''
                while i < len(s) and s[i] in self.alph_numbers:
                    num += s[i]
                    i += 1
                res_list.append(('number', self.convert_num(num)))
                continue

            # 2. Слова (функции)
            elif temp_char in self.alph_functions:
                word = ''
                while i < len(s) and s[i] in self.alph_functions:
                    word += s[i]
                    i += 1

                if word == 'min':
                    token = self.dict_function_token.get(word)
                    res_list.append((token, token))
                else:
                    raise ValueError(f"Неизвестная функция или переменная: '{word}'")
                continue

            # 3. Операторы
            elif temp_char in self.alph_operators:
                token = self.dict_operator_token.get(temp_char)
                res_list.append((token, temp_char))
                i += 1

            # 4. Скобки
            elif temp_char in self.alph_brackets:
                token = self.dict_bracket_token.get(temp_char)
                res_list.append((token, temp_char))
                i += 1

            else:
                raise ValueError(f"Неожиданный символ: '{temp_char}'")

        res_list.append(('EOF', 'EOF'))
        return res_list