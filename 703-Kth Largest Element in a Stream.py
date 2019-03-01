import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # 方法1
        # self.nums = sorted(nums)
        # self.k = k
        
        # 方法2，使用heapq模块
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > self.k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        # 方法1
        # self.nums += [val]
        # self.nums = sorted(self.nums)
        # return self.nums[-self.k]
        
        # 方法2
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
