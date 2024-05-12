class Solution:
    def validAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            if s[i] in countS:
                countS = 1 + countS.get(s[i], 0)
                countT = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
            
                return False
        return True

solution = Solution()
s = "anagram"
t = "nagaram"
print(solution.validAnagram(s,t))