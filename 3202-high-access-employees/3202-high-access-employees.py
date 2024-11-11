class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        when = defaultdict(list)
        res = []
        for a in access_times:
            m,k = a
            when[m].append(int(k))


        for x,lst in when.items():
            lst.sort()
            k = len(lst)
            flag = False

            for i in range(k-2):
                flag = flag or lst[i+2]< lst[i]+100
            
            if flag:
                res.append(x)
        return res


        