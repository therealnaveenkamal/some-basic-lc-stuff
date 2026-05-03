class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for elem in strs:
            count = [0]*26
            for c in elem:
                count[ord(c)-ord('a')]+=1
            key = tuple(count)
            if key not in hm:
                hm[key] = []
            hm[key].append(elem)
        return list(hm.values())

