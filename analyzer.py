import sys

if len(sys.argv) != 2:
    print("Usage: python3 analyzer.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as f:
        text = f.read()
except FileNotFoundError:
    print("Error: file not found:", filename)
    sys.exit(1)

lines = len(text.splitlines())
words = len(text.split())
chars = len(text)

print(lines, words, chars, filename)


