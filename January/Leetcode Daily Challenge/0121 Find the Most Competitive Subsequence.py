import heapq

class Solution:
    def mostCompetitive(self, nums:list, k:int) -> list:
        n = len(nums)
        S = []
        for i in range(n-k+1):
            S.append((nums[i], i))
        heapq.heapify(S)
        answer = []
        lastIdx = 0

        while True:
            val, idx = heapq.heappop(S)
            while idx < lastIdx:
                val, idx = heapq.heappop(S)
            answer.append(val)
            lastIdx = idx
            k -= 1
            if k == 0:
                break
            heapq.heappush(S, (nums[n-k], n-k))
        return answer
