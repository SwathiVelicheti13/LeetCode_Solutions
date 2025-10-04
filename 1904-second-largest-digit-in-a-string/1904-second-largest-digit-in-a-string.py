class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        list1= []
        for i in s:
            if i.isnumeric():
                list1.append(int(i))
        if len(list1)==0:
            return -1

        list1.sort()
        print(list1)
        for i in range(len(list1)-1,-1,-1):
            for j in range(len(list1)-2,-1,-1):
                if list1[i]>list1[j]:
                    return list1[j]
        return -1




            



        