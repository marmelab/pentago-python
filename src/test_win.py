import unittest
from unittest_data_provider import data_provider
import sys
import numpy as np

from test_utils.generate_board import generate_board_and_add_positions, generate_empty_board, generate_full_board
from test_utils.print_board import print_board_if_verbosity_is_set

from win import *


class WinTest (unittest.TestCase):
    positions = lambda: (
        ((-1, 0), True),
        ((0, -1), True),
        ((0, 0), False),
        ((5, 5), False),
        ((5, 6), True),
        ((6, 5), True),
    )

    @data_provider(positions)
    def test_is_position_outside_board(self, position, expected_is_outside):
        is_outside = is_position_outside_board(position)
        self.assertEqual(is_outside, expected_is_outside)

    positions = lambda: (
        (
            # Start position is not a player value
            generate_board_and_add_positions(
                ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5))),
            (0, 0),
            (1, 0),
            []
        ),
        (
            generate_board_and_add_positions(
                ((1, 5), (2, 5), (4, 5), (5, 5))),  # Got a 0 value in the middle
            (1, 5),
            (1, 0),
            []
        ),
        (
            # Start position is outside the board
            generate_board_and_add_positions(
                ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5))),
            (6, 6),
            (1, 0),
            []
        ),
        (
            # Direction browse the board outside boundaries
            generate_board_and_add_positions(
                ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5))),
            (1, 5),
            (-1, 0),
            []
        ),
        (
            generate_board_and_add_positions(
                ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5)), 2),  # In Column
            (1, 5),
            (1, 0),
            [{
                "player_id": 2,
                "aligned_positions": [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]
            }]
        ),
        (
            generate_board_and_add_positions(
                ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)), 1),  # In Line
            (0, 0),
            (0, 1),
            [{
                "player_id": 1,
                "aligned_positions": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
            }]
        ),
        (
            generate_board_and_add_positions(
                ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5)), 1),  # In diagonale
            (0, 1),
            (1, 1),
            [{
                "player_id": 1,
                "aligned_positions": [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
            }]
        ),
        (
            generate_board_and_add_positions(
                ((1, 4), (2, 3), (3, 2), (4, 1), (5, 0)), 2),  # In reversed diagonale
            (1, 4),
            (1, -1),
            [{
                "player_id": 2,
                "aligned_positions": [(1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]
            }]
        ),
    )

    @data_provider(positions)
    def test_browse_board_in_direction_to_get_aligmnent(self, board, start_positions, direction, expected_result):
        print_board_if_verbosity_is_set(board)
        results = []

        results = browse_board_in_direction_to_get_aligmnent(
            board, start_positions, direction, results)
        self.assertListEqual(results, expected_result)

    positions = lambda: (
        (
            generate_board_and_add_positions(
                ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5)), 2),
            range(0, 1),  # Will not check the second line
            range(2),
            (0, 1),
            []
        ),
        (
            generate_board_and_add_positions(
                ((1, 5), (2, 5), (3, 5), (4, 5), (5, 5)), 2),
            range(6),
            range(0, 1),  # Will not check every columns
            (1, 0),
            []
        ),
        (
            generate_board_and_add_positions(
                ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)), 2),  # In Line
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
                ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0)), 1),  # In Column
            range(3, 4), # Will not check good rows
            range(6),
            (1, 0),
            []
        ),
        (
            generate_board_and_add_positions(
                ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0)), 1),  # In Column
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
                ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5)), 1),  # In diagonale
            range(2),
            range(4, 6), # Will not check good columns
            (1, 1),
            []
        ),
        (
            generate_board_and_add_positions(
                ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5)), 1),  # In diagonale
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
                ((1, 4), (2, 3), (3, 2), (4, 1), (5, 0)), 2),  # In reversed diagonale
            range(4, 6), # Will not brose the good start line
            range(4, 6),
            (1, -1),
            []
        ),
        (
            generate_board_and_add_positions(
                ((1, 4), (2, 3), (3, 2), (4, 1), (5, 0)), 2),  # In reversed diagonale
            range(2),
            range(4, 6),
            (1, -1),
            [{
                "player_id": 2,
                "aligned_positions": [(1, 4), (2, 3), (3, 2), (4, 1), (5, 0)]
            }]
        ),
    )

    @data_provider(positions)
    def test_loop_over_all_possibilities_of_aligment_in_direction(self, board, range_row, range_col, direction, expected_result):
        print_board_if_verbosity_is_set(board)
        results = []
        results = loop_over_all_possibilities_of_aligment_in_direction(board, range_row, range_col, direction, results)
        self.assertListEqual(results, expected_result)

    positions = lambda: (
        (
            generate_board_and_add_positions(
                ((0, 0), (0, 2), (0, 3), (0, 4)), 2),
            []
        ),
        (
            generate_board_and_add_positions(
                ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)), 2),
            [{
                "player_id": 2,
                "aligned_positions": [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
            }]
        ),
        (
            generate_board_and_add_positions(
                ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)), 2),
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

    @data_provider(positions)
    def test_get_all_lines_aligned(self, board, expected_results):
        print_board_if_verbosity_is_set(board)
        
        results=[]

        results=get_all_lines_aligned(board, results)
        self.assertListEqual(results, expected_results)

    positions = lambda: (
        (
            generate_board_and_add_positions(
                ((0, 0), (1, 0), (2, 0), (3, 0)), 2),
            []
        ),
        (
            generate_board_and_add_positions(
                ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0))),
            [{
                "player_id": 1,
                "aligned_positions": [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
            }]
        ),
        (
            generate_board_and_add_positions(
                ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)), 2),
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

    @data_provider(positions)
    def test_get_all_columns_aligned(self, board, expected_results):
        print_board_if_verbosity_is_set(board)
        results=[]

        results=get_all_columns_aligned(board, results)
        self.assertListEqual(results, expected_results)

    positions = lambda: (
        (
            generate_board_and_add_positions(
                ((0, 0), (1, 1), (2, 2), (4, 4)), 2),
            []
        ),
        (
            generate_board_and_add_positions(
                ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4))),
            [{
                "player_id": 1,
                "aligned_positions": [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
            }]
        ),
        (
            generate_board_and_add_positions(
                ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (0, 1), (1, 2), (2, 3), (3, 4), (4, 5)), 2),
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

    @data_provider(positions)
    def test_get_all_diagonales_aligned(self, board, expected_results):
        print_board_if_verbosity_is_set(board)
        results=[]

        results=get_all_diagonales_aligned(board, results)
        self.assertListEqual(results, expected_results)

    positions = lambda: (
        (
            generate_board_and_add_positions(
                ((0, 4), (1, 3), (2, 2), (4, 0)), 2),
            []
        ),
        (
            generate_board_and_add_positions(
                ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0)), 2),
            [{
                "player_id": 2,
                "aligned_positions": [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
            }]
        ),
        (
            generate_board_and_add_positions(
                ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1)), 2),
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

    @data_provider(positions)
    def test_get_all_reversed_diagonales_aligned(self, board, expected_results):
        print_board_if_verbosity_is_set(board)
        results=[]

        results=get_all_reversed_diagonales_aligned(board, results)
        self.assertListEqual(results, expected_results)


    position_in_correct_combinations = lambda: (
        ((0, 0), False),
        ((1, 3), True),
        ((5, 1), True)
    )

    @data_provider(position_in_correct_combinations)
    def test_if_position_is_in_correct_combinations(self, position, expected_result):
        correct_combinations = [
                {
                    "player_id": 2,
                    "aligned_positions": [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
                },
                {
                    "player_id": 2,
                    "aligned_positions": [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
                }
        ]
        result = if_position_is_in_correct_combinations(position, correct_combinations)
        self.assertEqual(result, expected_result)
