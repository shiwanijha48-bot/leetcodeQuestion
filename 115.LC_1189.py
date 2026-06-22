class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = text.count('b')
        a = text.count('a')
        l = text.count('l') // 2
        o = text.count('o') // 2
        n = text.count('n')
        return min(b, a, l, o, n)

'''
        b = a = l = o = n = 0
        for ch in text:
            if ch == 'b':
                b += 1
            elif ch == 'a':
                a+= 1
            elif ch == 'l':
                l += 1
            elif ch == 'o':
                o += 1
            elif ch == 'n':
                n += 1
        res = 0
        while b >=1 and a >= 1 and l >= 2 and o >= 2 and n >= 1:
            b -= 1
            a -= 1
            l -= 2
            o -= 2
            n -= 1
            res += 1
        return res'''
