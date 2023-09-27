import heapq
import math

class DijkstraAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)
        self.distances = [math.inf] * self.num_vertices
        self.previous_vertices = [-1] * self.num_vertices

    def find_shortest_path(self, start, end):
        self.distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > self.distances[current_vertex]:
                continue

            for neighbor, weight in enumerate(self.graph[current_vertex]):
                if weight > 0:
                    distance = current_distance + weight
                    if distance < self.distances[neighbor]:
                        self.distances[neighbor] = distance
                        self.previous_vertices[neighbor] = current_vertex
                        heapq.heappush(priority_queue, (distance, neighbor))

        return self._shortest_path(start, end)

    def _shortest_path(self, start, end):
        path = []
        while end != -1:
            path.append(end)
            end = self.previous_vertices[end]
        return list(reversed(path))

# Пример использования:
D = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))

dijkstra = DijkstraAlgorithm(D)
start_vertex = 0
end_vertex = 4
shortest_path = dijkstra.find_shortest_path(start_vertex, end_vertex)
print(shortest_path)