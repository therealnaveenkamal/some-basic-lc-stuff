import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heaped = nums
        heapq.heapify(self.heaped)
        self.k = k
        while len(nums)>k:
            heapq.heappop(self.heaped)

    def add(self, val: int) -> int:
        heapq.heappush(self.heaped, val)

        while len(self.heaped)>self.k:
            heapq.heappop(self.heaped)
        return self.heaped[0]
    
