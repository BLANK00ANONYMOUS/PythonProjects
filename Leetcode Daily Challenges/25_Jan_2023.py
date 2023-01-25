import collections
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = collections.defaultdict(list)
        for src, dest in enumerate(edges):
            adj[src].append(dest)

        def bfs(src, dist_from_src):
            q = collections.deque()
            q.append([src, 0])
            dist_from_src[src] = 0

            while q:
                node, dist = q.popleft()
                for child in adj[node]:
                    if child not in dist_from_src:
                        q.append([child, dist + 1])
                        dist_from_src[child] = dist + 1

        dist_from_node1 = {}
        dist_from_node2 = {}

        bfs(node1, dist_from_node1)
        bfs(node2, dist_from_node2)

        res = -1
        res_dist = float("inf")

        for i in range(len(edges)):
            if i in dist_from_node1 and i in dist_from_node2:
                dist = max(dist_from_node1[i], dist_from_node2[i])
                if dist < res_dist:
                    res = i
                    res_dist = dist

        return res
