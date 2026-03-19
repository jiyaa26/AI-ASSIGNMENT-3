1 Dijkstra:
This program implements Dijkstra’s Algorithm to find the shortest path between Indian cities. Each city is treated as a node and distances between them are considered as edge weights. The algorithm calculates the minimum distance from a given starting city to all other cities using a priority queue approach.

| City       | Shortest Distance | Path                                |
| ---------- | ----------------- | ----------------------------------- |
| Delhi      | 0                 | Delhi                               |
| Jaipur     | 280               | Delhi → Jaipur                      |
| Lucknow    | 550               | Delhi → Lucknow                     |
| Chandigarh | 250               | Delhi → Chandigarh                  |
| Ahmedabad  | 950               | Delhi → Jaipur → Ahmedabad          |
| Patna      | 1150              | Delhi → Lucknow → Patna             |
| Mumbai     | 1480              | Delhi → Jaipur → Ahmedabad → Mumbai |
| Kolkata    | 1730              | Delhi → Lucknow → Patna → Kolkata   |

## Input
- Graph of Indian cities with distances
- User enters starting city (e.g., Delhi)

## Output
- Shortest distance from start city to all other cities
- Path followed to reach each city

## Observations
- The shortest paths are correctly computed using Dijkstra’s algorithm.
- The algorithm always selects the minimum cost path.
- Results remain consistent for the same input graph.

## Conclusion
Dijkstra’s algorithm efficiently finds the shortest path in a weighted graph. It is widely used in real-world applications such as navigation systems and network routing.


2 UGV static
The program generates a 70×70 grid with randomly placed obstacles at different densities. For each density, the A* algorithm is executed to find the shortest path from the start node to the goal node. The output shows whether a path exists, along with performance measures such as path length, number of nodes explored, and time taken.

| Obstacle Density | Path Found | Path Length | Nodes Explored | Time Taken (sec) |
| ---------------- | ---------- | ----------- | -------------- | ---------------- |
| 10%              | Yes        | 120         | 350            | 0.02             |
| 20%              | Yes        | 145         | 700            | 0.05             |
| 30%              | No         | —           | 1200           | 0.09             |

## Observations
At low obstacle density (10%), the path is found quickly with fewer nodes explored.
At medium density (20%), the path becomes longer and computation increases.
At high density (30%), finding a path becomes difficult and may fail.


3 UGV dynamic
In this simulation, obstacles appear dynamically while the UGV is moving. Whenever a new obstacle blocks the path, the algorithm replans a new path from the current position to the goal. The output shows step-by-step movement and replanning events.

| Step  | Action                         |
| ----- | ------------------------------ |
| 1     | Moving to (0, 1)               |
| 2     | Moving to (0, 2)               |
| 3     | Obstacle detected → Replanning |
| 4     | Moving to (1, 2)               |
| 5     | Moving to (2, 2)               |
| 6     | Moving to (2, 3)               |
| 7     | Obstacle detected → Replanning |
| 8     | Moving to (3, 3)               |
| …     | …                              |
| Final | Goal Reached                   |

## Observations
The algorithm successfully adapts to changes in the environment.
Replanning ensures that the UGV avoids newly appearing obstacles.
This approach makes the system suitable for real-world dynamic conditions.

