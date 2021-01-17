import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    answer = 0

    cnt = dict()
    cnt.update({0:1})
    Sum = 0
    minSum = 0
    for i in range(N):
        j = 0
        Sum += A[i]
        minSum = min(Sum, minSum)
        while Sum - j*j >= minSum:
            if cnt.__contains__(Sum - j*j):
                answer += cnt[Sum-j*j]
            j += 1
            
        cnt.setdefault(Sum, 0)
        cnt[Sum] += 1

    print("Case #" + str(t) + ": " + str(answer))
