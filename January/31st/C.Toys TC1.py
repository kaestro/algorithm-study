from copy import deepcopy

def backtrack(N, sets:list):
    if N == -1:
        return
    
    nextSets = [[N] + st for st in sets]
    sets += nextSets
    backtrack(N-1, sets)


def solution(T):
    N = int(input())
    sets = [[]]
    backtrack(N-1, sets)
    
    sets.sort(key=len, reverse=True)
    sets.pop()

    enjoys, remems = [0] * N, [0] * N
    for i in range(N):
        enjoys[i], remems[i] = map(int, input().split())
    
    ans = "INDEFINITELY"
    maxTime, Y = 0, 0
    for st in sets:
        enjoyTotal = 0
        for i in st:
            enjoyTotal += enjoys[i]
        
        curTime = enjoyTotal
        for i in st:
            if enjoyTotal >= enjoys[i] + remems[i]:
                curTime += enjoys[i]
            else:
                break
        
        if curTime == 2 * enjoyTotal:
            maxTime = 'INDEFINITELY'
            Y = N - len(st)
            break
        elif maxTime < curTime:
            maxTime = curTime
            Y = N - len(st)

    print("Case #{}: {} {}".format(T, Y, maxTime))



if __name__ == "__main__":
    T = int(input())
    for testCase in range(1, T+1):
        solution(testCase)