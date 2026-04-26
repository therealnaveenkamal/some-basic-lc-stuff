class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        for i in range(len(nums)-1):
            prefix.append(nums[i] * prefix[-1])
        
        for i in range(len(nums)-1, 0, -1):
            suffix.append(suffix[-1]*nums[i])
        
        f = []
        suffix = suffix[::-1]
        for i in range(len(nums)):
            f.append(prefix[i]*suffix[i])
        return f
    