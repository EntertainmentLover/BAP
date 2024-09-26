from itertools import product

def knight_moves(position):
    x, y = position
    moves = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2, x+2], [y-1, y+1]))
    moves = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
    return moves

position = (4, 4)
moves = knight_moves(position)

print("Допустимые ходы коня", position, moves)
