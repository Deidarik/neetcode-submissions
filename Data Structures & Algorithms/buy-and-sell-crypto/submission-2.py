class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        dif = 0
        for right in range(1, len(prices)):
            if prices[left] <= prices[right]:
                if dif < prices[right] - prices[left]:
                    dif = prices[right] - prices[left]
            else:
                left = right
        return dif
