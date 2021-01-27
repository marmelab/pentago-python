import unittest
from unittest_data_provider import data_provider

from player import Player


class PlayerTest (unittest.TestCase):
    def test_if_Player_constructor_return_correctly_initialized_player(self):
        player = Player(5, "Dustin")
        self.assertEqual(player.id, 5)
        self.assertEqual(player.name, "Dustin")


if __name__ == '__main__':
    unittest.main()
