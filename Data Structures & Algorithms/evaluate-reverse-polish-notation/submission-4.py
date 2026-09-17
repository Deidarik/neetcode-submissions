
class Solution:
    def arithmetics(self, nums: List[int], choice: str) -> None:
        res = 0
        b, a = nums.pop(), nums.pop()
        match choice:
           case '+':
                res = a + b
           case '*':
                res = a * b
           case '-':
                res = a - b
           case '/':
            try:
                res = int(a / b)
            except ZeroDivisionError:
                res = 0
        nums.append(res)

    def evalRPN(self, tokens: List[str]) -> int:
        operands = ['-', '+', '*', '/']
        nums = []
        for char in tokens:
            if char not in operands:
                nums.append(int(char))
            else:
                try:
                    self.arithmetics(nums, char)
                except Exception as e:
                    return -1
        return nums[0]
        
            

