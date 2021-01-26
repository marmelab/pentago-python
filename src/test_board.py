import unittest
from unittest_data_provider import data_provider
import sys
import numpy as np

from board import construct_board, is_board_full, get_position_if_valid, add_marble_to_board

from test_utils import print_board_if_verbosity_is_set, generate_board_and_add_position, generate_empty_board, generate_full_board

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
        ( "A1", generate_board_and_add_position((0, 0))),
        ( "a1", generate_board_and_add_position((0, 0))),
        ( "C4", generate_board_and_add_position((3, 2))),
        ( "F6", generate_board_and_add_position((5, 5)))
    )
    @data_provider(good_positions_values)
    def test_add_marble_to_board_return_board(self, position, expected_board):

        board = generate_empty_board()
        

        board = add_marble_to_board(board, position)
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
            board = add_marble_to_board(board, position)


        self.assertTrue("Position given is not correct" in str(context.exception))

