class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        i, j = 0, len(nums)
        
        while i < j:
            mid = i + ((j - i) // 2)
            
            if nums[mid] == target:
                return mid
                
            # ШАГ 1: Проверяем, отсортирована ли ЛЕВАЯ половина [i ... mid]
            if nums[i] <= nums[mid]:
                # Если да, проверяем, попадает ли target в этот отсортированный диапазон
                if nums[i] <= target < nums[mid]:
                    j = mid          # target здесь, сужаем вправо
                else:
                    i = mid + 1      # target не здесь, ищем в правой части
                    
            # ШАГ 2: Если левая не отсортирована, значит ПРАВАЯ половина [mid ... j-1] точно отсортирована
            else:
                # Проверяем, попадает ли target в правый отсортированный диапазон
                if nums[mid] < target <= nums[j - 1]:
                    i = mid + 1      # target здесь, сужаем влево
                else:
                    j = mid          # target не здесь, ищем в левой части
                    
        return -1