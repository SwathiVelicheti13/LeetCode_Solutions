class MinStack(object):

    def __init__(self):
        self.arr = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self.arr.append(val)

        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.arr) == 0:
            return -1
        else:
            self.arr.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.arr[len(self.arr)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        min1 = min(self.arr)
        return min1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()