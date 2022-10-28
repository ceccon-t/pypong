try:  # Python 3
    from Strategy.Strategy import Strategy, PLAYER_ONE, PLAYER_TWO
except ImportError:  # Python 2
    from Strategy import Strategy, PLAYER_ONE, PLAYER_TWO

class StrategyHumanPlayer(Strategy):
    
    def decide_acceleration_factor(self, game_state):
        player_choice = 0
        
        if self.player_number == PLAYER_ONE:
            player_choice = game_state.player_one_acceleration_factor
        if self.player_number == PLAYER_TWO:
            player_choice = game_state.player_two_acceleration_factor

        return player_choice
