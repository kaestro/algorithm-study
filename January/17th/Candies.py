# Test Set1 : TL

import sys
from math import ceil, log2

Test = int(sys.stdin.readline())
for t in range(1, Test+1):
    N, Q = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    OP = [list(sys.stdin.readline().split()) for i in range(Q)]

    # generate SegmentTrees
    size = 1 << (ceil(log2(N))+1)
    T = [0 for i in range(size)]
    MT = [0 for i in range(size)]
    
    def getSign(idx:int) -> int:
        return -1 if idx&1>0 else 1

    def initT(start:int, end:int, node:int):
        if start==end:
            T[node] = A[start]*getSign(start)
            return T[node]
        mid = (start+end)//2
        T[node] = initT(start, mid, node*2) + initT(mid+1, end, node*2+1)
        return T[node]

    def initMT(start:int, end:int, node:int):
        if start==end:
            MT[node] = A[start] * getSign(start) * (start+1)
            return MT[node]
        mid = (start+end)//2
        MT[node] = initMT(start, mid, node*2) + initMT(mid+1, end, node*2+1)
        return MT[node]
    
    initT(0, len(A)-1, 1)
    initMT(0, len(A)-1, 1)

    def getSum(tree:list, L:int, R:int, start:int, end:int, node:int) -> int:
        if R < start or end < L:
            return 0
        elif L <= start and end <= R:
            return tree[node]
        else:
            mid = (start+end)//2
            return getSum(tree, L, R, start, mid, node*2) + getSum(tree, L, R, mid+1, end, node*2+1)

    def update(tree:list, idx:int, diff:int, start:int, end:int, node:int):
        if idx < start or end < idx:
            return
        else:
            tree[node] += diff
            if start == end:
                return
            mid = (start+end)//2
            update(tree, idx, diff, start, mid, node*2)
            update(tree, idx, diff, mid+1, end, node*2+1)

    score = 0
    for cmd in OP:
        if cmd[0] == 'Q':
            L, R = int(cmd[1])-1, int(cmd[2])-1
            sumT = getSum(T, L, R, 0, len(A)-1, 1)
            sumMT = getSum(MT, L, R, 0, len(A)-1, 1)
            score += (getSign(L) * (sumMT - sumT*L))
        else: # cmd[0] == 'U'
            idx, val = int(cmd[1])-1, int(cmd[2])
            diffT = getSign(idx) * (val-A[idx])
            diffMT = getSign(idx) * (val-A[idx]) * (idx+1)
            update(T, idx, diffT, 0, len(A)-1, 1)
            update(MT, idx, diffMT, 0, len(A)-1, 1)
            A[idx] = val
    
    print("Case #" + str(t) + ": " + str(score))
