class Ball:

    def __init__(self, center_x, center_y, vel_x, vel_y):
        self.center = [center_x, center_y]
        self.velocity = [vel_x, vel_y]

    def pos(self, coord):
        return self.center[coord]

    def vel(self, coord):
        return self.velocity[coord]

    def update(self):
        self.center[0] += self.velocity[0]
        self.center[1] += self.velocity[1]

    def set_vel(self, coord, value):
        self.velocity[coord] = value 

    def scale_vel(self, coord, scaling_factor):
        self.velocity[coord] *= scaling_factor


