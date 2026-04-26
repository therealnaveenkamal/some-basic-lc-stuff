class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        max_cons = 1
        j=1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]+1:
                j+=1
                max_cons = max(max_cons, j)
            else:
                j=1

        return max_cons