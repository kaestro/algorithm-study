def record_breaker(lst):
    maximum = 0
    result = 0
    for i in range(len(lst)):
        if lst[i] > maximum and (i == len(lst)-1 or lst[i] > lst[i+1]):
            result += 1
        maximum = max(maximum, lst[i])
    return result

n = int(input())
for i in range(n):
    input1 = [int(x) for x in input().split()]
    input2 = [int(x) for x in input().split()]
    print("Case #{}: {}".format(i+1, record_breaker(input2)))