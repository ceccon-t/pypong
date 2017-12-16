import random

try:
    from Tkinter import *  # Python 2
except ImportError:
    try:
        from tkinter import *  # Python 3
    except ImportError:
        raise ImportError("This program requires Tkinter, please make sure you have it installed.")


# Constants
WIDTH = 800
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PADDLE_STEP = 4
LEFT = False
RIGHT = True
INFO_STRING = "Use W/S to move up/down.\nPress Space to pause.\nPress Esc once to start a new game, twice to quit."
INFO_STRING_PAUSED = "Press Space to unpause.\nPress Esc to quit."


def pause(event):
    global running, canvas, info_display
    running = not running
    if running:
        canvas.itemconfigure(info_display, text=INFO_STRING)
    else:
        canvas.itemconfigure(info_display, text=INFO_STRING_PAUSED)


def keydown(event):
    global paddle1_vel, paddle2_vel, paddle1_pos
    if event.char == "w":
        paddle1_vel = -PADDLE_STEP
    elif event.char == "s":
        paddle1_vel = PADDLE_STEP


def update_ball():
    global ball_center, ball_vel, canvas, ball
    ball_center[0] += ball_vel[0]
    ball_center[1] += ball_vel[1]
    if ((ball_center[1] + BALL_RADIUS) >= HEIGHT) or ((ball_center[1] - BALL_RADIUS) <= 0):
        ball_vel[1] *= -1
    canvas.coords(ball, ball_center[0] - BALL_RADIUS, ball_center[1] - BALL_RADIUS, ball_center[0] + BALL_RADIUS, ball_center[1] + BALL_RADIUS)


def update_paddles():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, canvas, paddle1, paddle2, ball_vel, ball_center

    new_paddle1_pos = paddle1_pos + paddle1_vel
    if new_paddle1_pos - HALF_PAD_HEIGHT >= 0 and new_paddle1_pos + HALF_PAD_HEIGHT <= HEIGHT:
        paddle1_pos = new_paddle1_pos
        canvas.coords(paddle1, HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT, HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT)
    paddle1_vel = 0

    ### AI SIMULATION FOR PADDLE 2 ###
    if ball_vel[0] > 0:
        if ball_center[1] > paddle2_pos and ball_vel[1] > 0:
            paddle2_vel = PADDLE_STEP * 0.6
        elif ball_center[1] < paddle2_pos and ball_vel[1] < 0:
            paddle2_vel = -PADDLE_STEP * 0.6
        # panic mode (when ball is close enough always attempt to match it)
        if ball_center[0] > (WIDTH * 3 / 4):
            if ball_center[1] > (paddle2_pos + HALF_PAD_HEIGHT):
                paddle2_vel = PADDLE_STEP * 0.6
            elif ball_center[1] < (paddle2_pos - HALF_PAD_HEIGHT):
                paddle2_vel = -PADDLE_STEP * 0.6
    ### END AI SIMULATION PADDLE 2 ###

    new_paddle2_pos = paddle2_pos + paddle2_vel
    if new_paddle2_pos - HALF_PAD_HEIGHT >= 0 and new_paddle2_pos + HALF_PAD_HEIGHT <= HEIGHT:
        paddle2_pos = new_paddle2_pos
        canvas.coords(paddle2, WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT, WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT)
    paddle2_vel = 0


def check_collision():
    global ball_center, ball_vel, paddle1_pos, paddle2_pos, canvas, ball, paddle1, paddle2, score1, score2, score1display, score2display
    if (ball_center[0] - BALL_RADIUS) <= PAD_WIDTH:
        if (ball_center[1] >= (paddle1_pos - HALF_PAD_HEIGHT)) and (ball_center[1] <= (paddle1_pos + HALF_PAD_HEIGHT)):
            ball_vel[0] *= -1.0
            if abs(ball_vel[0]) < 18: # Cap on the speed of the ball
                ball_vel[0] *= 1.15
            # print ball_vel[0]
            # Changes vertical vel of ball depending on where it hit the pad
            if ball_center[1] <= paddle1_pos:
                ball_vel[1] -= 0.5
            else:
                ball_vel[1] += 0.5
        else:
            score2 += 1
            canvas.itemconfigure(score2display, text=str(score2))
            spawn_ball(RIGHT)
    elif (ball_center[0] + BALL_RADIUS) >= (WIDTH - PAD_WIDTH):
        if (ball_center[1] >= (paddle2_pos - HALF_PAD_HEIGHT)) and (ball_center[1] <= (paddle2_pos + HALF_PAD_HEIGHT)):
            ball_vel[0] *= -1.0
            if abs(ball_vel[0]) < 18:  # Cap on the speed of the ball
                ball_vel[0] *= 1.15
            # print ball_vel[0]
            # Changes vertical vel of ball depending on where it hit the pad
            if ball_center[1] <= paddle2_pos:
                ball_vel[1] -= 0.5
            else:
                ball_vel[1] += 0.5
        else:
            score1 += 1
            canvas.itemconfigure(score1display, text=str(score1))
            spawn_ball(LEFT)


