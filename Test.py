from matplotlib import pyplot as plt
import numpy as np
from CompareBFStoBFS import test_maze, get_average_steps, get_average_time, get_average_path_length


def main():

    #bfs
    bfs_avg_steps = []
    bfs_avg_time = []
    bfs_avg_path_lengths = []

    #dfs
    dfs_avg_steps = []
    dfs_avg_time = []
    dfs_avg_path_lengths = []

    dimensions = []

    for _ in range(50, 1001, 50):
        bfs_results, dfs_results, bfs_paths, dfs_paths = test_maze(_, 10, 1)

        bfs_avg_steps.append(get_average_steps(bfs_results))
        bfs_avg_time.append(get_average_time(bfs_results))
        bfs_avg_path_lengths.append(get_average_path_length(bfs_results))

        dfs_avg_steps.append(get_average_steps(dfs_results))
        dfs_avg_time.append(get_average_time(dfs_results))
        dfs_avg_path_lengths.append(get_average_path_length(dfs_results))

        dimensions.append(_)


    plt.plot(dimensions, bfs_avg_steps, marker='o', label="BFS")
    plt.plot(dimensions, dfs_avg_steps, marker='o', label="DFS")
    #plt.xticks(np.arange(0, 201, 50))
    plt.xlabel("Dimension")
    plt.ylabel("Ø Schrittanzahl")
    plt.grid(True)
    plt.title("Durchschnittliche Schrittanzahl nach Dimension des Labyrinths \n mit 10 Tests/Dimension")
    plt.legend()

    plt.savefig('/Users/lewinci/Library/Mobile Documents/com~apple~CloudDocs/Uni/BAI4–KI/Praktikum/Praktikum 1 - Baumsuchverfahren/dead_end_maze_step_compare_1000.png')
    plt.show()

    print(f"{bfs_avg_steps}\n")
    print(f"{bfs_avg_path_lengths}\n")

    print(f"{dfs_avg_steps}\n")
    print(f"{dfs_avg_path_lengths}\n")


if __name__ == "__main__":
    main()