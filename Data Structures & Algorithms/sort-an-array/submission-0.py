class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Merge Sort
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left,right)

        def merge(left, right):
            sorted_arr = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_arr.append(left[i])
                    i+=1
                else:
                    sorted_arr.append(right[j])
                    j+=1
                
            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])
            return sorted_arr

        return mergeSort(nums)