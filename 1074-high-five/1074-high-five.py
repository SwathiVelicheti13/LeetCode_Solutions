class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dict1 = defaultdict(list)

        for list1 in items:
            dict1[list1[0]].append(list1[1])

        l1 = []
        for key, values in dict1.items():
            values = sorted(values,reverse=True)[:5]
            sum1=sum(values)//len(values)
            l1.append([key,sum1])
        l1.sort()
        return l1

            

        