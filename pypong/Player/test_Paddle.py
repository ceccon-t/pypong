from Player.Paddle import Paddle, HALF_PAD_HEIGHT, PADDLE_STEP

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


def test_accelerate():
    paddle = _build_default_paddle()

    acceleration = -1

    paddle.accelerate(acceleration)

    assert paddle.vel() == acceleration * PADDLE_STEP


def test_update():
    paddle = _build_default_paddle()
    acceleration = 1

    paddle.accelerate(acceleration)

    paddle.update()

    assert paddle.pos() == DEFAULT_POSITION + acceleration*PADDLE_STEP


def test_update_respects_limits():
    acceleration = 1
    limit_top = DEFAULT_POSITION - (HALF_PAD_HEIGHT + acceleration*PADDLE_STEP)
    limit_bottom = DEFAULT_POSITION + (HALF_PAD_HEIGHT + acceleration*PADDLE_STEP)
    paddle = Paddle(DEFAULT_POSITION, limit_top, limit_bottom)

    paddle.accelerate(-acceleration)

    assert paddle.pos() == DEFAULT_POSITION

    paddle.update()
    assert paddle.pos() == DEFAULT_POSITION - acceleration*PADDLE_STEP # can move when respecting top limit

    paddle.update()
    assert paddle.pos() == DEFAULT_POSITION - acceleration*PADDLE_STEP # expect no change, i.e. truncates at top

    paddle.accelerate(acceleration)

    paddle.update() # back to original position
    paddle.update()
    assert paddle.pos() == DEFAULT_POSITION + acceleration*PADDLE_STEP # can move when respecting bottom limit

    paddle.update()
    assert paddle.pos() == DEFAULT_POSITION + acceleration*PADDLE_STEP # expect no change, i.e. truncates at bottom


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


def test_topmost():
    paddle = _build_default_paddle()
    assert paddle.topmost() == DEFAULT_POSITION - HALF_PAD_HEIGHT

def test_bottommost():
    paddle = _build_default_paddle()
    assert paddle.bottommost() == DEFAULT_POSITION + HALF_PAD_HEIGHT




