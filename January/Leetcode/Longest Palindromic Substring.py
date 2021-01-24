class Solution:    
    def longestPalindrome(self, s: str) -> str:
        answer = [0, 0]
        # when len is odd
        for mid in range(len(s)):
            L, R = mid-1, mid+1
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if answer[1]-answer[0] < R - L:
                        answer[0], answer[1] = L, R
                    L -= 1
                    R += 1
                else:
                    break

        # when len is even
        for L in range(len(s)-1):
            R = L + 1
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if answer[1] - answer[0] < R - L:
                        answer[0], answer[1] = L, R
                    L -= 1
                    R += 1
                else:
                    break
        return s[answer[0]:answer[1]+1]
