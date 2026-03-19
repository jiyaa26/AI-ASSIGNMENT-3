import heapq
import random
import time

SIZE = 20   # smaller grid for demo


def create_grid():
    return [[0 for _ in range(SIZE)] for _ in range(SIZE)]


def add_dynamic_obstacles(grid, probability=0.2):
    for i in range(SIZE):
        for j in range(SIZE):
            if random.random() < probability:
                grid[i][j] = 1


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

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

    return None


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    return path[::-1]


# Simulation
grid = create_grid()
start = (0, 0)
goal = (19, 19)

current = start

while current != goal:
    path = astar(grid, current, goal)

    if not path:
        print("No path available!")
        break

    next_step = path[0]

    # Simulate dynamic obstacle appearing randomly
    if random.random() < 0.3:
        x, y = next_step
        grid[x][y] = 1
        print("Obstacle appeared! Replanning...")
        continue

    current = next_step
    print("Moving to:", current)

print("Reached Goal!" if current == goal else "Failed!")
