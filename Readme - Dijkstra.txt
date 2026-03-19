1. Dijkstra’s Algorithm (Uniform Cost Search)

In this part of the assignment, the main goal is to understand how to find the shortest path between cities when the distances between them are different. In real life, when we travel from one city to another, there are multiple routes available, and each route has a different distance. So naturally, we would prefer the route that takes the least distance or cost. This is exactly the problem that Dijkstra’s algorithm solves.

Dijkstra’s algorithm works in a very logical and step-by-step way. First, we assume that the distance from the starting city to itself is zero, and to all other cities is infinity. Then, we keep selecting the city which currently has the smallest known distance. From that city, we check all its neighboring cities and update their distances if we find a shorter path through the current city. This process continues until we have calculated the shortest distances to all cities.

In this assignment, I represented Indian cities as nodes in a graph and the roads between them as edges with weights (distances). Using a priority queue, I ensured that at each step, the city with the smallest distance is selected first. This makes the algorithm efficient and accurate. In Artificial Intelligence, this method is also called Uniform Cost Search because it always expands the path with the least cost first.

Overall, this part helped me understand how real-world navigation systems like Google Maps calculate the shortest routes between locations.