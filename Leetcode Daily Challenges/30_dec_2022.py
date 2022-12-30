from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, cur):
            if node == n - 1:
                res.append(cur)

            for child in graph[node]:
                dfs(child, cur + [child])

        n = len(graph)
        res = []
        dfs(0, [0])
        return res
