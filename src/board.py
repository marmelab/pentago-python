def construct_board():
    board = []
    for x in range(6):
        board.append([])
        for y in range(6):
            # 0 if empty, 1 if filled (and maybe later 2 for player 2 ?)
            board[x].append(0)
    return board

def print_board(board):
    print("\n      A  B  C  D  E  F")
    print("   ┌───────────────────┐")
    for x, line in enumerate(board, 0):
        line_values = ""
        for y in enumerate(line, 0):
            line_values = line_values + " ◯ "
        print(" " + str(x + 1) + " | " + line_values + "|")
    print("   └───────────────────┘\n")