import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    answer = 0
    N = int(sys.stdin.readline())
    S = list(map(int, sys.stdin.readline().split()))
    MAX = [0 for i in range(N)]

    MAX[0] = S[0]
    for i in range(1, N):
        MAX[i] = max(MAX[i - 1], S[i])
    
    # idx == 0
    if N == 1 or S[1] < S[0]:
        answer += 1
    
    for i in range(1, N-1):
        if S[i] > MAX[i-1] and S[i] > S[i + 1]:
            answer += 1
    
    # idx == N-1
    if S[N-1] > MAX[N-2]:
        answer += 1

    print("Case #" + str(t) + ": " + str(answer))
