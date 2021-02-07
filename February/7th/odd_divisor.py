# log(n) = log(2^x*k^y) = xlog(2) + xlog() 
import math

def odd_divisor(n):
    if not math.log2(n) % 1 == 0:
        print('YES')
    else:
        print('NO')


n = int(input())
for i in range(n):
    odd_divisor(int(input()))
    