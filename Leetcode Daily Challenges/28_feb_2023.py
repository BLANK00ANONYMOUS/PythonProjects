from collections import defaultdict
from idlelib.tree import TreeNode
from typing import Optional, List


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)

        def dfs(node):
            if not node:
                return "null"

            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(subtrees[s]) == 1:
                res.append(node)

            subtrees[s].append(node)
            return s

        res = []
        dfs(root)
        return res