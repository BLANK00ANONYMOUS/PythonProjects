class Solution:
    def countOdds(self, low: int, high: int) -> int:
        sz = high - low + 1
        cnt = sz // 2

        if sz % 2 and low % 2:
            cnt += 1

        return cnt
