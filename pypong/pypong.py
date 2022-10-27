try:
    from Tkinter import *  # Python 2
except ImportError:
    try:
        from tkinter import *  # Python 3
    except ImportError:
        raise ImportError("This program requires Tkinter, please make sure you have it installed.")

import random


# Constants
from GameConstants import *
from Player.Paddle import PAD_WIDTH, PAD_HEIGHT, HALF_PAD_WIDTH, HALF_PAD_HEIGHT


from Ball.Ball import Ball
from Player.Player import Player
from Player.Paddle import Paddle


# Helper functions
def _new_base_paddle():
    return Paddle(PADDLE_INITIAL_POSITION, 0, HEIGHT)


# Function definitions
def pause(event):
    global running, canvas, info_display
    running = not running
    if running:
        canvas.itemconfigure(info_display, text=INFO_STRING)
    else:
        canvas.itemconfigure(info_display, text=INFO_STRING_PAUSED)


def keydown(event):
    global player_one

    player_one_paddle = player_one.paddle()
    if event.char == "w":
        player_one_paddle.set_vel(-PADDLE_STEP)
    elif event.char == "s":
        player_one_paddle.set_vel(PADDLE_STEP)


def update_ball():
    global ball, canvas, ball_canvas_object
    ball.update()
    # ball has reached top or bottom of the field, must reflect
    if ((ball.pos(COORD_Y) + BALL_RADIUS) >= HEIGHT) or ((ball.pos(COORD_Y) - BALL_RADIUS) <= 0):
        ball.scale_vel(COORD_Y, -1) 
    canvas.coords(ball_canvas_object, ball.pos(COORD_X) - BALL_RADIUS, ball.pos(COORD_Y) - BALL_RADIUS, ball.pos(COORD_X) + BALL_RADIUS, ball.pos(COORD_Y) + BALL_RADIUS)


def update_paddles():
    global player_one, player_two, canvas, paddle_one_canvas_object, paddle_two_canvas_object, ball

    player_one.update_paddle()
    canvas.coords(paddle_one_canvas_object, HALF_PAD_WIDTH, player_one.paddle().pos() - HALF_PAD_HEIGHT, HALF_PAD_WIDTH, player_one.paddle().pos() + HALF_PAD_HEIGHT)

    ### COMPUTER MOVEMENT DECICION ###
    player_two_paddle = player_two.paddle()
    paddle2_pos = player_two_paddle.pos()
    paddle2_vel = player_two_paddle.vel()
    if ball.vel(COORD_X) > 0:
        if ball.pos(COORD_Y) > paddle2_pos and ball.vel(COORD_Y) > 0:
            paddle2_vel = PADDLE_STEP * 0.6
        elif ball.pos(COORD_Y) < paddle2_pos and ball.vel(COORD_Y) < 0:
            paddle2_vel = -PADDLE_STEP * 0.6
        # panic mode (when ball is close enough always attempt to match it)
        if ball.pos(COORD_X) > (WIDTH * 3 / 4):
            if ball.pos(COORD_Y) > (paddle2_pos + HALF_PAD_HEIGHT):
                paddle2_vel = PADDLE_STEP * 0.6
            elif ball.pos(COORD_Y) < (paddle2_pos - HALF_PAD_HEIGHT):
                paddle2_vel = -PADDLE_STEP * 0.6
    player_two_paddle.set_vel(paddle2_vel)
    ### END COMPUTER MOVEMENT DECICION ###

    player_two.update_paddle()
    canvas.coords(paddle_two_canvas_object, WIDTH - HALF_PAD_WIDTH, player_two.paddle().pos() - HALF_PAD_HEIGHT, WIDTH - HALF_PAD_WIDTH, player_two.paddle().pos() + HALF_PAD_HEIGHT)


def update_scores_display():
    global player_one, player_two, score1display, score2display
    score1 = player_one.score()
    score2 = player_two.score()
    canvas.itemconfigure(score1display, text=str(score1))
    canvas.itemconfigure(score2display, text=str(score2))
    if score1 > score2:
        canvas.itemconfigure(score1display, fill=COLOR_WINNING)
        canvas.itemconfigure(score2display, fill=COLOR_LOSING)
    elif score1 < score2:
        canvas.itemconfigure(score1display, fill=COLOR_LOSING)
        canvas.itemconfigure(score2display, fill=COLOR_WINNING)
    else:
        canvas.itemconfigure(score1display, fill=COLOR_DRAW)
        canvas.itemconfigure(score2display, fill=COLOR_DRAW)


