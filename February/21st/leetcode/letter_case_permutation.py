class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = set()
        
        self.helper(S, 0, result)
        return list(result)
        
        
    def helper(self, s,i, result):
        # arr.add(s)
        n = len(s)
        if i == n:
            return
        
        if s[i].isalpha():
            s1 = s[:i]+ s[i].lower() + s[i+1:]
            s2 = s[:i]+ s[i].upper() + s[i+1:]
            result.add(s1)
            result.add(s2)
            self.helper(s1,i+1,result)
            self.helper(s2,i+1,result)
        else:
            self.helper(s,i+1,result)
            result.add(s)

        