class Solution:
    def isValid(self, s: str) -> bool:
        # first thought is a stack where once you see the close you pop

        stack = []
        counterPart = {'(':')', '{':'}', '[':']'}
        if not s:
            return True
        for c in s:
            print(stack)
            # if not stack:
            #     stack.append(c)
            if c in counterPart:
                stack.append(c)
            else:

                if stack and counterPart[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
            # if stack and counterPart[stack[-1]]:
            #     if stack and counterPart[stack[-1]] == c:
            #         stack.pop()
            # else:
            #     stack.append(c)
        
        # if stack:
        #     return False
        return not stack