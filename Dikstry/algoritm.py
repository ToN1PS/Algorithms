import math

class DijkstraAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)
        self.distances = [math.inf] * self.num_vertices
        self.visited = set()
        self.previous_vertices = [-1] * self.num_vertices

    def find_shortest_path(self, start, end):
        self.distances[start] = 0

        while self.visited != set(range(self.num_vertices)):
            current_vertex = self._min_distance_vertex()
            if current_vertex == -1:
                break
            self.visited.add(current_vertex)

            for neighbor, weight in enumerate(self.graph[current_vertex]):
                if weight > 0 and neighbor not in self.visited:
                    new_distance = self.distances[current_vertex] + weight
                    if new_distance < self.distances[neighbor]:
                        self.distances[neighbor] = new_distance
                        self.previous_vertices[neighbor] = current_vertex

        return self._shortest_path(start, end)

    def _min_distance_vertex(self):
        min_distance = math.inf
        min_vertex = -1
        for vertex, distance in enumerate(self.distances):
            if distance < min_distance and vertex not in self.visited:
                min_distance = distance
                min_vertex = vertex
        return min_vertex

    def _shortest_path(self, start, end):
        path = [end]
        while path[-1] != start:
            path.append(self.previous_vertices[path[-1]])
        path.reverse()
        return path

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
