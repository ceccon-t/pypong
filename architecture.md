# PyPong - Architecture

## Structure

The main folder of the project is named `pypong`, and it is present at the root of the repository. Also at the root, `README.md` gives a short presentation at a project level, while this `architecture.md` file should quickly put any developer up to speed as to how the code is laid out. The `images` folder at root level contains images used only in the presentation of the repository, not to be used inside the application.

This project was initially developed with all the logic and data on a single file. Currently this is being refactored, the goal being to bring it closer to an object-oriented alignment. Until the refactor is finished, a significant part of the code will be located on file `pypong.py`, which also serves as the entry point of the application.

The most important constants used in the game can be found on file `GameConstants.py`.

Classes `Ball`, `Field` and `Paddle` (this one under `Player` folder) contain the logic to model and manipulate the respective game elements. Class `Player` contains a reference to the `Paddle` that this player controls, as well as a reference to a `Strategy` object to which player movement decisions should be delegated.

All player movements, either from human players or AI players, are handled in classes that extend `Strategy`, implementing its only method. Any strategy implemented should use the `GameState` object that this method receives as a parameter to determine if the player's paddle should move down (by returning a positive number), up (by returning a negative number) or stay put (by returning zero) - the returned value should preferably be on the -1.0 to 1.0 range. The game currently contains two strategies, one for human players and one for a very basic AI player. 

Class `TkinterPypongScreen` is responsible to handle most of the specifics of displaying things on the screen, leaving the game logic and modeling to the other classes mentioned above.

To maintain compatibility with Python 2, all subfolders of main folder containing scripts have an empty `__init__.py` file.

## Automated Tests

Most classes contain a test suite associated with them, on a file with prefix `test_`. All tests can be executed by simply running `pytest` while on the main folder of the project, assuming that pytest is installed. For more info, check section on libraries and frameworks being used. Although the game currently works on Python 2, automated tests will only be maintained for Python 3.

## Libraries and Frameworks

For the GUI, the project uses [Tkinter](https://docs.python.org/3/library/tkinter.html).

For automated tests, the project uses [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html).

