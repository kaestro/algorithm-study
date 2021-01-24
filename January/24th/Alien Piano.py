import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    K = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    
    DP = [[0, 0, 0, 0] for i in range(K)]
    for i in range(1, K):
        if A[i] > A[i-1]:
            DP[i][0] = min(DP[i-1][0]+1, DP[i-1][1]+1, DP[i-1][2]+1, DP[i-1][3]+1)
            DP[i][1] = min(DP[i-1][0], DP[i-1][1]+1, DP[i-1][2]+1, DP[i-1][3]+1)
            DP[i][2] = min(DP[i-1][0], DP[i-1][1], DP[i-1][2]+1, DP[i-1][3]+1)
            DP[i][3] = min(DP[i-1][0], DP[i-1][1], DP[i-1][2], DP[i-1][3]+1)
        elif A[i] < A[i-1]:
            DP[i][0] = min(DP[i-1][0]+1, DP[i-1][1], DP[i-1][2], DP[i-1][3])
            DP[i][1] = min(DP[i-1][0]+1, DP[i-1][1]+1, DP[i-1][2], DP[i-1][3])
            DP[i][2] = min(DP[i-1][0]+1, DP[i-1][1]+1, DP[i-1][2]+1, DP[i-1][3])
            DP[i][3] = min(DP[i-1][0]+1, DP[i-1][1]+1, DP[i-1][2]+1, DP[i-1][3]+1)
        else:
            DP[i][0] = min(DP[i-1][0], DP[i-1][1]+1, DP[i-1][2]+1, DP[i-1][3]+1)
            DP[i][1] = min(DP[i-1][0]+1, DP[i-1][1], DP[i-1][2]+1, DP[i-1][3]+1)
            DP[i][2] = min(DP[i-1][0]+1, DP[i-1][1]+1, DP[i-1][2], DP[i-1][3]+1)
            DP[i][3] = min(DP[i-1][0]+1, DP[i-1][1]+1, DP[i-1][2]+1, DP[i-1][3])
    answer = min(DP[K-1])
    print("Case #" + str(t) + ": " + str(answer))
