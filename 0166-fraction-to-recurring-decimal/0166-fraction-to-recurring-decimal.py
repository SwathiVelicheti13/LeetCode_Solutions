class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num = numerator 
        denom = denominator
        res = []

        if num%denom == 0:
            return str(num//denom)

        
        if (num < 0) ^ (denom < 0):  
            res.append('-')

        num,denom = abs(num),abs(denom)

        # integer part
        print("dd",num/denom)
        res.append(str(num//denom))
        res.append('.')

        # rem part

        rem = num%denom
        rem_map = {}

        #check for recurring decimal in quotient
        while rem:
            if rem in rem_map:
                res.insert(rem_map[rem],'(')
                res.append(')')
                break

            
            rem_map[rem] = len(res)
            rem=rem*10
            quo = rem//denom
            res.append(str(quo))
            rem = rem%denom
    
        return ''.join(res)
