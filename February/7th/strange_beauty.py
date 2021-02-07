import math
from collections import Counter

def strange_beauty(lst):

    d = Counter(lst)
    lst = list(set(lst))
    lcm = lst[0]
    result = 0
    print(lst)
    for i in range(1,len(lst)):
        new_lcm = int(lcm * lst[i]/math.gcd(lcm,lst[i]))
        print('lcm', new_lcm)
        if lcm != new_lcm:
            result += d[lst[i]]
        lcm = new_lcm
        print(result)
    return result




n = int(input())
for i in range(n):
    input1 = int(input())
    input2 = [int(x) for x in input().split()]
    print(strange_beauty(input2))
