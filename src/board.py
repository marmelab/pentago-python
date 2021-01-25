import string

def construct_board():
    return [[0]*6 for _ in range(6)]

def is_board_full(board):
    for x, line in enumerate(board, 0):
        for y, value in enumerate(line, 0):
            if value == 0:
                return False
    return True

def get_position_if_valid(board, position):  
    try:
        if len(position) != 2:
            return None

        x = int(position[1]) - 1

        # See https://stackoverflow.com/questions/5927149/get-character-position-in-alphabet
        y = ord(position[0].lower()) - 97

        r = range(0, 6)

        # If position is outside boundaries or on an already filled position.
        if  x not in r or y not in r or board[x][y] != 0:
            return None

        # Return 2 dim array relative position (e.g [0, 0])
        return [x, y]
    except:
        return None

def add_marble_to_board(board, position):
    board[position[0]][position[1]] = 1
    return board

def get_marble_character(value):
    return "◯" if value == 0 else "◉" 

def print_board(board):
    print("\n      A  B  C  D  E  F")
    print("   ┌───────────────────┐")
    for x, line in enumerate(board, 0):
        line_values = ""
        for y, value in enumerate(line, 0):
            line_values = line_values + " " + get_marble_character(value) + " "
        print(" " + str(x + 1) + " | " + line_values + "|")
    print("   └───────────────────┘\n")
