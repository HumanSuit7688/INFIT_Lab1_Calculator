class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos]

    def advance(self):
        self.pos += 1

    def parse_function_min(self):
        token = self.current_token()

        if token[0] == 'open_br':
            self.advance()
            token = self.current_token()

            list_numbers = []
            while(token[0] != 'close_br'):

                value = self.parse_expression()
                list_numbers.append(value)
                token = self.current_token()

                if token[0] == 'comma':
                    self.advance()
                    token = self.current_token()

            value = min(list_numbers)
            return value

        else:
            raise ValueError("Неправильно написана функция (отсутствует скобка в начале)")

    def parse_factor(self):
        token = self.current_token()

        if token[0] == 'number':
            value = token[1]
            self.advance()
            return value

        elif token[0] == 'open_br':
            self.advance()
            value = self.parse_expression()
            self.advance()
            return value

        elif token[0] == 'minus':
            self.advance()
            value = self.parse_factor() * (-1)
            return value

        elif token[0] == 'min':
            self.advance()
            value = self.parse_function_min()
            self.advance()
            return value


    def parse_term(self):
        product = self.parse_factor()
        operator = self.current_token()[0]

        while operator in ['multiply', 'divide']:
            self.advance()
            value = self.parse_factor()

            if operator == 'multiply':
                product *= value
            elif operator == 'divide':
                product /= value

            operator = self.current_token()[0]

        return product


    def parse_expression(self):
        total = self.parse_additive()
        operator = self.current_token()[0]

        while operator == 'bitwise_or':
            self.advance()
            value = self.parse_additive()
            total |= value

            operator = self.current_token()[0]

        return total

    def parse_additive(self):
        total = self.parse_term()
        operator = self.current_token()[0]

        while operator in ['plus', 'minus']:
            self.advance()
            value = self.parse_term()

            if operator == 'plus':
                total += value
            elif operator == 'minus':
                total -= value

            operator = self.current_token()[0]

        return total