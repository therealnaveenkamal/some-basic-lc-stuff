class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        f = []
        seen = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
                low, high = i+1, len(nums)-1
                while low<high:
                    s = nums[low] + nums[high]
                    if s == -nums[i]:
                        elem = [nums[i], nums[low], nums[high]]
                        if elem not in f:
                            f.append(elem)
                        low+=1
                        high-=1
                    elif s > -nums[i]:
                        high -= 1
                    elif s < -nums[i]:
                        low += 1
        return f

