# 2025-01-19 Taken from editorial 437, for which
# this is a sub-problem
from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)

        count = 0
        psum = 0
        for num in nums:
            psum += num

            if psum == k:
                count += 1

            count += h[psum - k]
            h[psum] += 1

        return count
