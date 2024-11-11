class Solution:
    def myAtoi(self, s: str) -> int:
        s= s.lstrip()
        if not s:
            return 0

        sign = 1
        index = 0

        if s[0] == '-':
            sign = -1
            index+=1
        elif s[0] == '+':
            index+=1
        
        result = 0

        while index<len(s) and s[index].isdigit():
            result = result*10 + int(s[index])
            index+=1
        
        result *= sign
        INTMAX = 2**31 -1
        INTMIN = -2**31

        if result<INTMIN:
            return INTMIN
        if result > INTMAX:
            return INTMAX
        
        return result
        