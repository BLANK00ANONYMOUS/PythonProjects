from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0
        j = 0
        for i in range(n):
            sum += mat[i][j]
            j += 1

        j = 0
        for i in range(n - 1, -1, -1):
            sum += mat[i][j]
            j += 1

        k = n // 2
        if n % 2:
            sum -= mat[k][k]
        print(mat[k][k])
        return sum
