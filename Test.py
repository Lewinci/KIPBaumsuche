from matplotlib import pyplot as plt
import numpy as np
from CompareBFStoBFS import test_maze, get_average_steps, get_average_time

def test_10x10(dim, maze_type):
    bfs_results, dfs_results = test_maze(dim, 10, maze_type)

    print(f"{get_average_steps(bfs_results)}\n")
    print(f"{get_average_time(bfs_results)}\n")

    print(f"{get_average_steps(dfs_results)}\n")
    print(f"{get_average_time(dfs_results)}\n")


    return get_average_steps(bfs_results), get_average_time(bfs_results)



def main():

    #bfs
    bfs_avg_steps = []
    bfs_avg_time = []

    #dfs
    dfs_avg_steps = []
    dfs_avg_time = []

    dimensions = []

    for _ in range(50, 201, 50):
        bfs_results, dfs_results = test_maze(_, 10, 0)

        bfs_avg_steps.append(get_average_steps(bfs_results))
        bfs_avg_time.append(get_average_time(bfs_results))

        dfs_avg_steps.append(get_average_steps(dfs_results))
        dfs_avg_time.append(get_average_time(dfs_results))

        dimensions.append(_)


    plt.plot(dimensions, bfs_avg_steps, marker='o', label="BFS")
    plt.plot(dimensions, dfs_avg_steps, marker='o', label="DFS")
    #plt.xticks(np.arange(0, 201, 50))
    plt.xlabel("Dimension")
    plt.ylabel("Ø Schrittzahl")
    plt.grid(True)
    plt.title("Durchschnittliche Schrittzahl nach Dimension des Labyrinths")
    plt.legend()
    plt.show()

    print(f"{bfs_avg_steps}\n")
    print(f"{bfs_avg_time}\n")

    print(f"{dfs_avg_steps}\n")
    print(f"{dfs_avg_time}\n")


if __name__ == "__main__":
    main()