import sys
from math import ceil

T = int(sys.stdin.readline())
for t in range(1, T+1):
    N, X = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    ll = []
    for i in range(N):
        ll.append((ceil(A[i]/X), i))
    ll.sort(key=lambda x:x[0])
    print("Case #" + str(t) + ": ", end = '')
    for i in range(N):
        print(str(ll[i][1]+1), end = ' ')
    print('')
