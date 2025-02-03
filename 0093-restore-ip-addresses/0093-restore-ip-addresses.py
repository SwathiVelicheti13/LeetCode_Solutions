class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        ipAddressList = []
        def backtracking(start,segments):
            if len(segments) == 4:
                if start == len(s):
                    str1 = '.'.join(segments)
                    ipAddressList.append(str1)
                    return 

            
            for digit in range(1,4):
                if start+digit<=len(s):
                    segment = s[start:start+digit]
                    if (len(segment)>1 and segment[0]=='0') or int(segment)>255:
                        continue
                    backtracking(start+digit,segments+[segment])

        backtracking(0,[])
        return ipAddressList

                

        