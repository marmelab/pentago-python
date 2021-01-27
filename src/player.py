class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name

def construct_players():
    return (
        Player(1, "Player 1"),
        Player(2, "Player 2"),
    )
