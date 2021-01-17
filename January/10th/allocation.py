import heapq

def allocate (lst, B):
    heapq.heapify(lst)
    result = 0
    for i in range(len(lst)):
        B -= heapq.heappop(lst)
        if B >= 0:
            result += 1
        else:
            break

    return result

n = int(input())
for i in range(n):
    input1 = [int(x) for x in input().split()]
    input2 = [int(x) for x in input().split()]
    print("Case #{}: {}".format(i+1,allocate (input2, input1[1])))
