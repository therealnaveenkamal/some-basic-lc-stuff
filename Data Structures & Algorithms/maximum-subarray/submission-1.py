class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = nums[0]

        for n in nums:
            curr = max(curr + n, n)
            max_sum = max(max_sum, curr)
        return max_sum
