import heapq

def dijkstra(graph, start):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    previous = {city: None for city in graph}
    
    pq = [(0, start)]

    while pq:
        current_distance, current_city = heapq.heappop(pq)

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous


# Sample India cities graph
graph = {
    "Delhi": {"Jaipur": 280, "Lucknow": 550},
    "Jaipur": {"Delhi": 280, "Ahmedabad": 670},
    "Lucknow": {"Delhi": 550, "Patna": 600},
    "Ahmedabad": {"Jaipur": 670},
    "Patna": {"Lucknow": 600}
}

start = "Delhi"
distances, previous = dijkstra(graph, start)

print("Shortest distances:", distances)
