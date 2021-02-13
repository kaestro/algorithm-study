from collections import Counter
from math import comb

# [1, 3, 3, 2, 2, 1, 1]
def advertising_agency (lst, k):
    s = list(set(lst))
    s.sort()
    s = s[::-1]

# [3,2,1]

    d = Counter(lst)
    result = 1
    i = 0
# 1: 3, 2: 2, 3: 2
# k = 2
    while k > 0:
        n = d[s[i]]
        if k >= n:
            k -= n
        else:
            result *= comb(n,k)
            k = 0
        i += 1

    return result % (10**9+7)



n = int(input())
for i in range(n):
    input1 = [int(x) for x in input().split()]
    input2 = [int(x) for x in input().split()]
    print(advertising_agency(input2,input1[1]))

