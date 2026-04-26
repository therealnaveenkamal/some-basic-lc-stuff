from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)
        for elem in s_count:
            if elem not in t_count or t_count[elem] != s_count[elem]:
                return False
        return True