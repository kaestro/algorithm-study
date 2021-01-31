import sys

t = int(sys.stdin.readline())
for T in range(t):
    n = int(sys.stdin.readline())    
    if n & 1 > 0: # if n is odd
        print("YES")
    else: # if n is even
        if n & (n-1) == 0:
            print("NO")
        else:
            print("YES")