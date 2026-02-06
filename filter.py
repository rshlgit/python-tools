import sys

if len(sys.argv) != 3:
    print("Usage: python3 filter.py <word> <filename>")
    sys.exit(1)

word = sys.argv[1]
filename = sys.argv[2]

try:
    with open(filename) as f:
        for line in f:
            if word in line:
                print(line.strip())
except FileNotFoundError:
    print("Error: file not found: ", filename)
