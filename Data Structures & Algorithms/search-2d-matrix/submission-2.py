class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0, len(matrix)):
            if (matrix[i][len(matrix[i])-1] == target):
                return True
            if (matrix[i][len(matrix[i])-1] > target):
                j = len(matrix[i])
                k = 0
                while k < j:
                    mid = k + ((j - k) // 2)
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        k = mid + 1
                    elif matrix[i][mid] > target:
                        j = mid   
        return False
