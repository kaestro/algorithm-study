import sys
 
t = int(sys.stdin.readline())
for T in range(t):
    n = int(sys.stdin.readline())    
    q = n // 2020
    if n <= 2020*q+q:
        print("YES")
    else:
        print("NO")