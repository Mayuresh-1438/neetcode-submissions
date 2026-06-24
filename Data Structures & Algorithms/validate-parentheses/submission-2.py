class Solution:
    def isValid(self, s: str) -> bool:
        
        st = []

        mp = { ')': '(', '}' : '{', ']' : '[' }


        for char in s:
            if char in '({[':
                st.append(char)
            elif st and st[-1] == mp[char]:
                st.pop()
            else:
                return False

        return len(st) == 0




