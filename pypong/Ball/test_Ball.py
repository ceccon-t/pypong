from Ball.Ball import Ball

def test_get_position():
    pos_x = 5
    pos_y = 17
    ball = Ball(pos_x, pos_y, 0, 0)
    assert ball.pos(0) == pos_x
    assert ball.pos(1) == pos_y


def test_get_velocity():
    vel_x = 5
    vel_y = 17
    ball = Ball(0, 0, vel_x, vel_y)
    assert ball.vel(0) == vel_x
    assert ball.vel(1) == vel_y


def test_set_velocity():
    vel_x = 5
    vel_y = 17
    ball = Ball(0, 0, vel_x, vel_y)

    new_vel_x = 3
    new_vel_y = 4
    ball.set_vel(0, new_vel_x)
    ball.set_vel(1, new_vel_y)

    assert ball.vel(0) == new_vel_x
    assert ball.vel(1) == new_vel_y


def test_scale_velocity():
    vel_x = 5
    vel_y = 17
    
    ball = Ball(0, 0, vel_x, vel_y)

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

    ball = Ball(pos_x, pos_y, vel_x, vel_y)
    ball.update()

    assert ball.pos(0) == expected_x
    assert ball.pos(1) == expected_y

