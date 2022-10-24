# Structure

The main folder of the project is named `pypong`, present at the root of the repository. Also at the root, `README.md` gives a short presentation at a project level, while this `architecture.md` file should quickly put any developer up to speed as to how the code is laid out. The `images` folder at root level contains images used only in the presentation of the repository, not to be used inside the application.

This project was initially developed with all the logic and data on a single file. Currently this is being refactored, the goal being to bring it closer to an object-oriented alignment. Until the refactor is finished, a significant part of the code will be located on file `pypong.py`, which also serves as the entry point of the application.

The most important constants used in the game can be found on file `GameConstants.py`.
