import sys
import numpy as np
import unittest

from unittest_data_provider import data_provider

from render import print_board


def print_board_if_verbosity_is_set(board):
    if "-v" in sys.argv:
        print_board(board, False)


def generate_empty_board():
    return np.array([[0] * 6 for _ in range(6)], int)


def generate_full_board():
    return np.array([[1] * 6 for _ in range(6)], int)


def generate_board_and_add_position(position, value = 1):
    board = generate_empty_board()
    board[position] = value
    return board


def generate_board_and_add_positions(positions, value = 1):
    board = generate_empty_board()
    for position in positions:
        board[position] = value
    return board


class UtilsTest (unittest.TestCase):
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
