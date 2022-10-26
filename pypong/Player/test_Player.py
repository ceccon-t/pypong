from Player.Player import Player

def _build_default_player():
    return Player()


def test_initial_score():
    player = _build_default_player()
    assert player.score() == 0


def test_increment_score():
    player = _build_default_player()

    initial_score = player.score()

    player.increment_score()
    assert player.score() == initial_score + 1


def test_reset_score():
    player = _build_default_player()

    player.increment_score()

    assert player.score() != 0

    player.reset_score()

    assert player.score() == 0
    