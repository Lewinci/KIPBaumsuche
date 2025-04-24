from collections import deque


class BFS:
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()  # Menge aller besuchter Knoten
        self.came_from = {}  # Arrays zur nachverfolgung des Pfades

    def solve(self):
        start = self.maze
        goal = self.maze.goal

        queue = deque()  # Warteschlage der noch zu besuchenden Knoten
        queue.append(start)  # Füge den Startpunkt ein
        self.visited.add(start)  # Startpunkt als besucht markieren
        self.came_from[start] = None  # Startpunkt hat keinen Vorgänger

        # Solange es Knoten in der Queue gibt hol dir den vordersten raus/ FIFO
        while queue:
            current = queue.popleft()

            # Ziel gefunden?
            if current == goal:
                return self.reconstruct_path(current)

            # holen uns die benachbarten Knoten, auf welchen wir noch nicht waren
            for neighbor in self.get_neighbors(current):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)  # als besucht markieren
                    self.came_from[neighbor] = current  # pfad speichern
                    queue.append(neighbor)  # Nachbarn zu Queue hinzufügen

        return None  # Kein Pfad gefunden

    def reconstruct_path(self, end):
        path = []
        current = end
        # solange current nicht none ist, füge current zu path hinzu und setze current auf den Knoten vom welchem ich komme
        while current != None:
            path.append(current)
            current = self.came_from[current]
            path.reverse()
            return path

    def get_neighbors(self, position):
        x, y = position
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Rechts, unten, links, oben
        neighbors = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)
            if self.maze.is_valid(neighbor):
                neighbors.append(neighbor)

        return neighbors