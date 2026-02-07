import sys

if len(sys.argv) != 3:
    print("Usage: python3 filter.py <word> <filename>")
    sys.exit(1)

word, filename = sys.argv[1:]

try:
    with open(filename, "r") as f:
        for line in f:
            if word.lower() in line.lower():
                print(line.strip())
except FileNotFoundError:
    print("file  not found:", filename)

