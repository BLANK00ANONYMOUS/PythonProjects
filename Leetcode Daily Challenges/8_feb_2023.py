class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        currSum = sum(arr[:k - 1])

        for l in range(len(arr) - k + 1):
            currSum += arr[l + k - 1]
            if (currSum / k) >= threshold:
                ans += 1
            currSum -= arr[l]

        return ans