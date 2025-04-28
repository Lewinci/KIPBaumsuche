import Mazegenerator
from Maze import Maze
import DFS
import BFS
import Maze
import time
import statistics

def test_maze(dim, iterations, dead_end_or_obstacle_maze):

    bfs_path_results = []
    dfs_path_results = []

    bfs_results = []
    dfs_results = []

    maze = None

    for i in range(iterations):
        if dead_end_or_obstacle_maze == 0:
            maze = Mazegenerator.generate_maze_with_eller(dim, dim)
        elif dead_end_or_obstacle_maze == 1:
            maze = Mazegenerator.generate_maze_with_dead_ends(dim)


        bfs = BFS.BFS(maze)
        dfs = DFS.DFS(maze)
        #solve Methoden returnen path und steps als Tupel
        start = time.time()
        bfs_path_and_results = bfs.solve()
        end = time.time()
        bfs_time = round(end - start, 3)

        start = time.time()
        dfs_path_and_results = dfs.solve()
        end = time.time()
        dfs_time = round(end - start, 3)

        bfs_results.append((bfs_path_and_results[1], bfs_time))
        dfs_results.append((dfs_path_and_results[1], dfs_time))

        bfs_path_results.append(bfs_path_and_results[0])
        dfs_path_results.append((dfs_path_and_results[0]))

    return bfs_results, dfs_results, bfs_path_results, dfs_path_results

def get_average_steps(algo_results):
    sum_of_steps = sum(tupel[0] for tupel in algo_results)
    step_avg = sum_of_steps / len(algo_results)
    return step_avg

def get_average_time(algo_results):
    sum_of_time = sum(tupel[1] for tupel in algo_results)
    time_avg = sum_of_time / len(algo_results)
    return time_avg

def get_average_path_length(algo_results):

    path_lengths = []
    for _ in algo_results:
        path_lengths.append(len(_))
    return sum(path_lengths) / len(algo_results)
