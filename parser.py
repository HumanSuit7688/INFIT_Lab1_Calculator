class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos]

    def advance(self):
        self.pos += 1

    def parse_factor(self):
        token = self.current_token()

        if token[0] == 'number':
            value = token[1]
            self.advance()
            return value

        elif token[0] == 'open_br':
            self.advance()  # пропустить '('
            value = self.parse_expression()  # рекурсивно разобрать выражение внутри
            self.advance()  # пропустить ')'
            return value

        elif token[0] == 'minus':
            self.advance()  # пропустить '-'
            value = self.parse_factor() * (-1)
            return value

    def parse_term(self):
        product = self.parse_factor()
        operator = self.current_token()[0]

        while operator in ['multiply', 'divide']:
            self.advance()  # ✅ пропускаем оператор (* или /)
            value = self.parse_factor()  # теперь читаем число

            if operator == 'multiply':
                product *= value
            elif operator == 'divide':
                product /= value

            operator = self.current_token()[0]

        return product


    def parse_expression(self):
        total = self.parse_term()
        operator = self.current_token()[0]

        while operator in ['plus', 'minus',]:
            self.advance()
            value = self.parse_term()

            if operator == 'plus':
                total += value
            elif operator == 'minus':
                total -= value

            operator = self.current_token()[0]

        return total