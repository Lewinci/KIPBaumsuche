
class Maze:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        #2D Array wird vorerst mit Nullen gefüllt
        self.grid = [[1 for _ in range(width)] for _ in range(height)]

        self.start = (0, 0)
        self.goal = (width -1, height -1)


    def set_start(self, x, y):
        self.start = (x, y)

    def set_goal(self, x, y):
        self.goal = (x - 1, y - 1)

    def set_obstacle(self, x, y):
        check_obstacle_position = (x,y)
        if check_obstacle_position != self.goal and check_obstacle_position != self.start:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x] = 1
            else:
                raise ValueError(f"Position ({x}, {y}) out of bounds.")

        else:
            raise ValueError(f"Position ({x}, {y}) cannot be start or goal position.")

    def set_path(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = 0
        else:
            raise ValueError(f"Position ({x}, {y}) out of bounds.")


    def is_valid(self, x, y):
        return (0 <= x < self.width and 0 <= y < self.height) and (self.grid[x][y] == 0)

    def print_maze(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                pos = (x, y)
                if pos == self.start:
                    row += "S"
                elif pos == self.goal:
                    row += "G"
                elif self.grid[y][x] == 1:
                    row += "█"
                elif self.grid[y][x] == '@':
                    row += "@"
                elif self.grid[y][x] == 'X':
                    row += "Y"
                else:
                    row += " "
            print(row)
