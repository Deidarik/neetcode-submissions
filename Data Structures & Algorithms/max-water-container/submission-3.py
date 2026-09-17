class Solution:

    def findBucket(self, l_i: int, r_i: int, l: int, r: int) -> int:
        return (r_i - l_i) * min(l, r)

    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        height = 0
        width = 0
        res = 0
        while left < right:
            res = max(self.findBucket(left, right, heights[left], heights[right]), res)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res