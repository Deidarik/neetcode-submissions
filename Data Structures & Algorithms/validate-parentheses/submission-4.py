class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        open_brackets = ['[', '{', '(']
        close_brackets = [']', '}', ')']
        stack = []
        ind = -1
        for char in s:
            if char in open_brackets:
                stack.append(char)
                ind+=1
            elif char in close_brackets and len(stack):
                if abs(ord(stack[ind]) - ord(char)) <=2:
                    stack.pop()
                    ind-=1
                else:
                    return False
            else:
                return False
        
        return True if len(stack) == 0 else False
            


        