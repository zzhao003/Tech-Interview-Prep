class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        stack = []
        m = {'[': ']','{': '}','(': ')'}
        for el in s:
            # if el in m:
            #     stack.append(el)
            if stack and stack[-1] in m and m[stack[-1]] == el:
                stack.pop()
            else:
                stack.append(el)
            # print(stack)
        return not bool(stack)
