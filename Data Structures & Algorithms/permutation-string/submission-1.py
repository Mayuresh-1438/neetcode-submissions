class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        s1_sorted = sorted(s1)
        for i in range(n2 - n1 + 1):
            sub = s2[i:i + n1]
            if sorted(sub) == s1_sorted:
                return True
        return False