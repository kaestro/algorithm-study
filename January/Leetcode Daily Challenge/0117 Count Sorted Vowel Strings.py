class Solution:
    def countVowelStrings(self, n: int) -> int:
        S = [1, 1, 1, 1, 1]
        for i in range(1, n):
            for j in range(1, 5):
                S[j] += S[j-1]
        return sum(S)
