# PyPong

![Game paused](https://raw.githubusercontent.com/ceccon-t/pypong/main/images/Py-Pong-Sc0.png "Game paused")

## Description

A version of the iconic game Pong, implemented in Python with Tkinter.

Move your paddle and intercept the ball so as to prevent it getting past you, while trying to make it go past your AI opponent's line. Each time either of you hits the ball, its speed increases, making it more difficult to defend.

There is no time limit, matches can go on for as long as the player desires. The score is kept and displayed on screen at all times.

How much of a lead can you manage to achieve over the machine?

![Game running](https://raw.githubusercontent.com/ceccon-t/pypong/main/images/Py-Pong-Sc1.png "Game running")

## How to play

Use keys W and S to move the player paddle up and down, respectively.

Pause the game by pressing the Space key, and restart by pressing Esc. Press Esc twice to quit the game and close the window.

The instructions are also always displayed on the screen.

## How to Run

From the root of the repository, navigate into pypong folder and run `pypong.py` with your installed Python executable. 

For instance, on a Linux you would do: `$ python pypong.py`

Python 3 is highly preferable, though the project works with Python 2 as well for now.

## How to run automated tests

Make sure you have pytest installed.

Then navigate to the main folder of the project with a terminal and run `pytest`. The test results will be displayed in the standard output of the terminal.

## More info

To get a short intro to how the code is organized and the development history, you can check `architecture.md`.
