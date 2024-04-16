class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        list1 = s.split(" ")
        list1 = [i for i in list1 if i!=""]
        list1.reverse()
        s = " ".join(list1)
        return s
        