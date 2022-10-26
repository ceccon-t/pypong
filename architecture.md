# PyPong - Architecture

## Structure

The main folder of the project is named `pypong`, and it is present at the root of the repository. Also at the root, `README.md` gives a short presentation at a project level, while this `architecture.md` file should quickly put any developer up to speed as to how the code is laid out. The `images` folder at root level contains images used only in the presentation of the repository, not to be used inside the application.

This project was initially developed with all the logic and data on a single file. Currently this is being refactored, the goal being to bring it closer to an object-oriented alignment. Until the refactor is finished, a significant part of the code will be located on file `pypong.py`, which also serves as the entry point of the application.

The most important constants used in the game can be found on file `GameConstants.py`.

Class `Ball` in `Ball/Ball.py` contains logic related to storing and updating position and velocity of the ball.

Class `Paddle` in `Player/Paddle.py` containss logic related to moving paddles and checking collisions with them. Deciding when to move (either from player input or AI) is planned to go elsewhere, meanwhile it is currently being done in the main script of the game.

To maintain compatibility with Python 2, all subfolders of main folder containing scripts have an empty `__init__.py` file.

## Automated Tests

Most classes contain a test suite associated with them, on a file with prefix `test_`. All tests can be executed by simply running `pytest` while on the main folder of the project, assuming that pytest is installed. For more info, check section on libraries and frameworks being used.

## Libraries and Frameworks

For the GUI, the project uses [Tkinter](https://docs.python.org/3/library/tkinter.html).

For automated tests, the project uses [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html).

