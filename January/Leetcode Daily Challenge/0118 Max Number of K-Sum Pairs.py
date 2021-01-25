class Solution:
    def maxOperations(self, nums:list, k:int) -> int:
        nums.sort()
        answer = 0
        L, R = 0, len(nums)-1
        while L < R:
            if nums[L] + nums[R] == k:
                L += 1
                R -= 1
                answer += 1
            elif nums[L] + nums[R] < k:
                L += 1
            else:
                R -= 1
        return answer
