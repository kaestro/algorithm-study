import math
# import Counter
 
def strange_beauty(lst):
    # d = Counter(lst)

    lcm = lst[0]
    result = 0
    for i in range(1,len(lst)):
        new_lcm = int(lcm * lst[i]/math.gcd(lcm,lst[i]))
 
        if new_lcm == lst[i]:
            None
        elif lcm != new_lcm:
            # result += d[lst[i]]
            result += 1
        lcm = new_lcm
    return result
 
 
 
 
n = int(input())
for i in range(n):
    input1 = int(input())
    input2 = [int(x) for x in input().split()]
    print(strange_beauty(input2))
