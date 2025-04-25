from BFS import BFS
from DFS import DFS
from Mazegenerator import generate_maze_with_eller
import copy


def run_algorithm(algorithm_class, maze, label):
    print(f"  --- {label} ---")
    algo = algorithm_class(maze)
    result = algo.solve()

    if result:
        path, steps = result
        algo.mark_path(path)
        print(f"    Gefundener Pfad: {path}")
        print(f"    Pfadlänge (Manhattan Distance): {len(path)}")
        print(f"    Benötigte Schritte: {steps}")
    else:
        print("    Kein Pfad gefunden.")


def main():
    start_size = 10  # Startgröße des Labyrinths
    step_size = 50  # Schrittgröße bei der Skalierung
    max_size = 1000  # Maximale Labyrinthgröße

    for size in range(start_size, max_size + 1, step_size):
        print(f"\nErstelle Labyrinth der Größe {size}x{size}...")

        # Labyrinth mit der aktuellen Größe generieren
        base_maze = generate_maze_with_eller(size, size)

        # BFS ausführen (auf Kopie des Labyrinths)
        bfs_maze = copy.deepcopy(base_maze)
        print(f"  BFS auf {size}x{size}:")
        run_algorithm(BFS, bfs_maze, "Breadth-First Search (BFS)")

        # DFS ausführen (ebenfalls auf Kopie)
        dfs_maze = copy.deepcopy(base_maze)
        print(f"  DFS auf {size}x{size}:")
        run_algorithm(DFS, dfs_maze, "Depth-First Search (DFS)")


if __name__ == "__main__":
    main()
