import sys

T = int(sys.stdin.readline())

def getNextNode(nodes:list, idx:int, curStep:int, tarStep:int,) -> int:
    if curStep == tarStep or idx == 0:
        return idx
    return getNextNode(nodes, nodes[idx], curStep+1, tarStep)

for t in range(1, T+1):
    N, A, B = map(int, sys.stdin.readline().split())
    info = list(map(int, sys.stdin.readline().split()))
    
    nodes = [0 for i in range(N+1)]
    for i in range(len(info)):
        nodes[i+2] = info[i]
    
    pA = [1 for i in range(N+1)] # A가 i번째 노드를 칠하는 경우의 수
    pB = [1 for i in range(N+1)] # B가 i번째 노드를 칠하는 경우의 수
    P = [0 for i in range(N+1)] # i번 노드가 칠해지는 확률

    for i in range(N, 0, -1):
        nextNode = getNextNode(nodes, i, 0, A)
        pA[nextNode] += pA[i]

        nextNode = getNextNode(nodes, i, 0, B)
        pB[nextNode] += pB[i]

        P[i] = (pA[i] / N) + (pB[i] / N) - (pA[i]*pB[i] / (N*N))

    answer = sum(P[1:])
    print("Case #" + str(t) + ": " + str(answer))
