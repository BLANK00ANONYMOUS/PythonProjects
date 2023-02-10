class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque()

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    q.append([r, c])

        res = -1
        dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            r, c = q.popleft()
            res = grid[r][c]

            for dx, dy in dr:
                nx, ny = r + dx, c + dy
                if (min(nx, ny) >= 0 and
                        max(nx, ny) < N and
                        grid[nx][ny] == 0):
                    q.append([nx, ny])
                    grid[nx][ny] = grid[r][c] + 1

        return res - 1 if res > 1 else -1