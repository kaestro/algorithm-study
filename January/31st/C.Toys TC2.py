import heapq


def solution(T):
    N = int(input())
    
    enjoys, remems = [0] * N, [0] * N
    enjoysTotal = 0
    for i in range(N):
        enjoys[i], remems[i] = map(int, input().split())
        enjoysTotal += enjoys[i]

    maxTime, curTime = enjoysTotal, enjoysTotal
    minRemoved, curRemoved = 0, 0
    pq = []
    for i in range(N):
        curTime += enjoys[i]
        heapq.heappush(pq, (-(enjoys[i] + remems[i]), i))

        while len(pq) > 0:
            topSum, topIdx = -pq[0][0], pq[0][1]
            if topSum > enjoysTotal:
                curTime -= 2 * enjoys[topIdx]
                enjoysTotal -= enjoys[topIdx]
                curRemoved += 1
                heapq.heappop(pq)
            else:
                break

        if curTime > maxTime:
            maxTime, minRemoved = curTime, curRemoved
        elif curTime == maxTime:
            minRemoved = min(minRemoved, curRemoved)

    if len(pq) != 0:
        maxTime = "INDEFINITELY"
        minRemoved = curRemoved


    print("Case #{}: {} {}".format(T, minRemoved, maxTime))



if __name__ == "__main__":
    T = int(input())
    for testCase in range(1, T+1):
        solution(testCase)