def construct_board():
    return [[0] * 6] * 6

def print_board(board):
    print("\n      A  B  C  D  E  F")
    print("   ┌───────────────────┐")
    for x, line in enumerate(board, 0):
        line_values = ""
        for y in enumerate(line, 0):
            line_values = line_values + " ◯ "
        print(" " + str(x + 1) + " | " + line_values + "|")
    print("   └───────────────────┘\n")