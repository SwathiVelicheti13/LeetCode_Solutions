class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        # Result list to store all combinations
        result = []
        
        # Edge case: if input is empty, return an empty list
        if not digits:
            return result

        # Helper function for backtracking
        def backtrack(index, path):
            # Base case: if path length equals digits length, we have a complete combination
            if index == len(digits):
                result.append("".join(path))
                return
            
            # Get the letters corresponding to the current digit
            possible_letters = phone_map[digits[index]]
            
            # Recursively build each combination
            for letter in possible_letters:
                path.append(letter)             # Add current letter to path
                backtrack(index + 1, path)      # Move to the next digit
                path.pop()                      # Backtrack and remove last letter

        # Start backtracking from the first digit
        backtrack(0, [])
        
        return result
            