class Solution:
    def isValid(self, s: str) -> bool:
        cnt = [0, 0, 0]
        lastBracket = []
        for i in range(len(s)):
            if s[i] == '(':
                cnt[0] += 1
                lastBracket.append(0)
            elif s[i] == ')':
                if cnt[0] <= 0 or lastBracket[-1] != 0:
                    return False
                cnt[0] -= 1
                lastBracket.pop()
            elif s[i] == '[':
                cnt[1] += 1
                lastBracket.append(1)
            elif s[i] == ']':
                if cnt[1] <= 0 or lastBracket[-1] != 1:
                    return False
                cnt[1] -= 1
                lastBracket.pop()
            elif s[i] == '{':
                cnt[2] += 1
                lastBracket.append(2)
            else: # s[i] == '}'
                if cnt[2] <= 0 or lastBracket[-1] != 2:
                    return False
                cnt[2] -= 1
                lastBracket.pop()
        if sum(cnt) > 0:
            return False
        else:
            return True
