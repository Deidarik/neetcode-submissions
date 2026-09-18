class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        i = 0
        j = len(nums) # Шаблон [i, j)
        
        while i < j:
            mid = i + ((j - i) // 2)
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[-1]:
                   i = mid + 1
            else:
                    j = mid
        if not(j):
             j = len(nums)
        elif j and nums[len(nums)-1] >= target:
            j = len(nums)
        elif j and nums[j-1] >= target:
            i = 0
        while i < j:
            mid = i + ((j - i) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                   j = mid
            else:
                   i = mid + 1
        return -1
