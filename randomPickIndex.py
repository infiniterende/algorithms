from collections import defaultdict
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.hashmap = defaultdict(list)
        for i, num in enumerate(nums):
            self.hashmap[num].append(i)

    def pick(self, target: int) -> int:
        rand = random.random()
        # random = 0.9 * 3 2.7
        indices = self.hashmap[target]
        size = len(indices)
        randomIndex = floor(rand * size)
        return indices[randomIndex]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
