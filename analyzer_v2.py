import sys

def read_lines():
    # File mode: analyzer_v2.py <filename>
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: file not found: {filename}", file=sys.stderr)
            sys.exit(1)

    # No file and no stdin        
    elif sys.stdin.isatty():
        print("Usage: python3 analyzer_v2.py [filename]\n"
              "  If no file is given, reads from stdin.", file=sys.stderr)
        sys.exit(1)
    
    # Stdin mode: cat file | analyzer_v2.py
    else:
        return sys.stdin.read()

text = read_lines()

lines = len(text.splitlines())
words = len(text.split())
chars = len(text)

print(lines, words, chars)
