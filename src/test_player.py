import unittest
from unittest_data_provider import data_provider

from player import Player, construct_players


class PlayerTest (unittest.TestCase):
    def test_if_Player_constructor_return_correctly_initialized_player(self):
        player = Player(5, "Dustin")
        self.assertEqual(player.id, 5)
        self.assertEqual(player.name, "Dustin")

    def test_if_construct_players_return_correctly_initialized_players(self):
        players = construct_players()

        self.assertIsInstance(players[0], Player)
        self.assertEqual(players[0].id, 1)
        self.assertEqual(players[0].name, "Player 1")

        self.assertIsInstance(players[1], Player)
        self.assertEqual(players[1].id, 2)
        self.assertEqual(players[1].name, "Player 2")

if __name__ == '__main__':
    unittest.main()
