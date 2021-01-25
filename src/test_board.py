import unittest
from board import construct_board, print_board

class BoardTest (unittest.TestCase):
    def test_if_construct_board_return_correctly_initialized_array(self):
        board = construct_board()

        expected_board  = [[0] * 6] * 6
        print_board(board)
        self.assertListEqual(board, expected_board)
    

if __name__ == '__main__':
   unittest.main()