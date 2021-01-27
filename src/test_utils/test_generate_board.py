import numpy as np
import unittest

from unittest_data_provider import data_provider

from test_utils.generate_board import generate_empty_board, generate_full_board, generate_board_and_add_position, generate_board_and_add_positions

class GenerateBoardTest (unittest.TestCase):
    def test_generate_empty_board(self):
        board = generate_empty_board()
        expected_board = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

        np.testing.assert_array_equal(board, expected_board)

    def test_generate_full_board(self):
        board = generate_full_board()
        expected_board = np.array([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [
                                  1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])

        np.testing.assert_array_equal(board, expected_board)

    def test_generate_board_and_add_position(self):
        board = generate_board_and_add_position((2, 3), 2)
        expected_board = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0], [
            0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])

        np.testing.assert_array_equal(board, expected_board)

    def test_generate_board_and_add_positions(self):
        board = generate_board_and_add_positions(((2, 3), (0, 1), (5, 5)), 2)
        expected_board = np.array([[0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 0, 0], [
            0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2]])

        np.testing.assert_array_equal(board, expected_board)
