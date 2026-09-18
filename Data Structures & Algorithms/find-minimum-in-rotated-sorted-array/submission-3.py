class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None:
            return -1
        i = 0
        j = len(nums)
        while i < j:
            mid = i + ((j - i) // 2)
            if nums[mid] > nums[len(nums)-1]:
                i = mid + 1
            elif nums[mid] <= nums[len(nums)-1]:
                j = mid
        return nums[i]