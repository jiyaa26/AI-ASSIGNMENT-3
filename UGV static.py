import heapq
import random
import time

SIZE = 70

def create_grid(density):
    grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            if random.random() < density:
                grid[i][j] = 1
    return grid


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}
    nodes_explored = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_explored += 1

        if current == goal:
            return reconstruct_path(came_from, current), nodes_explored

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            neighbor = (current[0]+dx, current[1]+dy)

            if 0 <= neighbor[0] < SIZE and 0 <= neighbor[1] < SIZE:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                temp_g = g_score[current] + 1

                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f = temp_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f, neighbor))
                    came_from[neighbor] = current

    return None, nodes_explored


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]


start = (0, 0)
goal = (69, 69)

for density in [0.1, 0.2, 0.3]:
    grid = create_grid(density)

    start_time = time.time()
    path, nodes = astar(grid, start, goal)
    end_time = time.time()

    print(f"\nDensity: {int(density*100)}%")

    if path:
        print("Path found!")
        print("Path length:", len(path))
    else:
        print("No path found")

    print("Nodes explored:", nodes)
    print("Time taken:", round(end_time - start_time, 4), "seconds")
