from Ball.Ball import Ball

DEFAULT_POS_X = 5
DEFAULT_POS_Y = 17
DEFAULT_VEL_X = 3
DEFAULT_VEL_Y = 4
DEFAULT_RADIUS = 4

def _build_default_ball():
    return Ball(DEFAULT_POS_X, DEFAULT_POS_Y, DEFAULT_VEL_X, DEFAULT_VEL_Y, DEFAULT_RADIUS)

def test_get_position():
    pos_x = 5
    pos_y = 17
    ball = Ball(pos_x, pos_y, 0, 0, DEFAULT_RADIUS)
    assert ball.pos(0) == pos_x
    assert ball.pos(1) == pos_y


def test_get_velocity():
    vel_x = 5
    vel_y = 17
    ball = Ball(0, 0, vel_x, vel_y, DEFAULT_RADIUS)
    assert ball.vel(0) == vel_x
    assert ball.vel(1) == vel_y


def test_set_velocity():
    vel_x = 5
    vel_y = 17
    ball = Ball(0, 0, vel_x, vel_y, DEFAULT_RADIUS)

    new_vel_x = 3
    new_vel_y = 4
    ball.set_vel(0, new_vel_x)
    ball.set_vel(1, new_vel_y)

    assert ball.vel(0) == new_vel_x
    assert ball.vel(1) == new_vel_y


def test_scale_velocity():
    vel_x = 5
    vel_y = 17
    
    ball = Ball(0, 0, vel_x, vel_y, DEFAULT_RADIUS)

    scale_factor_x = -1.15
    scale_factor_y = 0.75

    ball.scale_vel(0, scale_factor_x)
    ball.scale_vel(1, scale_factor_y)

    expected_new_velocity_x = vel_x * scale_factor_x
    expected_new_velocity_y = vel_y * scale_factor_y

    assert ball.vel(0) == expected_new_velocity_x
    assert ball.vel(1) == expected_new_velocity_y

def test_update():
    pos_x = 5
    pos_y = 17
    vel_x = 3
    vel_y = 4
    expected_x = pos_x + vel_x
    expected_y = pos_y + vel_y 

    ball = Ball(pos_x, pos_y, vel_x, vel_y, DEFAULT_RADIUS)
    ball.update()

    assert ball.pos(0) == expected_x
    assert ball.pos(1) == expected_y+1

def test_leftmost():
    ball = _build_default_ball()
    assert ball.leftmost() == DEFAULT_POS_X - DEFAULT_RADIUS

def test_rightmost():
    ball = _build_default_ball()
    assert ball.rightmost() == DEFAULT_POS_X + DEFAULT_RADIUS

def test_topmost():
    ball = _build_default_ball()
    assert ball.topmost() == DEFAULT_POS_Y - DEFAULT_RADIUS

def test_bottommost():
    ball = _build_default_ball()
    assert ball.bottommost() == DEFAULT_POS_Y + DEFAULT_RADIUS

