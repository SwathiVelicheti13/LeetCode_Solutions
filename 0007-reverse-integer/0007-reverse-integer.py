class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str1 = ""
        if x < -(pow(2,31)):
            return 0
        elif x > (pow(2,31)) -1:
            return 0
        else:
            x = str(x)
            str1 = x[::-1]
            if x[0] == '-':
                str1 = '-'+ str1[:-1]
            print(str1)
            x = int(str1)
            if x < -(pow(2,31)) or x > (pow(2,31)) -1:
                return 0
            return x