def check_collision():
    global ball, player_one, player_two, canvas, ball_canvas_object, score1display, score2display

    player_one_paddle = player_one.paddle()
    player_two_paddle = player_two.paddle()

    # ball has reached left (player) side of field
    if (ball.pos(COORD_X) - BALL_RADIUS) <= PAD_WIDTH:
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
    elif (ball.pos(COORD_X) + BALL_RADIUS) >= (WIDTH - PAD_WIDTH):
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
    global ball, canvas, ball_canvas_object
    vel = [0, 0]
    if direction == RIGHT:
        vel = [random.randrange(2, 4), -random.randrange(1, 3)]
    else:
        vel = [-random.randrange(2, 4), -random.randrange(1, 3)]
    ball = Ball(WIDTH / 2, HEIGHT / 2, vel[0], vel[1])
    canvas.coords(ball_canvas_object, ball.pos(COORD_X) - BALL_RADIUS, ball.pos(COORD_Y) - BALL_RADIUS, ball.pos(COORD_X) + BALL_RADIUS, ball.pos(COORD_Y) + BALL_RADIUS)


def new_game():
    global canvas, player_one, player_two, paddle_one_canvas_object, paddle_two_canvas_object, score1display, score2display, running, info_display
    
    player_one.set_paddle(_new_base_paddle())
    canvas.coords(paddle_one_canvas_object, HALF_PAD_WIDTH, player_one.paddle().pos() - HALF_PAD_HEIGHT, HALF_PAD_WIDTH, player_one.paddle().pos() + HALF_PAD_HEIGHT)
    
    player_two.set_paddle(_new_base_paddle())
    canvas.coords(paddle_two_canvas_object, WIDTH - HALF_PAD_WIDTH, player_two.paddle().pos() - HALF_PAD_HEIGHT, WIDTH - HALF_PAD_WIDTH, player_two.paddle().pos() + HALF_PAD_HEIGHT)

    player_one.reset_score()
    player_two.reset_score()
    update_scores_display()

    spawn_ball(RIGHT)

    running = False  # Game starts paused to give player time to prepare
    canvas.itemconfigure(info_display, text=INFO_STRING_PAUSED)


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
root.title("PyPong")

# place game window in a nice position on screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("+" + str(screen_width // 4) + "+" + str(screen_height // 4))  # using only offsets from left and top

# Canvas / Field
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Field lines
canvas.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")
canvas.create_line(PAD_WIDTH, 0, PAD_WIDTH, HEIGHT, fill="white")
canvas.create_line(WIDTH - PAD_WIDTH, 0, WIDTH-PAD_WIDTH, HEIGHT, fill="white")

# Info
info_display = canvas.create_text(WIDTH / 4, HEIGHT - 25, text=INFO_STRING, fill="white", font=('Helvetica', '10'))

# Ball
ball = Ball(WIDTH / 2, HEIGHT / 2, 1, 1)
ball_canvas_object = canvas.create_oval(ball.pos(COORD_X) - BALL_RADIUS, ball.pos(COORD_Y) - BALL_RADIUS, ball.pos(COORD_X) + BALL_RADIUS, ball.pos(COORD_Y) + BALL_RADIUS, fill=BALL_COLOR)

# Players
player_one = Player(_new_base_paddle())
player_two = Player(_new_base_paddle())
paddle_one_canvas_object = canvas.create_line(HALF_PAD_WIDTH, player_one.paddle().pos() - HALF_PAD_HEIGHT, HALF_PAD_WIDTH, player_one.paddle().pos() + HALF_PAD_HEIGHT, fill=PLAYER_ONE_COLOR, width = PAD_WIDTH)
paddle_two_canvas_object = canvas.create_line(WIDTH - HALF_PAD_WIDTH, player_two.paddle().pos() - HALF_PAD_HEIGHT, WIDTH - HALF_PAD_WIDTH, player_two.paddle().pos() + HALF_PAD_HEIGHT, fill=PLAYER_TWO_COLOR, width=PAD_WIDTH)

# Scores
score1display = canvas.create_text(WIDTH / 4, HEIGHT / 4, text=str(player_one.score()), fill=COLOR_DRAW, font=('Helvetica', '30'))
score2display = canvas.create_text(WIDTH * 3/ 4, HEIGHT / 4, text=str(player_two.score()), fill=COLOR_DRAW, font=('Helvetica', '30'))

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
