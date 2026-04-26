class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # a + b = target
        # Goal is to find a number in a hashmap. If we've already seen, target-a, then we have a solution

        hm = {}
        for i in range(len(nums)):
            a = nums[i]
            if target - a in hm:
                return [hm[target-a], i]
            else:
                hm[a] = i
