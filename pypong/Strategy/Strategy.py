PLAYER_ONE = 1
PLAYER_TWO = 2

class Strategy:

    def __init__(self, player_number):
        self.player_number = player_number

    def decide_acceleration_factor(self, game_state):
        raise Exception("Class must implement 'decide_acceleration_factor' method.")
