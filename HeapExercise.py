import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # max-heap (store as negatives)
        self.right = []  # min-heap
    def addNum(self, num):
        heapq.heappush(self.left, -num)
        # Balance heaps
        if self.left and self.right and (-self.left[0] > self.right[0]):
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2

mf = MedianFinder()
for n in [5, 15, 1, 3]:
    mf.addNum(n)
    print("Median:", mf.findMedian())