def spawn_ball(direction):
    global ball_center, ball_vel, canvas, ball
    ball_center = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel = [random.randrange(2, 4), -random.randrange(1, 3)]
    else:
        ball_vel = [-random.randrange(2, 4), -random.randrange(1, 3)]
    canvas.coords(ball, ball_center[0] - BALL_RADIUS, ball_center[1] - BALL_RADIUS, ball_center[0] + BALL_RADIUS, ball_center[1] + BALL_RADIUS)


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, canvas, paddle1, paddle2, score1, score2, score1display, score2display, running, info_display
    paddle1_pos = HEIGHT / 2
    canvas.coords(paddle1, HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT, HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT)
    paddle2_pos = HEIGHT / 2
    canvas.coords(paddle2, WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT, WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT)
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    canvas.itemconfigure(score1display, text=str(score1))
    score2 = 0
    canvas.itemconfigure(score2display, text=str(score2))
    spawn_ball(RIGHT)
    running = False
    canvas.itemconfigure(info_display, text=INFO_STRING_PAUSED)


def restart(event):
    global root, running
    if running:
        new_game()
    else:
        root.destroy()


def gameloop():
    global root, canvas, ball_center, ball, paddle1_pos, paddle2_pos, paddle1, paddle2, running
    root.after(1000 // 60, gameloop)
    if running:
        update_paddles()
        update_ball()
        check_collision()


# Initializations
root = Tk()
root.title("Simple Pong")

# place game window in a nice position on screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("+" + str(screen_width // 4) + "+" + str(screen_height // 4))  # using only offsets from left and top

canvas = Canvas(root, width=WIDTH, height= HEIGHT, bg="black")
canvas.pack()

# Field lines
canvas.create_line(WIDTH / 2, 0, WIDTH / 2, HEIGHT, fill="white")
canvas.create_line(PAD_WIDTH, 0, PAD_WIDTH, HEIGHT, fill="white")
canvas.create_line(WIDTH - PAD_WIDTH, 0, WIDTH-PAD_WIDTH, HEIGHT, fill="white")

# Ball
ball_center = [WIDTH / 2, HEIGHT / 2]
ball_vel = [1, 1]
ball = canvas.create_oval(ball_center[0] - BALL_RADIUS, ball_center[1] - BALL_RADIUS, ball_center[0] + BALL_RADIUS, ball_center[1] + BALL_RADIUS, fill="white")

# Paddles
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
paddle1 = canvas.create_line(HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT, HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT, fill="white", width = PAD_WIDTH)
paddle2 = canvas.create_line(WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT, WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT, fill="white", width=PAD_WIDTH)

# Scores
score1 = 0
score2 = 0

score1display = canvas.create_text(WIDTH / 4, HEIGHT / 4, text=str(score1), fill="white", font=('Helvetica', '30'))
score2display = canvas.create_text(WIDTH * 3/ 4, HEIGHT / 4, text=str(score2), fill="white", font=('Helvetica', '30'))

info_display = canvas.create_text(WIDTH / 4, HEIGHT - 25, text=INFO_STRING, fill="white", font=('Helvetica', '10'))

# Game control
running = False


root.bind('<Key>', keydown)
root.bind('<space>', pause)
root.bind('<Escape>', restart)


# Start game loop
new_game()
gameloop()

# Start main loop
root.mainloop()
