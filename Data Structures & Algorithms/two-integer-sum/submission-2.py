class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Naive way is to sum all the pairs and check. O(n2)
        # Goal: A+B=target
        # Optimal way is to hash the seen numbers As and check for
        # target-A is seen already.

        hm = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hm:
                return [hm[a], i]
            else:
                hm[nums[i]] = i
        return [-1, -1]
