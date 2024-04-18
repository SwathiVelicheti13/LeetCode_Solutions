class MyQueue(object):

    def __init__(self):
        self.stack=deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: int
        """
        return self.stack.popleft()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()