class Solution:
    def betterCompression(self, compressed: str) -> str:
        i = 0
        freq_map = defaultdict(int)

        while i<len(compressed):

            char = compressed[i]
            i += 1
            # Extract the frequency number after the character
            freq = 0
            while i < len(compressed) and compressed[i].isdigit():
                freq = freq * 10 + int(compressed[i])
                i += 1
            # Add the frequency to the character in the frequency map
            freq_map[char] += freq
        
        print(freq_map)

        res = []

        for val in sorted(freq_map.keys()):
            res.append(str(val))
            res.append(str(freq_map[val]))
        print(res)
        return ''.join(res)


            