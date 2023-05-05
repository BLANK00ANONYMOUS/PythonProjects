class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cn = 0
        cp = 0

        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                cn += 1
            if num > 0:
                cn += 1

        if cn > 0 and cn % 2:
            return -1
        if cn > 0 and cn % 2 == 0:
            return 1

        return 1
