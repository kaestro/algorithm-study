from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = []
    
    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
    
    def addEdge(self, u, v):
        if u == v:
            return

        if v not in self.graph[u]:
            self.graph[u].append(v)
    
    def topologicalSortUtilIsCyclic(self, vertex, visited:dict, stack:list, recStack:dict, parent):
        visited[vertex] = True
        recStack[vertex] = True

        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                if self.topologicalSortUtilIsCyclic(neighbor, visited, stack, recStack, vertex):
                    return True
            elif recStack[neighbor] == True:
                return True

        stack.append(vertex)
        recStack[vertex] = False
        return False

    def topologicalSort(self):
        visited = {v:False for v in self.vertices}
        recStack = {v:False for v in self.vertices}
        stack = []

        for vertex in self.vertices:
            if not visited[vertex]:
                isCyclic = self.topologicalSortUtilIsCyclic(vertex, visited, stack, recStack, '0')
            if isCyclic:
                return '-1'

        return ''.join(stack[::-1])



if __name__ == "__main__":
    T = int(input())
    for i in range(1, T+1):
        R, C = map(int, input().split())
        rows = []
        for _ in range(R):
            rows.append(input())
        rows = rows[::-1]

        graph = Graph()
        
        for col in range(C):
            for row in range(R):
                graph.addVertex(rows[row][col])

                if row == R - 1:
                    continue
                
                graph.addEdge(rows[row][col], rows[row+1][col])
        
        res = graph.topologicalSort()
        print("Case #{}: {}".format(i, res))
