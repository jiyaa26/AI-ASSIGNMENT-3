2. UGV Navigation with Static Obstacles

In the second part, the problem becomes more practical and interesting. Here, we imagine a robot called an Unmanned Ground Vehicle (UGV) that needs to move from a starting point to a goal point in a battlefield. The entire area is represented as a 70×70 grid, where each cell represents a position the robot can move to. Some of these cells contain obstacles, which means the robot cannot pass through them.

The key challenge here is to find the shortest path from the start to the goal while avoiding all the obstacles. Since the obstacles are already known and do not change, this is called a static environment. To solve this problem efficiently, I used the A* (A-star) algorithm.

A* is an intelligent pathfinding algorithm that not only considers the distance traveled so far but also estimates how far the goal is. It combines these two values to decide the best path at each step. This makes it faster and more efficient than basic algorithms like Dijkstra in grid-based problems.

In the implementation, I created a grid and randomly placed obstacles with different densities such as 10%, 20%, and 30%. Then I applied the A* algorithm to find the path. I also evaluated the performance using measures like path length, number of nodes explored, and time taken. I observed that when the obstacle density is low, the path is found quickly, but as the density increases, the problem becomes more complex and sometimes no path exists.

This part gave me a clear understanding of how robots or autonomous vehicles navigate in environments where obstacles are known in advance.