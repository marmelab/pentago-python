from board import construct_board

from player import Player

class Game:
    def __init__(self):
        self.board = construct_board()

        self.players = construct_players()
        self.current_player_id = 1

def construct_players():
    return (
        Player(1, "Player 1"),
        Player(2, "Player 2"),
    )

# Return the other player id.
def player_finished_his_turn(current_player_id):
    return 2 if current_player_id == 1 else 1


