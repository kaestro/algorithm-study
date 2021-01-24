
def alien_piano(lst):
    result = 0


    up = 0
    down = 0

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            up += 1
            down = 0
        elif lst[i] < lst[i - 1]:
            down += 1
            up = 0
        if up > 3 or down > 3:
            result += 1
            up = 0
            down = 0
    return result
    

n = int(input())
for i in range(n):
    input1 = [int(x) for x in input().split()]
    input2 = [int(x) for x in input().split()]
    print("Case #{}: {}".format(i+1, alien_piano(input2)))