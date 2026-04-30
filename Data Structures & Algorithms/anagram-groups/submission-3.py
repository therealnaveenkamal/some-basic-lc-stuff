class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Complexity: O(n * k log k)
        # k = len(word)
        # hm = {}
        # for elem in strs:
        #     a = "".join(sorted(elem))
        #     if a in hm:
        #         hm[a].append(elem)
        #     else:
        #         hm[a] = [elem]

        # return list(hm.values())

        hm = {}
        for elem in strs:
            count = [0]*26
            for c in elem:
                count[ord(c)-ord('a')]+=1
            key = tuple(count)
            if key not in hm:
                hm[key] = [elem]
            else:
                hm[key].append(elem)
        return list(hm.values())