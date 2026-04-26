class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_ = 0
        while i < j:
            max_ = max(max_, (j-i)*min(heights[i], heights[j]))
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_