import unittest
from unittest_data_provider import data_provider

from player import construct_players


class PlayerTest (unittest.TestCase):
    def test_if_construct_board_return_correctly_initialized_players(self):
        players = construct_players()

        expected_players = (
            {"id": 1, "name": "Player 1"},
            {"id": 2, "name": "Player 2"}
        )

        self.assertSequenceEqual(players, expected_players)


if __name__ == '__main__':
    unittest.main()
