class Solution:
    def decodeString(self, s: str) -> str:

        curr_str = ""
        curr_num = ""

        stack = []
        decode_string = ""
        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])

            else:

                curr_str = ""
                while stack and stack[-1]!='[':
                    curr_str=stack.pop()+curr_str
                stack.pop()
                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num=stack.pop()+curr_num

                curr_str = curr_str*int(curr_num)

                stack.append(curr_str)

        return ''.join(stack)
                     