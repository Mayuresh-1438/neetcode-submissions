class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            hs = set()
            for j in range(i,len(s)):
                if s[j] in hs:
                    break
                hs.add(s[j])
            max_len = max(max_len,len(hs))
        return max_len
            