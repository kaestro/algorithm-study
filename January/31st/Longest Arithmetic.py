import sys

T = int(sys.stdin.readline())
for t in range(1, T+1):
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    diff, l = 1e9+1, 1
    longest = 0
    for i in range(1, N):
        if diff == A[i]-A[i-1]:
            l += 1
        else:
            diff = A[i]-A[i-1]
            longest = max(longest, l+1)
            l = 1
    longest = max(longest, l+1)
    print("Case #" + str(t) + ": " + str(longest))
