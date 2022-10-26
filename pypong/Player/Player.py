class Player:
    
    def __init__(self):
        self._score = 0

    def score(self):
        return self._score

    def increment_score(self):
        self._score += 1

    def reset_score(self):
        self._score = 0