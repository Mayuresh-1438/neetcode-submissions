class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        p = 0
        q = len(st) -1
        while p<q:
            if not st[p].isalnum():
                p +=1
                continue
            if not st[q].isalnum():
                q -=1
                continue
            if st[p] != st[q]:
                return False
            p +=1
            q -=1
        return True
