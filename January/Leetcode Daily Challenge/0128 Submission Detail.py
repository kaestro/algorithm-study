class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        answer = [0 for i in range(n)]
        l = n
        while n > 0:
            temp = k - 26 * (n-1)
            if temp <= 1:
                answer[l-n] = 1
                k -= 1
            else:
                answer[l-n] = temp
                k -= temp
            n -= 1
        for i in range(l):
            answer[i] = chr(ord('a') + answer[i] - 1)
        return ''.join(answer)