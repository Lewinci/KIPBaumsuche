import random
from Maze import Maze

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def generate_maze_with_eller(width, height, min_man_distance=None, max_man_distance=None):
    assert 0 < width <= 1000
    assert 0 < height <= 1000
    #assert 0 < min_man_distance
    #assert min_man_distance <= max_man_distance <= (maze_width + maze_height)

    maze = Maze(width, height)

    # Initialize each cell with a unique set
    sets = [i for i in range(width)]
    grid = [[0 for _ in range(width)] for _ in range(height)]
    next_set = width

    for y in range(height):
        # JOIN RIGHT CELLS
        for x in range(width - 1):
            if sets[x] != sets[x + 1] and (random.random() < 0.5 or y == height - 1):
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

        # --- START & ZIEL SETZEN ---
        valid_positions = [(x, y) for y in range(height) for x in range(width) if grid[y][x] == 1]

        if min_man_distance is not None and max_man_distance is not None:
            while True:
                start = random.choice(valid_positions)
                goal = random.choice(valid_positions)
                dist = manhattan_distance(start, goal)
                if min_man_distance <= dist <= max_man_distance:
                    break
            maze.set_start(*start)
            maze.set_goal(*goal)
        else:
            # Standard: Start links oben, Ziel rechts unten
            maze.set_start(0, 0)
            maze.set_goal(width, height)


    return maze