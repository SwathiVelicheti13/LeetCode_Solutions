class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dict1 = defaultdict(list)

        for list1 in items:
            dict1[list1[0]].append(list1[1])
            dict1[list1[0]].sort(reverse = True)

        l1 = []
        for key, values in dict1.items():
            sum1=(sum(values[0:5]))//5
            l1.append([key,sum1])
        l1.sort()
        return l1

            

        