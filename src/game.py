from board import construct_board

from player import Player

class Game:
    def __init__(self, name1, name2, current_player_id):
        self.board = construct_board()
        self.players = construct_players(name1, name2)
        self.current_player_id = current_player_id
        self.one_quarter_is_symetric = True

def construct_players(name1, name2):
    return (
        Player(1, name1),
        Player(2, name2),
    )

# Return the other player id.
def player_finished_his_turn(current_player_id):
    return 2 if current_player_id == 1 else 1


