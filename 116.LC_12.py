class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000 : "M", 900: "CM", 500 : "D", 400 : "CD", 100 : "C", 90 : "XC", 50 : "L", 40 : "XL" , 10 : "X" , 9 : "IX",  5 : "V" , 4 : "IV" , 1 : "I"} # Roman values and their symbols-> largest to smalleszt
        res = ""  # final roman numberal
    
        for i in roman: # checking each roman num from largest to smallest
            while num >= i:  # can use current roman val multiple time. like VIII = 8
                res += roman[i] # Add Roman symbol
                num -= i # reduce number
        return res
