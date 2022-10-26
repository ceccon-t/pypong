from turtle import position
from Player.Paddle import Paddle, HALF_PAD_HEIGHT

DEFAULT_POSITION = 100
DEFAULT_LIMIT_TOP = 0
DEFAULT_LIMIT_BOTTOM = 400

def _build_default_paddle():
    return Paddle(DEFAULT_POSITION, DEFAULT_LIMIT_TOP, DEFAULT_LIMIT_BOTTOM)


def test_get_position():
    paddle = _build_default_paddle()
    assert paddle.pos() == DEFAULT_POSITION


def test_get_velocity():
    paddle = _build_default_paddle()

    initial_velocity = 0

    assert paddle.vel() == initial_velocity


def test_set_velocity():
    paddle = _build_default_paddle()

    new_velocity = -3

    paddle.set_vel(new_velocity)

    assert paddle.vel() == new_velocity


def test_update():
    paddle = _build_default_paddle()
    step = 4

    paddle.set_vel(step)

    paddle.update()

    assert paddle.pos() == DEFAULT_POSITION + step


def test_update_respects_limits():
    step = 1
    limit_top = DEFAULT_POSITION - (HALF_PAD_HEIGHT + step)
    limit_bottom = DEFAULT_POSITION + (HALF_PAD_HEIGHT + step)
    paddle = Paddle(DEFAULT_POSITION, limit_top, limit_bottom)

    paddle.set_vel(-step)

    assert paddle.pos() == DEFAULT_POSITION

    paddle.update()
    assert paddle.pos() == DEFAULT_POSITION - step # can move when respecting top limit

    paddle.update()
    assert paddle.pos() == DEFAULT_POSITION - step # expect no change, i.e. truncates at top

    paddle.set_vel(step)

    paddle.update() # back to original position
    paddle.update()
    assert paddle.pos() == DEFAULT_POSITION + step # can move when respecting bottom limit

    paddle.update()
    assert paddle.pos() == DEFAULT_POSITION + step # expect no change, i.e. truncates at bottom


def test_hits():
    paddle = _build_default_paddle()

    point_above = DEFAULT_POSITION - HALF_PAD_HEIGHT - 1
    point_right_at_top = DEFAULT_POSITION - HALF_PAD_HEIGHT
    point_within = DEFAULT_POSITION + 1
    point_right_at_bottom = DEFAULT_POSITION + HALF_PAD_HEIGHT
    point_below = DEFAULT_POSITION + HALF_PAD_HEIGHT + 1

    assert paddle.hits(point_above) == False
    assert paddle.hits(point_right_at_top) == True
    assert paddle.hits(point_within) == True
    assert paddle.hits(point_right_at_bottom) == True
    assert paddle.hits(point_below) == False




