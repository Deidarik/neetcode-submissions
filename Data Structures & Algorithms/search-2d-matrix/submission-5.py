class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows, cols = len(matrix), len(matrix[0])
        
        # ШАБЛОН [l, r)
        l, r = 0, rows * cols 
        
        while l < r:
            mid = l + (r - l) // 2
            
            # Перевод 1D в 2D
            val = matrix[mid // cols][mid % cols]
            
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid 
                
        return False