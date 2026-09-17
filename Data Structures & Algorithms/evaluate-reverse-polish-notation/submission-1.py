
class Solution:
    def arithmetics(self, nums: List[int], choice: str) -> None:
        res = 0
        i = len(nums)
        match choice:
           case '+':
                res = nums[i - 2] + nums[i - 1]
           case '*':
                res = nums[i - 2] * nums[i - 1]
           case '-':
                res = nums[i - 2] - nums[i - 1]
           case '/':
            try:
                res = int(nums[i - 2] / nums[i - 1])
            except ZeroDivisionError:
                res = 0
        nums.pop() 
        nums.pop()
        nums.append(int(res))

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
        
            

