import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.set = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.set.remove(smallest)
            return smallest
        else:
            smallest = self.current
            self.current += 1
            return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)

# Example usage:
smallestInfiniteSet = SmallestInfiniteSet()
print(smallestInfiniteSet.popSmallest()) # returns 1
smallestInfiniteSet.addBack(2)
print(smallestInfiniteSet.popSmallest()) # returns 2
print(smallestInfiniteSet.popSmallest()) # returns 3
smallestInfiniteSet.addBack(1)
print(smallestInfiniteSet.popSmallest()) # returns 1
print(smallestInfiniteSet.popSmallest()) # returns 4
print(smallestInfiniteSet.popSmallest()) # returns 5
