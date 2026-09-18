class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speedl = 1
        speedr = max(piles) + 1
        
        while speedl < speedr:
            mid = speedl + ((speedr - speedl) // 2)
            
            # Считаем часы (трюк с целочисленным округлением вверх вместо math.ceil)
            hours_needed = sum((pile + mid - 1) // mid for pile in piles)
            
            if hours_needed > h:
                speedl = mid + 1  # Не успеваем, нужна скорость выше
            else:
                speedr = mid      # Успеваем, пробуем найти скорость еще ниже
                
        # Когда цикл закончится, speedl == speedr, и это наш ответ
        return speedl