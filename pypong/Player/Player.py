class Player:
    
    def __init__(self, paddle):
        self._paddle = paddle
        self._score = 0

    def paddle(self):
        return self._paddle

    def set_paddle(self, new_paddle):
        self._paddle = new_paddle

    def update_paddle(self):
        self._paddle.update()
        self._paddle.accelerate(0)

    def score(self):
        return self._score

    def increment_score(self):
        self._score += 1

    def reset_score(self):
        self._score = 0