import random

# Saving the Class as its own py file nd importing afterwards
# avoiding to hardcode any set values. Pass them as the Object paramenters instead
# Try to impose as little as possible to the end user. Some suggested restrictions can be presented
# as a Class method, so the user can use it or write their own.

class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4,8)):
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, x_boundary)
        self.y = random.randrange(0, y_boundary)
        self.size = random.randrange(size_range[0], size_range[1]) # specific to Pygame. Play around to see results

    def move(self):
        self.move_x = random.randrange(-2,3)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y

    def check_boundary(self):
        if self.x < 0:
            self.x = 0 + self.size
        elif self.x > self.x_boundary:
            self.x = self.x_boundary - self.size

        if self.y < 0:
            self.y = 0 - self.size
        elif self.y > self.y_boundary:
            self.y = self.y_boundary - self.size