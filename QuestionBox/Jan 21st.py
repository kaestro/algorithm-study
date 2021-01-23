#https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3611/
from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = ''.join([str(nums[i]) for i in range(k)])

        for i in range(1, len(nums)-k+1):
            temp = ''.join([str(nums[j]) for j in range(i, i+k)])
            res = min(res, temp)

        return [int(ch) for ch in res]


if __name__ == "__main__":
    sol = Solution()
    nums = [3,5,2,6]
    k = 2
    sol.mostCompetitive(nums, k)