from collections import deque

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        q = deque()
        S = [0 for i in range(n+1)]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        S[1] = 1
        S[2] = 1
        q.append(2)
        while len(q) > 0:
            num = q.popleft()
            if 2*num-1 <= n:
                S[2*num-1] = S[num] + S[num-1]
                q.append(2*num-1)
            if 2*num <= n:
                S[2*num] = S[num]
                q.append(2*num)
        return max(S)
