from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[-1] * (k + 1) for _ in range(n)]

        def back_track(i, coins):
            if i == n:
                return 0

            if dp[i][coins] != -1:
                return dp[i][coins]

            dp[i][coins] = back_track(i + 1, coins)
            cur_pile = 0
            for j in range(min(coins, len(piles[i]))):
                cur_pile += piles[i][j]
                dp[i][coins] = max(dp[i][coins], cur_pile + back_track(i + 1, coins - j - 1))

            return dp[i][coins]

        return back_track(0, k)