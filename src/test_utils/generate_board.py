import sys
import numpy as np
import unittest

from unittest_data_provider import data_provider


# Generate 6*6 board with 0 in all values
def generate_empty_board():
    return np.array([[0] * 6 for _ in range(6)], int)

# Generate 6*6 board with 1 in all values
def generate_full_board():
    return np.array([[1] * 6 for _ in range(6)], int)

# Generate empty board and value to a position
def generate_board_and_add_position(position, value = 1):
    board = generate_empty_board()
    board[position] = value
    return board

# Generate empty and set multiple positions to value.
def generate_board_and_add_positions(positions, value = 1):
    board = generate_empty_board()
    for position in positions:
        board[position] = value
    return board
