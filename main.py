from BFS import BFS
from DFS import DFS
from Mazegenerator import generate_maze_with_eller
from Maze import Maze

def run_algorithm(algorithm_class, maze, label):
    print(f"\n--- {label} ---")
    algo = algorithm_class(maze)
    result = algo.solve()

    if result:
        path, steps = result
        algo.mark_path(path)
        maze.print_maze()
        print(f"Gefundener Pfad: {path}\n")
        print(f"Pfadlänge (Manhattan Distance): {len(path)}")
        print(f"Benötigte Schritte: {steps}")
    else:
        print("Kein Pfad gefunden.")

def main():
    width, height = 15, 15

    # Fixe Start-/Zielposition, immer gleiches Labyrinth für beide Algorithmen
    base_maze = generate_maze_with_eller(width, height)

    # BFS ausführen (auf Kopie des Labyrinths)
    import copy
    bfs_maze = copy.deepcopy(base_maze)
    run_algorithm(BFS, bfs_maze, "Breadth-First Search (BFS)")

    # DFS ausführen (ebenfalls auf Kopie)
    dfs_maze = copy.deepcopy(base_maze)
    run_algorithm(DFS, dfs_maze, "Depth-First Search (DFS)")

if __name__ == "__main__":
    main()
