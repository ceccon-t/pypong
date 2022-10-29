PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

PADDLE_STEP = 4
 
class Paddle():
    
    def __init__(self, position, limit_top, limit_bottom):
        self.position = position 
        self.limit_top = limit_top
        self.limit_bottom = limit_bottom
        self.velocity = 0

    def pos(self):
        return self.position

    def vel(self):
        return self.velocity

    def topmost(self):
        return self.position - HALF_PAD_HEIGHT

    def bottommost(self):
        return self.position + HALF_PAD_HEIGHT

    def accelerate(self, acceleration_factor):
        self.velocity = acceleration_factor * PADDLE_STEP

    def update(self):
        new_pos = self.position + self.velocity
        top = new_pos - HALF_PAD_HEIGHT
        bottom = new_pos + HALF_PAD_HEIGHT
        if top >= self.limit_top and bottom <= self.limit_bottom:
            self.position = new_pos

    def hits(self, other_position):
        top = self.position - HALF_PAD_HEIGHT
        bottom = self.position + HALF_PAD_HEIGHT
        return other_position >= top and other_position <= bottom