class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        def good(i):
            if l1 % i or l2 % i:
                return False
            d1 = l1 // i
            d2 = l2 // i
            return str1[:i] * d1 == str1 and str1[:i] * d2 == str2

        for i in range(min(l1, l2), 0, -1):
            if good(i):
                return str1[:i]

        return ""
