class Solution:
    def kLengthApart(self, nums:list, k: int) -> bool:
        idx = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                idx = i
                break
        if idx == -1:
            return True
        
        for i in range(idx+1, len(nums)):
            if nums[i] == 1:
                if i - idx <= k:
                    return False
                idx = i
        return True