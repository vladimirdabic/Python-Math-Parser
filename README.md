A simple math parser, supports functions and variables.

```
> 2+2*2
6
> cos(0)
0.0
> (2+2)*2
8
```

Using the parser in your project:

```py
import mathparser

scanner = mathparser.Scanner()
parser = mathparser.Parser()
itp = mathparser.Interpreter()

def calc(expr): 
  tree = parser.parse(scanner.scan(expr))
  return itp.evaluate(tree)


print(calc("2+2*2"))
```

Defining custom context:
```py
import mathparser

scanner = mathparser.Scanner()
parser = mathparser.Parser()

ctx = {
  "two": 2,
  "sum": lambda *args: sum(args)
}

itp = mathparser.Interpreter(ctx)

def calc(expr): 
  tree = parser.parse(scanner.scan(expr))
  return itp.evaluate(tree)


print(calc("two*2"))
print(calc("sum(two, 3)"))
```
