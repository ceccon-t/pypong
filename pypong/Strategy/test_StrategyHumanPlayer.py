from Strategy.Strategy import PLAYER_ONE, PLAYER_TWO
from Strategy.GameState import GameState

from Strategy.StrategyHumanPlayer import StrategyHumanPlayer

def test_player_one_move_up():
    acceleration_factor = -1

    state = GameState()
    state.player_one_acceleration_factor = acceleration_factor

    strategy = StrategyHumanPlayer(PLAYER_ONE)

    result = strategy.decide_acceleration_factor(state)

    assert result == acceleration_factor


def test_player_one_move_down():
    acceleration_factor = 1

    state = GameState()
    state.player_one_acceleration_factor = acceleration_factor

    strategy = StrategyHumanPlayer(PLAYER_ONE)

    result = strategy.decide_acceleration_factor(state)

    assert result == acceleration_factor


def test_player_two_move_up():
    acceleration_factor = -1

    state = GameState()
    state.player_two_acceleration_factor = acceleration_factor

    strategy = StrategyHumanPlayer(PLAYER_TWO)

    result = strategy.decide_acceleration_factor(state)

    assert result == acceleration_factor


def test_player_two_move_down():
    acceleration_factor = 1

    state = GameState()
    state.player_two_acceleration_factor = acceleration_factor

    strategy = StrategyHumanPlayer(PLAYER_TWO)

    result = strategy.decide_acceleration_factor(state)

    assert result == acceleration_factor
