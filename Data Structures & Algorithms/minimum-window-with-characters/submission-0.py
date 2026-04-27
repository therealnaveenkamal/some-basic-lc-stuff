from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        l = 0
        r = 0
        broke=0
        lchar = None
        while r<=len(s):
            broke=0
            s_count = Counter(s[l:r])
            for elem in t_count:
                if elem not in s_count or s_count[elem] < t_count[elem]:
                    r+=1
                    broke=1
                    break
            if broke==0:
                if lchar is None or len(lchar)>len(s[l:r]):
                    lchar=s[l:r]
                l+=1
        if lchar:
            return lchar
        else:
            return ""
