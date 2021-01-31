from math import log2

class Solution:
    def concatenatedBinary(self, n:int) -> int:
        S = [0 for i in range(n+1)]
        M = 1000000007
        for i in range(1, n+1):
            S[i] = (S[i-1] << int(log2(i)+1)) + i
            S[i] %= M
        return S[n]