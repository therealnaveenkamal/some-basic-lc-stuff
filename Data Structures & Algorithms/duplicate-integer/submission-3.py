class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = set()
        for e in nums:
            if e in hm:
                return True
            else:
                hm.add(e)
        return False