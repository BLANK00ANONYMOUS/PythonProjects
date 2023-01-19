class Solution(object):
    def subarraysDivByK(self, nums, k):
        sums = [0] * k
        sums[0] += 1
        res = 0
        currSum = 0
        for n in nums:
            currSum = (currSum + n % k + k) % k
            res += sums[currSum]
            sums[currSum] += 1
        return res



