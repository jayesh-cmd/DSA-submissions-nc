class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # One Method --
        # concat_arr =[]
        # for num in nums:
        #     concat_arr.append(num)
        # concat_arr.extend(nums)
        # return concat_arr

        # Second Method --
        return nums + nums

        # For Both --
        # O(n) - because both need to copy all elements to the new array.
        # O(n) - since we create a new array of size 2n
