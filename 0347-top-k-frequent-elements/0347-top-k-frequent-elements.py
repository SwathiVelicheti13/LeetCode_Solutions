import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = Counter(nums)

        heapList = []
        result = []
      
        for key,val in dict1.items():
            heapList.append([-val,key])

        heapq.heapify(heapList)
        
        print(heapList)
        for i in range(k):
            val,key = heapq.heappop(heapList)
            result.append(key)
        return result




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
                

    


        