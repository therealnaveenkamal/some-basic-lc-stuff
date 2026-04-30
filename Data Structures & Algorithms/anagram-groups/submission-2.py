class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for elem in strs:
            a = "".join(sorted(elem))
            if a in hm:
                hm[a].append(elem)
            else:
                hm[a] = [elem]

        return list(hm.values())