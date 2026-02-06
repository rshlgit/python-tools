import sys

if len(sys.argv) != 4:
    print("Usage: python3 calc.py <num1> <op> <num2>")
    sys.exit(1)

a = float(sys.argv[1])
op = sys.argv[2]
b = float(sys.argv[3])

try:
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("Unknown Operator")
except ZeroDivisionError:
    print("Error: division by zero")

