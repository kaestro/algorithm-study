import sys
import heapq
 
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    
    if sum(a) < m:
        print(-1)
        continue
 
    pq1, pq2 = [], []
    for i in range(n):
        if b[i] == 1:
            heapq.heappush(pq1, -a[i])
        else:
            heapq.heappush(pq2, -a[i])
    
    answer = 0
    curMemory, curCost = 0, 0
    while len(pq1) >= 2 and len(pq2) >= 1:
        if curMemory - pq1[0] >= m:
            answer = curCost + 1
            break
        elif curMemory - pq2[0] >= m:
            answer = curCost + 2
            break
        
        temp = -heapq.heappop(pq1)
        if temp -pq1[0] <= -pq2[0]:
            curCost += 2
            curMemory += -heapq.heappop(pq2)
            heapq.heappush(pq1, -temp)
        else:
            curCost += 1
            curMemory += temp
    if curMemory >= m:
        answer = curCost
 
    if answer > 0:
        print(answer)
    else:
        if len(pq2) == 0:
            while curMemory < m:
                curMemory += -heapq.heappop(pq1)
                curCost += 1
            answer = curCost
        elif len(pq1) == 0:
            while curMemory < m:
                curMemory += -heapq.heappop(pq2)
                curCost += 2
            answer = curCost
        else:
            while curMemory < m:
                if curMemory - pq1[0] >= m:
                    curCost += 1
                    break
                if len(pq2) > 0:
                    curMemory += -heapq.heappop(pq2)
                    curCost += 2
            answer = curCost
        print(answer)