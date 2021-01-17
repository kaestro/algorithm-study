import sys
T = int(sys.stdin.readline())

for t in range(1, T+1):
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    answer = 0
    def countDown(idx:int) -> int:
        global answer, N, A
        for i in range(idx, idx + K):
            if A[i] != (K - i + idx):
                return i
        answer += 1
        return i + 1

    i = 0
    while i <= N - K:
        if A[i] == K:
            i = countDown(i)
        else:
            i += 1
    print("Case #" + str(t) + ": " + str(answer))
