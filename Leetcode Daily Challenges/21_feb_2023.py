from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if ((mid - 1 < 0 or nums[mid - 1] != nums[mid]) and
                    (mid + 1 == n or nums[mid] != nums[mid + 1])):
                return nums[mid]

            leftSz = mid - 1 if nums[mid - 1] == nums[mid] else mid
            if leftSz % 2:
                hi = mid - 1
            else:
                lo = mid + 1

        return