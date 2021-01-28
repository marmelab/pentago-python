import unittest
from unittest_data_provider import data_provider
import sys
import numpy as np

from board import *

from test_utils.generate_board import generate_board_and_add_position, generate_empty_board, generate_full_board, generate_board_and_add_positions
from test_utils.print_board import print_board_if_verbosity_is_set

class BoardTest (unittest.TestCase):
    def test_if_construct_board_return_correctly_initialized_array(self):
        board = construct_board()
        print_board_if_verbosity_is_set(board)

        expected_board  = np.array([[0] * 6] * 6)
        
        np.testing.assert_array_equal(board, expected_board)
    
    def test_is_board_not_full_should_return_false(self):
        board = [[1]*6 for _ in range(6)]
        board[0][0] = 0
        print_board_if_verbosity_is_set(board)

        result = is_board_full(board)
        
        self.assertFalse(result)
    
    def test_is_board_full_should_return_true(self):
        board = [[1]*6 for _ in range(6)]
        print_board_if_verbosity_is_set(board)

        result = is_board_full(board)
        
        self.assertTrue(result)


    positions_values = lambda: (
        ( "A1", (0, 0)),
        ( "a1", (0, 0)),
        ( "C4", (3, 2)),
        ( "F6", (5, 5)),
        ( "A0", None),
        ( "A7", None),
        ( "G1", None),
        ( "anything", None)
    )
   
    @data_provider(positions_values)
    def test_get_position_if_valid(self, position, expected_result):
        board = generate_empty_board()
        print_board_if_verbosity_is_set(board)
        
        result = get_position_if_valid(board, position)
    
        self.assertEqual(result, expected_result)

    def test_get_position_if_valid_should_return_None_due_to_cell_already_filled(self):
        board = [[0]*6 for _ in range(6)]
        board[0][0] = 1
        print_board_if_verbosity_is_set(board)
        
        result = get_position_if_valid(board, "A1")
        expected_result = None

        self.assertEqual(result, expected_result)


    good_positions_values = lambda: (
        ( "A1", generate_board_and_add_position((0, 0), 1), 1),
        ( "A1", generate_board_and_add_position((0, 0), 2), 2),
        ( "a1", generate_board_and_add_position((0, 0), 1), 1),
        ( "C4", generate_board_and_add_position((3, 2), 1), 1),
        ( "F6", generate_board_and_add_position((5, 5), 1), 1)
    )
    @data_provider(good_positions_values)
    def test_add_marble_to_board_return_board(self, position, expected_board, current_player_id):

        board = generate_empty_board()
        

        board = add_marble_to_board(board, current_player_id, position)
        print_board_if_verbosity_is_set(board)

        np.testing.assert_array_equal(board, expected_board)

    bad_positions_values = lambda: (
        ( "A0", generate_empty_board()),
        ( "A7", generate_empty_board()),
        ( "G1", generate_empty_board()),
        ( "anything", generate_empty_board()),
        ( "A1", generate_full_board())
    )
    @data_provider(bad_positions_values)
    def test_add_marble_to_board_raise_exception(self, position, board):

        print_board_if_verbosity_is_set(board)
        
        with self.assertRaises(ValueError) as context:
            board = add_marble_to_board(board, 1, position)


        self.assertEqual("Position given is not correct", str(context.exception))

    rotation_keys = lambda: (
        (0, (slice(0, 3), slice(0, 3))),
        (1, (slice(0, 3), slice(0, 3))),
        (2, (slice(0, 3), slice(3, 6))),
        (3, (slice(0, 3), slice(3, 6))),
        (4, (slice(3, 6), slice(3, 6))),
        (5, (slice(3, 6), slice(3, 6))),
        (6, (slice(3, 6), slice(0, 3))),
        (7, (slice(3, 6), slice(0, 3))),
    )

    @data_provider(rotation_keys)
    def test_get_quarter_boundaries_from_rotation_key(self, rotation_key, expected_boundaries):
        result_boundaries = get_quarter_boundaries_from_rotation_key(rotation_key)
        
        self.assertTupleEqual(expected_boundaries, result_boundaries)

    
    good_rotation_values = lambda: (
        ( "", generate_board_and_add_position((0, 0)), True, generate_board_and_add_position((0, 0)) ),
        ( "1", generate_board_and_add_position((0, 0)), False, generate_board_and_add_position((2, 0)) ),
        ( "1", generate_board_and_add_position((0, 0)), True, generate_board_and_add_position((2, 0)) ),
        ( "2", generate_board_and_add_position((0, 0)), False, generate_board_and_add_position((0, 2)) ),
        ( "3", generate_board_and_add_position((0, 3)), False, generate_board_and_add_position((2, 3)) ),
        ( "4", generate_board_and_add_position((0, 3)), False, generate_board_and_add_position((0, 5)) ),
        ( "5", generate_board_and_add_position((3, 3)), False, generate_board_and_add_position((5, 3)) ),
        ( "6", generate_board_and_add_position((3, 3)), False, generate_board_and_add_position((3, 5)) ),
        ( "7", generate_board_and_add_position((3, 0)), False, generate_board_and_add_position((5, 0)) ),
        ( "8", generate_board_and_add_position((3, 0)), False, generate_board_and_add_position((3, 2)) ),
    )

    @data_provider(good_rotation_values)
    def test_rotate_quarter_of_board_should_return_board(self, player_input_value, board, one_quarter_is_symetric, expected_board):
        print_board_if_verbosity_is_set(board)
        print_board_if_verbosity_is_set(expected_board)
        result = rotate_quarter_of_board(board, player_input_value, one_quarter_is_symetric)

        np.testing.assert_array_equal(result, expected_board)


    bad_rotation_values = lambda: (
        ( "0", generate_empty_board()),
        ( "A1", generate_empty_board()),
        ( "something", generate_empty_board()),
        ( "9", generate_empty_board()),
    )
    @data_provider(bad_rotation_values)
    def test_rotate_quarter_of_board_raise_exception(self, player_input_value, board):

        print_board_if_verbosity_is_set(board)
        
        with self.assertRaises(ValueError) as context:
            board = rotate_quarter_of_board(board, player_input_value, False)


        self.assertEqual("Rotation given is not correct", str(context.exception))

    is_quarter_symetric_values = lambda: (
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], True),
        ([[0, 1, 0], [0, 0, 0], [0, 0, 0]], False),
        ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], True),
        ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], True),
        ([[1, 2, 1], [2, 0, 2], [1, 2, 1]], True),
    )
    @data_provider(is_quarter_symetric_values)
    def test_is_quarter_symetric(self, quarter, expected_result):
        print_board_if_verbosity_is_set(quarter)

        result = is_quarter_symetric(quarter)

        self.assertEqual(result, expected_result)

    is_at_least_one_quarter_symetric_values = lambda: (
        (generate_board_and_add_positions(((0, 0), (3, 0), (3, 3), (0, 3))), False),
        (generate_empty_board(), True),
    )
    @data_provider(is_at_least_one_quarter_symetric_values)
    def test_is_at_least_one_quarter_symetric(self, board, expected_result):
        print_board_if_verbosity_is_set(board)

        result = is_at_least_one_quarter_symetric(board)

        self.assertEqual(result, expected_result)
