from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        N = len(nums)
        L, R = 0, 0
        num, preNum = 0, 0
        curLen, preLen = 0, 0
        answer = 0
        nums.sort()

        while R < N and nums[R] == nums[L]:
            R += 1
        preNum = nums[L]
        preLen = R - L
        L = R

        while L < N:
            num = nums[L]
            R = L
            while R < N and nums[R] == num:
                R += 1
            curLen = R - L
            if num - preNum == 1:
                answer = max(answer, curLen + preLen)
            
            L = R
            preNum = num
            preLen = curLen
        return answer