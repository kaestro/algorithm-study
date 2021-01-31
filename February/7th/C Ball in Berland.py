import sys
from bisect import bisect_left, bisect_right

t = int(sys.stdin.readline())
for T in range(t):
    a, b, k = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    K = []
    for i in range(k):
        K.append((A[i], B[i]))
    A.sort()
    B.sort()

    answer = 0
    for boy, girl in K:
        cntBoy = bisect_right(A, boy) - bisect_left(A, boy)
        cntGirl = bisect_right(B, girl) - bisect_left(B, girl)
        answer += k - cntBoy - cntGirl + 1
    answer //= 2
    print(answer)