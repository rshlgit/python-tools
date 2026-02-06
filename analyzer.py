import sys

def read_input():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
             with open(filename, "r") as f:
                 return f.read()
        except FileNotFoundError:
            print("Error: file not found:", filename)
            sys.exit(1)
    else:
        return sys.stdin.read()

text = read_input()

lines = len(text.splitlines())
words = len(text.split())
chars = len(text)

print(lines, words, chars)


