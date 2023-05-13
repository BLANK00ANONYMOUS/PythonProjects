class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10 ** 9 + 7
        dp = {}

        def back_track(length):
            if length > high:
                return 0
            if length in dp:
                return dp[length]

            dp[length] = 1 if length >= low else 0
            dp[length] += back_track(length + zero)
            dp[length] += back_track(length + one)

            return dp[length] % mod

        return back_track(0)
