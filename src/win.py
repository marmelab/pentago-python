from constant.board import BOARD_SIZE, WIN_CONDITION, WIN_AREA_CHECK

def is_position_outside_board(position):
    return position[0] < 0 or position[0] >= BOARD_SIZE or position[1] < 0 or position[1] >= BOARD_SIZE

def browse_board_in_direction_to_get_aligmnent(board, start_position, direction):
    """
        Check in the board if, by giving a start_position: (x, y) and a direction: (stepX , stepY)
        we can detect five marbles aligned.
    """

    if is_position_outside_board(start_position):
        return None

    # Get the value in the board for start_position
    player_id = board[start_position]

    # If the start_position is not a value played.
    if player_id == 0:
        return None

    result = {
        "player_id": player_id,
        "aligned_positions": [start_position]
    }


    # We have start_position, we need to get in the direction the 4 next values to detect if we have 5 marbles aligned.
    for i in range(1, WIN_CONDITION):

        current_position = (
            start_position[0] + (i * direction[0]),
            start_position[1] + (i * direction[1])
        )

        # Check if current_position is outside the board
        if is_position_outside_board(current_position):
            return None

        value = board[current_position]

        """
            e.g: player_id= 1
            if value = 0 or 2, it canno't be an alignment, so stop the detection now.
        """
        if value != player_id:
            return None

        # Instead, player_id and value are equal, save this position.
        result["aligned_positions"].append(current_position)


    return result


def loop_over_all_possibilities_of_aligment_in_direction(board, range_row, range_col, direction):
    results = []
    """
        Double loop between 2 ranges (range_row, range_col) and check for a particular direction if have an alignment.
    """
    for row in range_row:
        for col in range_col:
            start_position = (row, col)

            result = browse_board_in_direction_to_get_aligmnent(
                board,
                start_position,
                direction
            )
            if result != None:
                results.append(result)

    return results


def get_all_lines_aligned(board):

    """
        To check if we have a 5 marbles aligned in rows, we only have to iterate throught first two columns.
        ┌──────────+─────────┐
        |  x  x  ◯ | ◯  ◯  ◯ |
        |  x  x  ◯ | ◯  ◯  ◯ |
        |  x  x  ◯ | ◯  ◯  ◯ |
        |──────────+─────────|
        |  x  x  ◯ | ◯  ◯  ◯ |
        |  x  x  ◯ | ◯  ◯  ◯ |
        |  x  x  ◯ | ◯  ◯  ◯ |
        └──────────+─────────┘
    """

    range_row = range(BOARD_SIZE)
    range_col = range(WIN_AREA_CHECK)
    direction = (0, 1)
    return loop_over_all_possibilities_of_aligment_in_direction(
        board,
        range_row,
        range_col,
        direction
    )


def get_all_columns_aligned(board):
    """
        To check if we have a column with 5 marbles aligned, we only have to iterate throught first two lines:

        ┌──────────+─────────┐
        |  x  x  x | x  x  x |
        |  x  x  x | x  x  x |
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        |──────────+─────────|
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        └──────────+─────────┘

    """

    range_row = range(WIN_CONDITION)
    range_col = range(BOARD_SIZE)
    direction = (1, 0)

    return loop_over_all_possibilities_of_aligment_in_direction(
        board,
        range_row,
        range_col,
        direction
    )


def get_all_diagonales_aligned(board):
    """
        To check if we have a 5 marbles aligned in diagonales (from top-left to right-bottom), we only have to check following start positions.
        ┌──────────+─────────┐
        |  x  x  ◯ | ◯  ◯  ◯ |
        |  x  x  ◯ | ◯  ◯  ◯ |
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        |──────────+─────────|
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        └──────────+─────────┘
    """

    range_row = range(WIN_AREA_CHECK)
    range_col = range(WIN_AREA_CHECK)
    direction = (1, 1)

    return loop_over_all_possibilities_of_aligment_in_direction(
        board,
        range_row,
        range_col,
        direction
    )


def get_all_reversed_diagonales_aligned(board):
    """
        Finally, to check if we have a 5 marbles aligned in reversed diagonales (from top-right to left-bottom), we only have to check following start positions.
        ┌──────────+─────────┐
        |  ◯  ◯  ◯ | ◯  x  x |
        |  ◯  ◯  ◯ | ◯  x  x |
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        |──────────+─────────|
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        |  ◯  ◯  ◯ | ◯  ◯  ◯ |
        └──────────+─────────┘
    """

    range_row = range(WIN_AREA_CHECK)
    range_col = range(BOARD_SIZE - WIN_AREA_CHECK, BOARD_SIZE)
    direction = (1, -1)

    return loop_over_all_possibilities_of_aligment_in_direction(
        board,
        range_row,
        range_col,
        direction
    )

def get_all_marbles_combinations_correctly_aligned(board):
    """
        The board is a 6*6 board.

        To check if we have 5 marbles aligned, we only need to start checking from positions described below:
        ┌──────────+─────────┐
        |  x  x  x | x  x  x |
        |  x  x  x | x  x  x |
        |  x  x  ◯ | ◯  ◯  ◯ |
        |──────────+─────────|
        |  x  x  ◯ | ◯  ◯  ◯ |
        |  x  x  ◯ | ◯  ◯  ◯ |
        |  x  x  ◯ | ◯  ◯  ◯ |
        └──────────+─────────┘

        And browse the board to the right, to the bottom,
        to the right bottom (diagonale) and to the left bottom (reversed-diagonale)

    """

    results = get_all_lines_aligned(board)
    results += get_all_columns_aligned(board)
    results += get_all_diagonales_aligned(board)
    results += get_all_reversed_diagonales_aligned(board)

    return results

def if_position_is_in_correct_combinations(position, correct_combinations):

    for combination in correct_combinations:
        for aligned_position in combination["aligned_positions"]:
            if aligned_position == position:
                return True
    
    return False

def get_winners_player_id_from_correct_combinations(correct_combinations):
    winners = []

    for combination in correct_combinations:
        player_id = combination["player_id"]

        if player_id not in winners:
            winners.append(player_id)

    return winners
