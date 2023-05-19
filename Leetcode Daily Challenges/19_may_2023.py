from typing import List

# make the below code more efficient


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        for u, v in edges:
            in_degree[v] += 1

        res = []
        for i in range(n):
            if in_degree[i] == 0:
                res.append(i)

        return res
