from .classes import NumberNode, BinOp, AssignVar, Variable, Call


class Parser:
    def parse(self, tokens):
        self.tokens = tokens
        self.current = 0

        return self.parseAssign()

    def parseAssign(self):
        left = self.parseTerm()

        while self.match('='):
            if type(left) == Variable:
                left = AssignVar(left.name, self.parseAssign())
            else:
                raise Exception("Invalid assignment target (Must be a variable name)")

        return left
    

    def parseTerm(self):
        left = self.parseFactor()

        while self.match('+', '-'):
            op = self.previous()
            right = self.parseFactor()
            left = BinOp(left, right, op)

        return left

    def parseFactor(self):
        left = self.parsePower()

        while self.match('*', '/'):
            op = self.previous()
            right = self.parsePower()
            left = BinOp(left, right, op)

        return left

    def parsePower(self):
        left = self.parseCall()

        while self.match('^'):
            op = self.previous()
            right = self.parseCall()
            left = BinOp(left, right, op)

        return left

    def parseCall(self):
        left = self.parsePrimary()

        while self.match('('):
            left = self.finishCall(left)

        return left

    def finishCall(self, value):
        # parse parameters
        args = []
        if not self.check(')'):
            while True:
                args.append(self.parseAssign())

                # check for comma, if no comma, break
                if not self.match(','): break

        self.consume(')', "Expected ')' after function call")
        return Call(value, args)

    def parsePrimary(self):
        if self.match('number'):
            return NumberNode(self.previous().literal)
        if self.match('identifier'):
            return Variable(self.previous().lexeme)

        if self.match('('):
            expr = self.parseAssign()
            self.consume(')', "Expected ')' after grouping expression")
            return expr

        raise Exception("Expected expression")



    def consume(self, t_type, errmsg):
        if not self.check(t_type):
            raise Exception(errmsg)

        return self.advance()

    def match(self, *types):
        for t_type in types:
            if self.check(t_type):
                self.advance()
                return True
        return False

    def check(self, t_type):
        return self.peek().type == t_type

    def isAtEnd(self):
        return self.tokens[self.current].type == "EOF"

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current-1]

    def advance(self):
        self.current += 1
        return self.previous()