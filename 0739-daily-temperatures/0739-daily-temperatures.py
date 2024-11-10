class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0]*len(temperatures)
        stack = []

        for x in range(len(temperatures)):
            while stack and temperatures[x] > temperatures[stack[-1]]:
                idx = stack.pop()
                answers[idx] = x-idx
            stack.append(x)
        return answers

        