import unittest
from unittest_data_provider import data_provider
import numpy as np

from game import construct_game, player_finished_his_turn


class GameTest (unittest.TestCase):
    def test_if_construct_game_return_correctly_initialized_game(self):
        game = construct_game()
        expected_game = {
            "board": np.array([[0] * 6 for _ in range(6)], int),
            "players": (
                {"id": 1, "name": "Player 1"},
                {"id": 2, "name": "Player 2"}
            ),
            "current_player_id": 1
        }

    turn_values = lambda: (
        (1, 2),
        (2, 1),
        (0, 1),
    )
    @data_provider(turn_values)
    def test_if_player_finished_his_turn_switch_correctly_between_players(self, current_player_id, expected_result):
        result = player_finished_his_turn(current_player_id)

        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()
