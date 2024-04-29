class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for c in s:
            if c in dic:
                dic[c] = dic[c] + 1
            else:
                dic[c] = 1
        
        for r in t:
            if r in dic and not(dic[r] < 1):
                dic[r] = dic[r] - 1
                continue
            else:
                return False
        
        for key in dic:
            if dic[key] > 0:
                return False
                
        return True