class Player:
    
    def __init__(self, paddle, strategy):
        self._paddle = paddle
        self._strategy = strategy
        self._score = 0

    def paddle(self):
        return self._paddle

    def set_paddle(self, new_paddle):
        self._paddle = new_paddle

    def update_paddle(self):
        self._paddle.update()
        self._paddle.accelerate(0)

    def move(self, game_state):
        acceleration_factor = self._strategy.decide_acceleration_factor(game_state)
        self._paddle.accelerate(acceleration_factor)
        self.update_paddle()

    def score(self):
        return self._score

    def increment_score(self):
        self._score += 1

    def reset_score(self):
        self._score = 0