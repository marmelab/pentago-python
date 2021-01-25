import unittest
from board import construct_board, print_board, is_board_full, get_position_if_valid, add_marble_to_board

class BoardTest (unittest.TestCase):
    def test_if_construct_board_return_correctly_initialized_array(self):
        board = construct_board()
        print_board(board)

        expected_board  = [[0] * 6] * 6
        
        self.assertListEqual(board, expected_board)
    
    def test_is_board_not_full_should_return_false(self):
        board = [[1]*6 for _ in range(6)]
        board[0][0] = 0
        print_board(board)

        result = is_board_full(board)
        
        self.assertFalse(result)
    
    def test_is_board_full_should_return_true(self):
        board = [[1]*6 for _ in range(6)]
        print_board(board)

        result = is_board_full(board)
        
        self.assertTrue(result)
    
    def test_get_position_if_valid_should_return_array_position(self):
        board = [[0]*6 for _ in range(6)]
        print_board(board)
        
        result = get_position_if_valid(board, "A1")
        expected_result = [0,0]

        self.assertEqual(result, expected_result)

        result = get_position_if_valid(board, "F6")
        expected_result = [5,5]
        self.assertEqual(result, expected_result)

    def test_get_position_if_valid_should_return_None_due_to_boundaries(self):
        board = [[0]*6 for _ in range(6)]
        print_board(board)
        
        result = get_position_if_valid(board, "A0")
        expected_result = None

        self.assertEqual(result, expected_result)

        result = get_position_if_valid(board, "A7")
        expected_result = None

        self.assertEqual(result, expected_result)


        result = get_position_if_valid(board, "G1")
        expected_result = None

        self.assertEqual(result, expected_result)
    
    def test_get_position_if_valid_should_return_None_due_to_position_length(self):
        board = [[0]*6 for _ in range(6)]
        print_board(board)
        
        result = get_position_if_valid(board, "anything")
        expected_result = None

        self.assertEqual(result, expected_result)

    def test_get_position_if_valid_should_return_None_due_to_cell_already_filled(self):
        board = [[0]*6 for _ in range(6)]
        board[0][0] = 1
        print_board(board)
        
        result = get_position_if_valid(board, "A1")
        expected_result = None

        self.assertEqual(result, expected_result)


    def test_get_position_if_valid_should_return_relative_board_position(self):
        board = [[0]*6 for _ in range(6)]
        print_board(board)
        
        result = get_position_if_valid(board, "A1")
        expected_result = [0, 0]

        self.assertEqual(result, expected_result)

        result = get_position_if_valid(board, "F6")
        expected_result = [5, 5]

        self.assertEqual(result, expected_result)

    def test_add_marble_to_board(self):

        board = [[0]*6 for _ in range(6)]
        
        expected_board = [[0]*6 for _ in range(6)]
        
        expected_board[0][0] = 1

        board = add_marble_to_board(board, [0, 0])
        print_board(board)
        
        
        self.assertListEqual(board, expected_board)



if __name__ == '__main__':
   unittest.main()
