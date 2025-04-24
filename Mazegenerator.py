import random
from Maze import Maze
from googoomaze import create_maze

#MIN_MANHATTEN_DISTANCE = 1

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def generate_maze_with_eller(width, height):
    assert 0 < width <= 1000
    assert 0 < height <= 1000  

    maze = Maze(width, height)
    epsilon = 0.2
    # Initialize each cell with a unique set
    sets = [i for i in range(width)]
    grid = [[0 for _ in range(width)] for _ in range(height)]
    next_set = width

    for y in range(height):
        # JOIN RIGHT CELLS
        for x in range(width - 1):
            if sets[x] != sets[x + 1] and (random.random() < epsilon or y == height - 1):
                old_set, new_set = sets[x + 1], sets[x]
                for i in range(width):
                    if sets[i] == old_set:
                        sets[i] = new_set
                grid[y][x + 1] = 1  # remove wall

        # CREATE VERTICAL CONNECTIONS
        new_sets = [-1] * width
        for set_id in set(sets):
            members = [i for i, s in enumerate(sets) if s == set_id]
            num_verticals = max(1, random.randint(1, len(members)))
            verticals = random.sample(members, num_verticals)
            for x in verticals:
                if y + 1 < height:
                    grid[y + 1][x] = 1  # remove wall
                    new_sets[x] = set_id

        # Update sets for next row
        for x in range(width):
            if new_sets[x] == -1:
                new_sets[x] = next_set
                next_set += 1
        sets = new_sets

        # Mark all paths
        for x in range(width):
            if grid[y][x] == 1:
                maze.set_path(x, y)

    # Erzeuge gültige Start- und Zielposition mit Mindestdistanz
    #valid_positions = [(x, y) for y in range(height) for x in range(width) if grid[y][x] == 1]
    #while True:
    #    start = random.choice(valid_positions)
    #    goal = random.choice(valid_positions)
    #    if max_man_distance >= manhattan_distance(start, goal) >= min_man_distance:
    #        break

    #maze.set_start(*start)
    #maze.set_goal(goal[0] + 1, goal[1] + 1)  # wie in set_goal mit -1 Korrektur'


    return maze


def generate_maze(dim):
    # create a new maze from sample code
    M = create_maze(dim)
    print(M)
    # converting the numpy array into a Maye object
    maze = Maze(dim*2+1,dim*2+1)
    for y in range(dim*2+1):
        for x in range(dim*2+1):
            if M[y,x] == 0:
                maze.set_path(x, y)

    maze.set_start(1,0)
    maze.set_goal(dim*2,dim*2+1) 
    return maze


