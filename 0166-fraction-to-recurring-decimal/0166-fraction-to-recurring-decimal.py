class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
        
        # Step 2: Work with absolute values
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Step 3: Integer part
        integer_part = numerator // denominator
        remainder = numerator % denominator
        result = sign + str(integer_part)
        
        # If no remainder, return result
        if remainder == 0:
            return result
        
        # Step 4: Handle decimal part
        result += "."
        remainder_map = {}
        decimal_part = ""
        
        while remainder != 0:
            # If remainder repeats
            if remainder in remainder_map:
                index = remainder_map[remainder]
                decimal_part = decimal_part[:index] + "(" + decimal_part[index:] + ")"
                return result + decimal_part
            
            # Store the current remainder position
            remainder_map[remainder] = len(decimal_part)
            
            # Multiply remainder by 10 and divide
            remainder *= 10
            decimal_part += str(remainder // denominator)
            remainder %= denominator
        
        # Append the non-repeating decimal part
        return result + decimal_part
            