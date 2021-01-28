import unittest
from unittest_data_provider import data_provider
import numpy as np

from game import Game, player_finished_his_turn, construct_players
from player import Player

class GameTest (unittest.TestCase):
    def test_if_game_instance_return_correctly_initialized_game(self):
        game = Game("Dustin", "Brice", 2)

        expected_board = np.array([[0] * 6 for _ in range(6)], int)
        expected_current_player_id = 2


        np.testing.assert_array_equal(game.board, expected_board)
        self.assertIsInstance(game.players[0], Player)
        self.assertIsInstance(game.players[1], Player)
        self.assertEqual(game.current_player_id, expected_current_player_id)
        self.assertEqual(game.one_quarter_is_symetric, True)


    turn_values = lambda: (
        (1, 2),
        (2, 1),
        (0, 1),
    )
    @data_provider(turn_values)
    def test_if_player_finished_his_turn_switch_correctly_between_players(self, current_player_id, expected_result):
        result = player_finished_his_turn(current_player_id)

        self.assertEqual(result, expected_result)


    def test_if_construct_players_return_correctly_initialized_players(self):
        players = construct_players("Dustin", "Brice")

        self.assertIsInstance(players[0], Player)
        self.assertEqual(players[0].id, 1)
        self.assertEqual(players[0].name, "Dustin")

        self.assertIsInstance(players[1], Player)
        self.assertEqual(players[1].id, 2)
        self.assertEqual(players[1].name, "Brice")



if __name__ == '__main__':
    unittest.main()
