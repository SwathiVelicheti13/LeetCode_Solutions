class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)

        for val in nums:
            dict1[val]+=1
        
        list1 = []

        for key,val in dict1.items():
            list1.append([-val,key])

        heapq.heapify(list1)

        res = []
        for i in range(k):
            val,key = heapq.heappop(list1)
            res.append(key)
        return res



        # if len(dict1) == k:
        #     return list(dict1.keys())

        # k = k%len(dict1)
        # for a in range(k):
        #     max1 = 0
        #     for x,y in dict1.items():
        #         if max1<y:
        #             max1 = y
        #             temp =x 
        #     list1.append(temp)
        #     dict1[temp] = 0
        # return list1
                

    


        