class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Brute Force ----
        # for row in matrix:
        #     for element in row:
        #         if element == target:
        #             return True
        # return False
        # T.C. -> O(m * n) -> m is the number of rows and n is the length of the row
        # S.C. -> O(1)

        # Optimal Solution ----
        for row in matrix:
            low, high = 0, len(row)-1
            while low<=high:
                mid = (low+high) // 2
                if row[mid] == target:
                    return True
                elif target > row[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
        # T.C. -> O(m log n) -> m is rows and log n is binary search
        # S.C. -> O(1)