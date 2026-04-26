class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for elem in strs:
            sort_a = ''.join(sorted(elem))
            if sort_a not in hm:
                hm[sort_a] = []
            hm[sort_a].append(elem)
        return list(hm.values())