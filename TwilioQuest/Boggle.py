import nltk
from nltk.corpus import words

nltk.download('words')
dictionary = words.words()

board = [['r', 'n', 'o'],
         ['a', 'j', 's'],
         ['p', 'y', 'f']]

def solve(board, dictionary):
    max_lengths = {}
    for word in dictionary:
        if word[0] not in max_lengths:
            max_lengths[word[0]] = min(len(word), 9)
        else:
            max_lengths[word[0]] = max(min(len(word), 9), max_lengths[word[0]])

    found = {}

    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            max_length = 0
            if letter in max_lengths:
                max_length = max_lengths[letter]
            check_the_combined_word(board, i, j, max_length, letter, [[i, j]], found)

    return found

def check_the_combined_word(board, x, y, max_length, combined_word, green_ones, found):
    at = lambda cell: board[cell[0]][cell[1]]

    if len(combined_word) > max_length:
        return

    if len(combined_word) <= max_length:
        if (combined_word in dictionary) and (len(combined_word) == 5):
            found[combined_word] = 1

    nbrs = neighbors([x, y], board)
    green_ones.append([x, y])

    for n in nbrs:
        if not_visited(n, green_ones.copy()):
            check_the_combined_word(board, n[0], n[1], max_length, combined_word + at(n), green_ones, found)
    green_ones.pop()

def neighbors(point, board):
    num_rows = len(board)
    num_cols = len(board[0])

    ret = []
    for next_cell in [[+1, 0],
                      [-1, 0],
                      [0, -1],
                      [0, +1],
                      [+1, +1],
                      [-1, +1],
                      [-1, -1],
                      [+1, -1]]:
        if (0 <= point[0] + next_cell[0] < num_rows) and (0 <= point[1] + next_cell[1] < num_cols):
            ret.append([point[0] + next_cell[0], point[1] + next_cell[1]])
    return ret

def not_visited(x, visited):
    L = len(list(filter(lambda  o: o[0] == x[0] and o[1] == x[1], visited)))
    return L == 0

found = solve(board, dictionary)
L = list(found.keys())
if len(L) == 0:
    print(-1)
else:
    print(" ".join(sorted(L)))
