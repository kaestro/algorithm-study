from collections import defaultdict

def beauty_of_tree(N,a,b,lst):

    def create_graph(graph, parent, lst, N):

        for i in range(len(lst)):
            graph[lst[i]].append(i+2)
            parent[i+2] = lst[i]

        return graph, parent



    def dfs(graph, parent, visits_a, visits_b, N, a, b):


        stack = []
        stack.append(1)
        visited = set()
        while stack:
            temp = stack.pop()
            i = 0
            n = temp
            while n > 0:
                if i % a == 0:
                    visits_a[n-1] += 1
                if i % b == 0:
                    visits_b[n-1] += 1
                i += 1
                n = parent[n]

            visited.add(temp)
            
            for v in graph[temp]:
                if v not in visited:
                    stack.append(v)


    def calculate_prob (visits_a, visits_b, N):
        prob = [0 for _ in range(N)]
        for i in range(N):
            visits_a[i] = visits_a[i]/N
            visits_b[i] = visits_b[i]/N
            prob[i] = visits_a[i]+visits_b[i] - visits_a[i]*visits_b[i]


        
        return sum(prob)

    graph = defaultdict(list)
    parent = defaultdict(int)
    create_graph(graph, parent, lst,N)

    visits_a = [0 for _ in range(N)]
    visits_b = [0 for _ in range(N)]

    dfs(graph,parent,visits_a, visits_b, N,a,b)
    return calculate_prob(visits_a,visits_b,N)


n = int(input())
for i in range(n):
    input1 = [int(x) for x in input().split()]
    input2 = [int(x) for x in input().split()]
    print("Case #{}: {}".format(i+1, beauty_of_tree(*input1, input2)))