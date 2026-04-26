class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        seen = {}
        max_ = 0
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        seen[s[0]]=1

        while j<len(s):
            
            if s[j] not in seen or (s[j] in seen and seen[s[j]]==0):
                seen[s[j]]=1
                max_ = max(max_, j-i+1)
                j+=1
            else:
                seen[s[i]]=0
                i+=1
        return max_

