class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # dict1 = defaultdict(int)

        # for i in s:
        #     dict1[i]+=1
        # slist = list(s)
        # x = 0
        # while x<len(slist):
        #     if dict1[slist[x]] == k:
        #         slist.remove(slist[x])
        #         x = x-1
        #     x+=1
        # return ''.join(slist)
        stck = [['$', 0]]     # a placeholder to mark stack is empty. This eliminates the need to do an empty check later
        
        for c in s:
            if stck[-1][0] == c:
                stck[-1][1]+=1 # update occurences count of top element if it matches current character
                if stck[-1][1] == k:
                    stck.pop()
            else:
                stck.append([c, 1])            
        
        return ''.join(c * cnt for c, cnt in stck)

        
        
        