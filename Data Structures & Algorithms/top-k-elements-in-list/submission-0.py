from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for elem in nums:
            hm[elem] = hm.get(elem, 0)+1
        return sorted(hm, key=hm.get, reverse=True)[:k]