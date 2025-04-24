from collections import deque
from Maze import Maze
import Mazegenerator


class BFS:
    def __init__(self, maze):
        # Überprüfen, ob maze ein Objekt der Klasse Maze ist
        if not isinstance(maze, Maze):
            raise TypeError("Es muss ein Objekt der Klasse Maze übergeben werden.")

        self.maze = maze
        self.visited = set()  # Menge aller besuchter Knoten
        self.came_from = {}  # Dictionar zur Nachverfolgung des Pfades

    def solve(self):
        start = self.maze.start  # Holen der Startposition aus dem Maze-Objekt
        goal = self.maze.goal  # Holen der Zielposition aus dem Maze-Objekt

        open_list = deque()  # Warteschlange für noch zu besuchende Knoten
        open_list.append(start)  # Füge den Startpunkt hinzu
        self.visited.add(start)  # Markiere den Startpunkt als besucht
        self.came_from[start] = None  # Der Startpunkt hat keinen Vorgänger

        # Solange es Knoten in der open_list gibt, hole dir den vordersten Knoten raus (FIFO)
        while open_list:
            current = open_list.popleft()
            # Ziel gefunden?
            if current == goal:
                return self.reconstruct_path(current)

            # Hole dir die benachbarten Knoten, die noch nicht besucht wurden
            for neighbor in self.get_neighbors(current):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)  # Markiere als besucht
                    self.came_from[neighbor] = current  # Speichere den Pfad
                    open_list.append(neighbor)  # Füge den Nachbarn der open_list hinzu

        return None  # Kein Pfad gefunden

    def reconstruct_path(self, end):
        path = []
        current = end
        # Solange current nicht None ist, füge es zum Pfad hinzu und setze current auf den Vorgänger
        while current is not None:
            path.append(current)
            current = self.came_from[current]
        path.reverse()  # Umkehren des Pfades
        return path

    def get_neighbors(self, position):
        x, y = position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Rechts, unten, links, oben
        neighbors = []

        # Prüfe alle benachbarten Knoten
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)
            if self.maze.is_valid(neighbor[0], neighbor[1]):  # Überprüfe, ob der Nachbar gültig ist
                neighbors.append(neighbor)

        return neighbors

    def mark_path(self, path):
            for c in path:
                self.maze.grid[c[0]][c[1]] = '*'


# Beispielhafte Nutzung
maze = Mazegenerator.generate_maze_with_eller(100, 100)
bfs = BFS(maze)
path = bfs.solve()
bfs.mark_path(path)

if path:
    maze.print_maze()
    print(f"Gefundener Pfad: {path}\n")
    print(len(path))

else:
    print("Kein Pfad gefunden.")
