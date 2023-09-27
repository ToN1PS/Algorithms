import math

class ShortestPathFinder:
    def __init__(self, graph):
        self.graph = graph
        self.N = len(graph)
        self.P = [[-1 for _ in range(self.N)] for _ in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                if i != j and self.graph[i][j] != math.inf:
                    self.P[i][j] = i
    
    def find_shortest_path(self, start, end):
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    if self.graph[i][j] > self.graph[i][k] + self.graph[k][j]:
                        self.graph[i][j] = self.graph[i][k] + self.graph[k][j]
                        self.P[i][j] = self.P[k][j]
        
        return self._reconstruct_path(start, end)
    
    def _reconstruct_path(self, start, end):
        if self.P[start][end] == -1:
            return None  # No path exists
        path = [end]
        while end != start:
            end = self.P[start][end]
            path.append(end)
        return list(reversed(path))

# Граф задан в виде двумерного списка
V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
     [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
     [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
     [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
     [10, math.inf, 3, 8, math.inf, math.inf, 1, 0]]

# Создаем экземпляр класса ShortestPathFinder
path_finder = ShortestPathFinder(V)

# Находим кратчайший путь между вершинами start и end
start = 0
end = 7
shortest_path = path_finder.find_shortest_path(start, end)
print(shortest_path)
