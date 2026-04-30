class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        min_lr = [0]*len(height)
        max_ = 0
        for i in range(len(height)):
            max_left[i] = max_
            max_ = max(max_, height[i])
        
        max_ = 0
        for i in range(len(height)-1, -1, -1):
            trap = min(max_, max_left[i])-height[i]
            min_lr[i] = trap if trap > 0 else 0
            max_ = max(max_, height[i])
        
        return sum(min_lr)