class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_d = {}
        for i in range(0, len(nums)):
            if nums[i] not in num_d:
                num_d[nums[i]] = str(i)
            else:
                num_d[nums[i]] += '.' + str(i)
        for num in num_d.keys():
            dif = target - num
            if dif in num_d and dif == num and len(num_d[num].split('.')) >= 2:
                return num_d[num].split('.')[:2]
            elif dif in num_d and dif != num:
                a, b = num_d[num].split('.')[0], num_d[dif].split('.')[0]
                return [a, b] if a < b else [b, a]
        return -1
        