from board import construct_board
from player import construct_players

def construct_game():
    return {
        "board": construct_board(),
        "players": construct_players(),
        "current_player_id": 1
    }


# Return the other player id.
def player_finished_his_turn(current_player_id):
    return 2 if current_player_id == 1 else 1

