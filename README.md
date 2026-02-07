# Python Tools

Small command-line p;ractice tools built while learning Python + the Unix CLI

## Tools

### analyzer.py / analyzer_v2.py
Count lines, words, and characters

File mode:
    python3 analyzer_v2.py sample.txt

Pipe mode:
    cat sample.txt | python3 analyzer_v2.py

### calc.py
CLI Calculator:
    python3 calc.py 3 "+" 5
    python3 calc.py 10 "*" 2

### filter.py
Print lines containing a word:
    python3 filter.py sample.txt

## Goal

Practice building small Unix-style tools:
- argument parsing
- stdin vs files
- error handling
- composable scripts
