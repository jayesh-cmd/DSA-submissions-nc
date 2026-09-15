class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for mat in matrix:
            l, r = 0, len(mat) - 1
            while l <= r:
                mid = (l+r)//2
                if mat[mid] == target:
                    return True
                elif mat[mid] > target:
                    r = mid - 1
                elif mat[mid] < target:
                    l = mid + 1
                else:
                    return False
        return False