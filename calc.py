import sys
import operator

if len(sys.argv) != 4:
    print("Usage: python3 calc.py <num1> <op> <num2>")
    sys.exit(1)

a = float(sys.argv[1])
op = sys.argv[2]
b = float(sys.argv[3])

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

try:
    result = ops[op](a, b)
    print(result)
except KeyError:
    print("Unknown Operator")
except ZeroDivisionError:
    print("Error: division by zero")

