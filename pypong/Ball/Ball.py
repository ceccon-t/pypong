class Ball:

    def __init__(self, center_x, center_y, vel_x, vel_y, radius):
        self._center = [center_x, center_y]
        self._velocity = [vel_x, vel_y]
        self._radius = radius

    def pos(self, coord):
        return self._center[coord]

    def vel(self, coord):
        return self._velocity[coord]

    def update(self):
        self._center[0] += self._velocity[0]
        self._center[1] += self._velocity[1]

    def set_vel(self, coord, value):
        self._velocity[coord] = value 

    def scale_vel(self, coord, scaling_factor):
        self._velocity[coord] *= scaling_factor

    def leftmost(self):
        return self._center[0] - self._radius

    def rightmost(self):
        return self._center[0] + self._radius

    def topmost(self):
        return self._center[1] - self._radius

    def bottommost(self):
        return self._center[1] + self._radius


