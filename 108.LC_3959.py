class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digSum = 0
        sqSum = 0
        while n > 0:
            dig = n % 10
            digSum += dig
            sqSum += dig * dig
            n //= 10
        if sqSum - digSum >= 50:
            return True
        else:
            return False
            
            
