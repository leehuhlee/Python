import sys

words = sys.argv
words.pop(0)
index = 1

for word in words:
    print(f"{index}. {word}")
    index += 1
