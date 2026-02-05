text = open("text.txt").read().lower()
words = text.split()

counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1

print(counts)