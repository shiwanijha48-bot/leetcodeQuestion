class Solution:
    def passwordStrength(self, password: str) -> int:
        temp = set(password)   # to get unique chars only
        st = 0  # total streangth
        for ch in temp:
            if 'a' <= ch <= 'z':
                st += 1
            elif 'A' <= ch <= 'Z':
                st += 2
            elif '0' <= ch <= '9':
                st += 3
            elif ch in '@#$!':
                st += 5
        return st
            
