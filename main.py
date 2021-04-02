from mathparser import Scanner, Parser, Interpreter, pretty_print
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


print("Type 'exit' to exit")
print("Type 'tree' to toggle printing tree")
print_tree = False

while True:
    inp = input("> ")

    if inp == "exit":
        break
    elif inp == "tree":
        print_tree = not print_tree
        print(f"Printing tree {'on' if print_tree else 'off'}")
        continue

    try:
        tokens = scn.scan(inp)
        tree = prs.parse(tokens)

        if print_tree:
            print("root")
            pretty_print(tree)

        print(itp.evaluate(tree))
    except Exception as e:
        print(e)