import math

class Solution:
    def nearestPalindromic(self, n: str) -> str:

        if 1 <= int(n) <= 9:
            return str(int(n) - 1)  # Handle single-digit numbers separately

        len1 = len(n)
        half_len = (len1 + 1) // 2  # Correct calculation of left part
        left = int(n[:half_len])  # Extract left part

        res = set()  # Use a set to avoid duplicates

        # Function to create a palindrome
        def make_palindrome(left):
            left_str = str(left)
            if len(n) % 2 == 0:  
                result = int(left_str + left_str[::-1])  # Mirror full left
            else:
                result = int(left_str + left_str[-2::-1])  # Mirror except last digit
            
            res.add(result)

        # Generate possible palindrome candidates
        make_palindrome(left)     # Mirror `left`
        make_palindrome(left - 1) # Mirror `left-1`
        make_palindrome(left + 1) # Mirror `left+1`
        res.add(10 ** (len1 - 1) - 1)  # Largest palindrome with len-1 digits
        res.add(10 ** len1 + 1)  # Smallest palindrome with len+1 digits

        # Remove the original number itself if present
        res.discard(int(n))

        # Find the closest palindrome
        min_diff = float('inf')
        best_value = None
        num = int(n)

        print(res)  # Debugging output

        for val in res:
            diff = abs(num - val)
            if diff < min_diff or (diff == min_diff and val < best_value):
                min_diff = diff
                best_value = val

        return str(best_value)
