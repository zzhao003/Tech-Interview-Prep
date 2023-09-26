class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) <= 1: return False
        # stack = []
        # m = {'[': ']','{': '}','(': ')'}
        # for el in s:
        #     # if el in m:
        #     #     stack.append(el)
        #     if stack and stack[-1] in m and m[stack[-1]] == el:
        #         stack.pop()
        #     else:
        #         stack.append(el)
        #     # print(stack)
        # return not bool(stack)
        hm = {')':'(','}':'{',']':'['}
        res = []
        for c in s:
            # if c in s, its a closing,then check if top of stack is a matching opening
            if res and c in hm and res[-1] == hm[c]:
                res.pop()
                # everything else, add to stack
            else:
                res.append(c)
        return True if len(res) == 0 else False