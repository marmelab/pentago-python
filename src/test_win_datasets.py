from test_utils.generate_board import generate_board_and_add_positions, generate_empty_board, generate_full_board

is_position_outside_board = lambda: (
    ((-1, 0), True),
    ((0, -1), True),
    ((0, 0), False),
    ((5, 5), False),
    ((5, 6), True),
    ((6, 5), True),
)

browse_board_in_direction_to_get_aligmnent = lambda: (
    (
        # Start position is not a player value
        generate_board_and_add_positions(
            ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5))
        ),
        (0, 0),
        (1, 0),
        None
    ),
    (
        generate_board_and_add_positions(
            ((1, 5), (2, 5), (4, 5), (5, 5))
        ),  # Got a 0 value in the middle
        (1, 5),
        (1, 0),
        None
    ),
    (
        # Start position is outside the board
        generate_board_and_add_positions(
            ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5))
        ),
        (6, 6),
        (1, 0),
        None
    ),
    (
        # Direction browse the board outside boundaries
        generate_board_and_add_positions(
            ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5))
        ),
        (1, 5),
        (-1, 0),
        None
    ),
    (
        generate_board_and_add_positions(
            ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5)),
            2
        ),  # In Column
        (1, 5),
        (1, 0),
        {
            "player_id": 2,
            "aligned_positions": [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]
        }
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4))
        ),  # In Line
        (0, 0),
        (0, 1),
        {
            "player_id": 1,
            "aligned_positions": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        }
    ),
    (
        generate_board_and_add_positions(
            ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5))
        ),  # In diagonale
        (0, 1),
        (1, 1),
        {
            "player_id": 1,
            "aligned_positions": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
        }
    ),
    (
        generate_board_and_add_positions(
            ((1, 4), (2, 3), (3, 2), (4, 1), (5, 0)),
            2
        ),  # In reversed diagonale
        (1, 4),
        (1, -1),
        {
            "player_id": 2,
            "aligned_positions": [(1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]
        }
    ),
)

loop_over_all_possibilities_of_aligment_in_direction = lambda: (
    (
        generate_board_and_add_positions(
            ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5)),
            2
        ),
        range(0, 1),  # Will not check the second line
        range(2),
        (0, 1),
        []
    ),
    (
        generate_board_and_add_positions(
            ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5)),
            2
        ),
        range(6),
        range(0, 1),  # Will not check every columns
        (1, 0),
        []
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)),
            2
        ),  # In Line
        range(6),
        range(2),
        (0, 1),
        [{
            "player_id": 2,
            "aligned_positions": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        }]
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0))
        ),  # In Column
        range(3, 4), # Will not check good rows
        range(6),
        (1, 0),
        []
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0))
        ),  # In Column
        range(2),
        range(6),
        (1, 0),
        [{
            "player_id": 1,
            "aligned_positions": [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        }]
    ),
    (
        generate_board_and_add_positions(
            ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5))
        ),  # In diagonale
        range(2),
        range(4, 6), # Will not check good columns
        (1, 1),
        []
    ),
    (
        generate_board_and_add_positions(
            ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5))
        ),  # In diagonale
        range(2),
        range(2),
        (1, 1),
        [{
            "player_id": 1,
            "aligned_positions": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
        }]
    ),
    (
        generate_board_and_add_positions(
            ((1, 4), (2, 3), (3, 2), (4, 1), (5, 0)),
            2
        ),  # In reversed diagonale
        range(4, 6), # Will not brose the good start line
        range(4, 6),
        (1, -1),
        []
    ),
    (
        generate_board_and_add_positions(
            ((1, 4), (2, 3), (3, 2), (4, 1), (5, 0)),
            2
        ),  # In reversed diagonale
        range(2),
        range(4, 6),
        (1, -1),
        [{
            "player_id": 2,
            "aligned_positions": [(1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]
        }]
    ),
)

get_all_lines_aligned = lambda: (
    (
        generate_board_and_add_positions(
            ((0, 0), (0, 2), (0, 3), (0, 4)),
            2
        ),
        []
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)),
            2
        ),
        [{
            "player_id": 2,
            "aligned_positions": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        }]
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)),
            2
        ),
        [
            {
                "player_id": 2,
                "aligned_positions": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
            },
            {
                "player_id": 2,
                "aligned_positions": [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]
            }
        ]
    ),
)

get_all_columns_aligned = lambda: (
    (
        generate_board_and_add_positions(
            ((0, 0), (1, 0), (2, 0), (3, 0)),
            2
        ),
        []
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0))
        ),
        [{
            "player_id": 1,
            "aligned_positions": [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        }]
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)),
            2
        ),
        [
            {
                "player_id": 2,
                "aligned_positions": [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
            },
            {
                "player_id": 2,
                "aligned_positions": [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]
            }
        ]
    ),
)

get_all_diagonales_aligned = lambda: (
    (
        generate_board_and_add_positions(
            ((0, 0), (1, 1), (2, 2), (4, 4)),
            2
        ),
        []
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4))
        ),
        [{
            "player_id": 1,
            "aligned_positions": [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        }]
    ),
    (
        generate_board_and_add_positions(
            ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)),
            2
        ),
        [
            {
                "player_id": 2,
                "aligned_positions": [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
            },
            {
                "player_id": 2,
                "aligned_positions": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
            }
        ]
    ),
)

get_all_reversed_diagonales_aligned = lambda: (
    (
        generate_board_and_add_positions(
            ((0, 4), (1, 3), (2, 2), (4, 0)),
            2
        ),
        []
    ),
    (
        generate_board_and_add_positions(
            ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0)),
            2
        ),
        [{
            "player_id": 2,
            "aligned_positions": [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
        }]
    ),
    (
        generate_board_and_add_positions(
            ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1)),
            2
        ),
        [
            {
                "player_id": 2,
                "aligned_positions": [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
            },
            {
                "player_id": 2,
                "aligned_positions": [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
            }
        ]
    ),
)

if_position_is_in_correct_combinations = lambda: (
    ((0, 0), False),
    ((1, 3), True),
    ((5, 1), True)
)
