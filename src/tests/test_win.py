import unittest
from unittest_data_provider import data_provider
import sys
import numpy as np

from tests.test_utils.print_board import print_board_if_verbosity_is_set
import tests.test_win_datasets as datasets

from win import *

class WinTest (unittest.TestCase):

    @data_provider(datasets.is_position_outside_board)
    def test_is_position_outside_board(self, position, expected_is_outside):
        is_outside = is_position_outside_board(position)
        self.assertEqual(is_outside, expected_is_outside)


    @data_provider(datasets.browse_board_in_direction_to_get_aligmnent)
    def test_browse_board_in_direction_to_get_aligmnent(self, board, start_positions, direction, expected_result):
        print_board_if_verbosity_is_set(board)

        result = browse_board_in_direction_to_get_aligmnent(
            board,
            start_positions,
            direction
        )

        if expected_result == None:
            self.assertIsNone(result)
        else:
            self.assertDictEqual(result, expected_result)


    @data_provider(datasets.loop_over_all_possibilities_of_aligment_in_direction)
    def test_loop_over_all_possibilities_of_aligment_in_direction(self, board, range_row, range_col, direction, expected_results):
        print_board_if_verbosity_is_set(board)
    
        results = loop_over_all_possibilities_of_aligment_in_direction(board, range_row, range_col, direction)

        self.assertListEqual(results, expected_results)

    @data_provider(datasets.get_all_lines_aligned)
    def test_get_all_lines_aligned(self, board, expected_results):
        print_board_if_verbosity_is_set(board)

        results=get_all_lines_aligned(board)
        
        self.assertListEqual(results, expected_results)

    @data_provider(datasets.get_all_columns_aligned)
    def test_get_all_columns_aligned(self, board, expected_results):
        print_board_if_verbosity_is_set(board)

        results=get_all_columns_aligned(board)
        
        self.assertListEqual(results, expected_results)

    @data_provider(datasets.get_all_diagonales_aligned)
    def test_get_all_diagonales_aligned(self, board, expected_results):
        print_board_if_verbosity_is_set(board)

        results=get_all_diagonales_aligned(board)
        
        self.assertListEqual(results, expected_results)

    @data_provider(datasets.get_all_reversed_diagonales_aligned)
    def test_get_all_reversed_diagonales_aligned(self, board, expected_results):
        print_board_if_verbosity_is_set(board)

        results=get_all_reversed_diagonales_aligned(board)
        
        self.assertListEqual(results, expected_results)


    @data_provider(datasets.if_position_is_in_correct_combinations)
    def test_if_position_is_in_correct_combinations(self, position, expected_results):
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
        self.assertEqual(result, expected_results)


    @data_provider(datasets.get_winners_player_id_from_correct_combinations)
    def test_get_winners_player_id_from_correct_combinations(self, correct_combinations, expected_results):
        winners = get_winners_player_id_from_correct_combinations(correct_combinations)
        self.assertListEqual(winners, expected_results)

