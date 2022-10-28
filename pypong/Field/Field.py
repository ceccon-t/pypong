class Field:

    def __init__(self, width, height, color, paddle_width):
        self._width = width 
        self._height = height 
        self._color = color
        self._paddle_width = paddle_width

    def width(self):
        return self._width

    def height(self):
        return self._height

    def color(self):
        return self._color

    def hits_top(self, pos_y):
        return pos_y <= 0

    def hits_bottom(self, pos_y):
        return pos_y >= self._height

    def hits_left_goal_area(self, pos_x):
        return pos_x <= self._paddle_width

    def hits_right_goal_area(self, pos_x):
        return pos_x >= self._width -  self._paddle_width

