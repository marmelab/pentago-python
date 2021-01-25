import unittest
from board import construct_board

class BoardTest (unittest.TestCase):
    def test_if_construct_board_return_correctly_sized_array(self):
        board = construct_board()
        self.assertEqual(len(board), 6)

        for x, line in enumerate(board, 0):
            self.assertEqual(len(line), 6)
    
    def test_if_construct_board_init_all_array_values_to_0(self):
        board = construct_board()

        for x, line in enumerate(board, 0):
            for y, value in enumerate(line, 0):
                self.assertEqual(value, 0)

if __name__ == '__main__':
   unittest.main()