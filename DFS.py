
from Maze import Maze
import Mazegenerator

class DFS:
    def __init__(self, maze):
        if not isinstance(maze, Maze):
            raise TypeError("Es muss ein Objekt der Klasse Maze übergeben werden.")

        self.maze = maze

    def solve(self):

        steps = 0

        closed_list = set()
        open_list = []

        start = self.maze.start
        goal = self.maze.goal

        open_list.append(start)
        closed_list.add(start)

        parent = {}  # um später Pfad zurückverfolgen zu können

        while open_list:
            current = open_list.pop()
            if current == goal:
                return self.reconstruct_path(parent), steps
            for neighbour in self.getNeighbours(current):
                if neighbour not in closed_list:
                    parent[neighbour] = current
                    closed_list.add(neighbour)
                    open_list.append(neighbour)
            steps += 1

        return None

    def getNeighbours(self, position):
        neighbours = []
        x ,y = position

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Rechts, unten, links, oben

        for x_direction, y_direction in directions:
            current_neighbour = (x + x_direction, y + y_direction)
            if self.maze.is_valid(current_neighbour[0], current_neighbour[1]):
                neighbours.append(current_neighbour)

        return neighbours

    def reconstruct_path(self, parent):
        path = []
        current = self.maze.goal

        while current != self.maze.start:
            path.append(current)
            current = parent[current]
        path.append(self.maze.start)
        path.reverse()
        return path

    def mark_path(self, path):
            for c in path:
                self.maze.grid[c[0]][c[1]] = '🔸'



maze1 = Mazegenerator.generate_maze_with_eller(1000, 1000)

dfs = DFS(maze1)
path, steps = dfs.solve()
dfs.mark_path(path)

if path:
    maze1.print_maze()
    print(f"Gefundener Pfad: {path}\n")
    print(f"Manhatten Distance: {len(path)}\n")
    print(f"Steps: {steps}\n")

else:
    print("Kein Pfad gefunden.")