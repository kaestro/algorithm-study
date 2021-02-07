from collections import Counter
from math import comb
def advertising_agency (lst, k):
    s = set(lst)
    s = list(s)
    s.sort()
    s = s[::-1]

    d = Counter(lst)
    result = 1
    i = 0

    print(d)
    print(s)
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

