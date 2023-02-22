from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        res = hi

        def good(x):
            n, curr = 1, x
            for w in weights:
                if curr - w < 0:
                    n += 1
                    curr = x
                curr -= w
            return n <= days

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if good(mid):
                res = min(res, mid)
                hi = mid - 1
            else:
                lo = mid + 1

        return res