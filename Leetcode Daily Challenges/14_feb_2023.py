import collections
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])

        pq = [(-1, start)]
        vis = set()

        while pq:
            prob, curr = heapq.heappop(pq)
            vis.add(curr)

            if curr == end:
                return prob * -1

            for neig, edgeProb in adj[curr]:
                if neig not in vis:
                    heapq.heappush(pq, (prob * edgeProb, neig))

        return 0