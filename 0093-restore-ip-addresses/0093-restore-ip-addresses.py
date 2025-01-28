class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, segments):
            # If 4 segments are formed and the string is completely used
            if len(segments) == 4:
                if start == len(s):
                    result.append('.'.join(segments))
                return
            
            # Iterate through possible segment lengths (1 to 3)
            for i in range(1, 4):
                if start + i > len(s):  # If segment goes out of bounds
                    break
                
                segment = s[start:start + i]
                
                # Check if the segment is valid
                if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                
                # Backtrack with the current segment added
                backtrack(start + i, segments + [segment])
        
        result = []
        backtrack(0, [])
        return result
        