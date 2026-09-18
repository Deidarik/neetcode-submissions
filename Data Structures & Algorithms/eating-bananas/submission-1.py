import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #найти максимум функции
        minspeed = 2**31 - 1
        speedl = 1
        speedr = max(piles) + 1
        while speedl < speedr:
            dif = h
            mid = speedl + ((speedr - speedl) // 2)
            for pile in piles:
                dif -= math.ceil(pile/mid)
            if dif < 0:
                speedl = mid+1
            if dif >= 0:
                speedr = mid
                if mid < minspeed:
                    minspeed = mid
        return minspeed