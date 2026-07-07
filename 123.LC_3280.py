class Solution:
    def convertDateToBinary(self, date: str) -> str:
        y, m, d = date.split('-')
        a =  bin(int(y))[2:]
        b =  bin(int(m))[2:]
        c = bin(int(d))[2:]
        return f"{a}-{b}-{c}"
