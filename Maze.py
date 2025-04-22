import random
class Maze:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        #2D Array wird vorerst mit Nullen gefüllt
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

        self.start = (0, 0)
        self.goal = (width, height)

    def set_start(self, x, y):
        self.start = (x, y)

    def set_goal(self, x, y):
        self.goal = (x, y)

    def set_obstacle(self, x, y):
        check_obstacle_position = (x,y)
        if check_obstacle_position != self.goal and check_obstacle_position != self.start:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[x][y] = 1
            else:
                raise ValueError(f"Position ({x}, {y}) out of bounds.")

        else:
            raise ValueError(f"Position ({x}, {y}) cannot be start or goal position.")

    def set_path(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[x][y] = 1
        else:
            raise ValueError(f"Position ({x}, {y}) out of bounds.")

