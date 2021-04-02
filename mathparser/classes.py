

class Token:
    def __init__(self, t_type, lexeme, literal, line):
        self.type = t_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __repr__(self):
        return f"Token(type: {self.type}, lexeme: {self.lexeme}, literal: {self.literal}, line: {self.line})"





class NumberNode:
    def __init__(self, num):
        self.value = num

    def __repr__(self):
        return f"Number({self.value})"

class BinOp:
    def __init__(self, l, r, op):
        self.left = l
        self.right = r
        self.op = op

    def __repr__(self):
        return f"BinOp({self.left} {self.op} {self.right})"

class AssignVar:
    def __init__(self, varname, v):
        self.name = varname
        self.value = v

    def __repr__(self):
        return f"Assign({self.name} = {self.value})"

class Variable:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Variable({self.name})"

class Call:
    def __init__(self, value, args):
        self.value = value
        self.args = args

    def __repr__(self):
        return f"Call({self.value}, {self.args})"

class ArrayNode:
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        return f"Array{self.elements}"

class IndexFrom:
    def __init__(self, value, idx):
        self.value = value
        self.idx = idx

    def __repr__(self):
        return f"IndexFrom({self.value}: {self.idx})"

class SetAtIndex:
    def __init__(self, value, idx, new):
        self.value = value
        self.idx = idx
        self.new = new

    def __repr__(self):
        return f"SetAtIndex({self.value}: {self.idx})"