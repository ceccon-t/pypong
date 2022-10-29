try:  # Python 3
    from tkinter import *  
except ImportError:
    try:  # Python 2
        from Tkinter import *  
    except ImportError:  # Tkinter not installed...
        raise ImportError("This program requires Tkinter, please make sure you have it installed.")

import random


from GameConstants import *
from Player.Paddle import PAD_WIDTH, HALF_PAD_WIDTH, PAD_HEIGHT, HALF_PAD_HEIGHT

from TkinterPypongScreen import TkinterPypongScreen

from Field.Field import Field

from Ball.Ball import Ball
from Player.Player import Player
from Player.Paddle import Paddle

from Strategy.GameState import GameState
from Strategy.Strategy import PLAYER_ONE, PLAYER_TWO

from Strategy.StrategyHumanPlayer import StrategyHumanPlayer
from Strategy.StrategySimpleComputerPlayer import StrategySimpleComputerPlayer


# Helper functions
def _new_base_paddle():
    return Paddle(PADDLE_INITIAL_POSITION, 0, HEIGHT)


# Function definitions
def pause(event):
    global running, screen
    running = not running
    if running:
        screen.set_instructions_message(INFO_STRING)
    else:
        screen.set_instructions_message(INFO_STRING_PAUSED)


def keydown(event):
    global game_state

    if event.char == "w":
        game_state.player_one_acceleration_factor = -1
    elif event.char == "s":
        game_state.player_one_acceleration_factor = 1
    elif event.char == "o":
        game_state.player_two_acceleration_factor = -1
    elif event.char == "l":
        game_state.player_two_acceleration_factor = 1


def update_ball():
    global ball, field, screen
    ball.update()
    # ball has reached top or bottom of the field, must reflect
    if field.hits_top(ball.topmost()) or field.hits_bottom(ball.bottommost()):
        ball.scale_vel(COORD_Y, -1) 
    screen.draw_ball(ball)


def update_paddles():
    global player_one, player_two, game_state, screen

    # Update player one paddle
    player_one.move(game_state)
    game_state.player_one_acceleration_factor = 0
    screen.draw_left_paddle(player_one.paddle())

    # Update player two paddle
    player_two.move(game_state)
    game_state.player_two_acceleration_factor = 0
    screen.draw_right_paddle(player_two.paddle())


def update_scores_display():
    global player_one, player_two, screen
    score1 = player_one.score()
    score2 = player_two.score()
    score1_color = COLOR_DRAW
    score2_color = COLOR_DRAW
    if score1 > score2:
        score1_color = COLOR_WINNING
        score2_color = COLOR_LOSING
    elif score1 < score2:
        score2_color = COLOR_WINNING
        score1_color = COLOR_LOSING
    screen.draw_score_left(score1, score1_color)
    screen.draw_score_right(score2, score2_color)


def check_collision():
    global ball, field, player_one, player_two

    player_one_paddle = player_one.paddle()
    player_two_paddle = player_two.paddle()

    # ball has reached left (player) side of field
    if field.hits_left_goal_area(ball.leftmost()):
        if (player_one_paddle.hits(ball.pos(COORD_Y))):
            ball.scale_vel(COORD_X, -1.0) 
            if abs(ball.vel(COORD_X)) < 18: # Cap on the speed of the ball
                ball.scale_vel(COORD_X, 1.15) 
            # Changes vertical vel of ball depending on where it hit the pad
            if ball.pos(COORD_Y) <= player_one_paddle.pos():
                ball.set_vel(COORD_Y, ball.vel(COORD_Y) - 0.5) 
            else:
                ball.set_vel(COORD_Y, ball.vel(COORD_Y) + 0.5) 
        else:
            player_two.increment_score()
            update_scores_display()
            spawn_ball(RIGHT)

    # ball has reached right (computer) side of field
    elif field.hits_right_goal_area(ball.rightmost()):
        if (player_two_paddle.hits(ball.pos(COORD_Y))):
            ball.scale_vel(COORD_X, -1.0) 
            if abs(ball.vel(COORD_X)) < 18:  # Cap on the speed of the ball
                ball.scale_vel(COORD_X, 1.15) 
            # Changes vertical vel of ball depending on where it hit the pad
            if ball.pos(COORD_Y) <= player_two_paddle.pos():
                ball.set_vel(COORD_Y, ball.vel(COORD_Y) - 0.5) 
            else:
                ball.set_vel(COORD_Y, ball.vel(COORD_Y) + 0.5) 
        else:
            player_one.increment_score()
            update_scores_display()
            spawn_ball(LEFT)


def spawn_ball(direction):
    global game_state, ball, field, screen
    vel = [0, 0]
    if direction == RIGHT:
        vel = [random.randrange(2, 4), -random.randrange(1, 3)]
    else:
        vel = [-random.randrange(2, 4), -random.randrange(1, 3)]
    ball = Ball(field.width() / 2, field.height() / 2, vel[0], vel[1], BALL_RADIUS)
    game_state.ball = ball
    screen.draw_ball(ball)


def new_game():
    global screen, player_one, player_two, running
    
    player_one.set_paddle(_new_base_paddle())
    screen.draw_left_paddle(player_one.paddle())
    
    player_two.set_paddle(_new_base_paddle())
    screen.draw_right_paddle(player_two.paddle())

    player_one.reset_score()
    player_two.reset_score()
    update_scores_display()

    spawn_ball(RIGHT)

    running = False  # Game starts paused to give player time to prepare
    screen.set_instructions_message(INFO_STRING_PAUSED)


def restart(event):
    global root, running
    if running:
        new_game()
    else:
        root.destroy()


def gameloop():
    global root, running
    root.after(1000 // 60, gameloop)
    if running:
        update_paddles()
        update_ball()
        check_collision()


# Initializations
root = Tk()
root.title(GAME_TITLE)

# place game window in a nice position on screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("+" + str(screen_width // 4) + "+" + str(screen_height // 4))  # using only offsets from left and top


# Field and screen
field = Field(WIDTH, HEIGHT, FIELD_COLOR, FIELD_COLOR_LINES, PAD_WIDTH)
screen = TkinterPypongScreen(root, field, PAD_HEIGHT, PAD_WIDTH, PLAYER_ONE_COLOR, PLAYER_TWO_COLOR)


# Info
screen.set_instructions_message(INFO_STRING)


# Ball
ball = Ball(field.width() / 2, field.height() / 2, 1, 1, BALL_RADIUS)
screen.create_ball_object(ball, BALL_COLOR)


# Players
player_one = Player(_new_base_paddle(), StrategyHumanPlayer(PLAYER_ONE))
player_two = Player(_new_base_paddle(), StrategySimpleComputerPlayer(PLAYER_TWO))
screen.create_left_paddle_object(player_one.paddle())
screen.create_right_paddle_object(player_two.paddle())


# Game state
game_state = GameState()
game_state.ball = ball 
game_state.player_one = player_one
game_state.player_two = player_two 
game_state.coord_x_universal_id = COORD_X
game_state.coord_y_universal_id = COORD_Y 
game_state.field_width = field.width()
game_state.field_height = field.height()
game_state.paddle_width = PAD_WIDTH
game_state.paddle_height = PAD_HEIGHT

# Game control
running = False


# User input
root.bind('<Key>', keydown)
root.bind('<space>', pause)
root.bind('<Escape>', restart)


# Start game loop
new_game()
gameloop()

# Start main loop
root.mainloop()
