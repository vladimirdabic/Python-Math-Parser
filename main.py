from mathparser import Scanner, Parser, Interpreter
import math


scn = Scanner()
prs = Parser()

context = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sum': sum,
    'log': math.log
}

itp = Interpreter(context)


while True:
    inp = input("> ")

    if inp == "exit":
        break

    try:
        tokens = scn.scan(inp)
        tree = prs.parse(tokens)
        print(itp.evaluate(tree))
    except Exception as e:
        print(e)