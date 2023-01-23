class Solution(object):
    def findJudge(self, n, trust):
        in_degree = [0] * n
        out_degree = [0] * n

        for people in trust:
            people_one, people_two = people
            in_degree[people_two] += 1
            out_degree[people_one] += 1

        ans = -1
        cnt = 0
        for i in range(n):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                ans = i + 1
                cnt += 1

        if cnt > 1:
            ans = -1

        return ans
