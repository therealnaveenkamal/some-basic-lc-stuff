class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        
        for arr in strs:
            a = "".join(sorted(arr))
            if a in hm:
                hm[a].append(arr)
            else:
                hm[a] = [arr]
        return list(hm.values())