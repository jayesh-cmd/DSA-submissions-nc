class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            freq[num] += 1

        sorted_item = sorted(freq.items(), key=lambda x : x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(sorted_item[i][0])

        return res