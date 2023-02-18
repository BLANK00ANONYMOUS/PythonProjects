from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefSum = []
        su = 0
        for num in nums:
            su += num
            self.prefSum.append(su)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            ls = self.prefSum[left - 1]
        else:
            ls = 0

        return self.prefSum[right] - ls

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)