class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)-2):
            tmp = s[i:i+3]
            if len(set(tmp)) == 3:
                c+=1
        return c