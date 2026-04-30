class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hm = {}
        for e in s:
            hm[e] = hm.get(e, 0) + 1
        
        for e in t:
            if e not in hm:
                return False
            hm[e] -=1

            if hm[e] == 0:
                del hm[e]
        return not hm

        
