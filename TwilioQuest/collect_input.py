import sys

words = sys.argv
words.pop(0)

for word in words:
    print(f"{word}")