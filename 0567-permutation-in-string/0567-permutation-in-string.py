class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        # Count characters in s1
        s1_count = Counter(s1)
        # Initialize the sliding window's character count for s2
        window_count = Counter(s2[:len1])

        # Check the initial window
        if window_count == s1_count:
            return True
        
        # Slide the window across s2
        for i in range(len1, len2):
            # Add the new character (right side of the window)
            window_count[s2[i]] += 1
            # Remove the old character (left side of the window)
            window_count[s2[i - len1]] -= 1
            
            # Clean up zero-count entries to keep counters comparable
            if window_count[s2[i - len1]] == 0:
                del window_count[s2[i - len1]]
            
            # Check if current window matches s1 count
            if window_count == s1_count:
                return True

        return False
        