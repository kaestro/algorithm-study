class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        for i in range(32):
            if n & 1 > 0:
                answer += 1
            n >>= 1
        return answer