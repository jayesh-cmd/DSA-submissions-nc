class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Brute Force ----
        # freq_map = {}
        # for num in nums:
        #     freq_map[num] = freq_map.get(num,0)+1
        # sorted_item = sorted(freq_map.items(),key=lambda x:x[1], reverse=True)
        # result = []
        # for i in range(k):
        #     result.append(sorted_item[i][0])
        # return result
        # T.C. -> O(n log n) -> Due To Sorting
        # S.C. -> O(n) -> Frequency Map

        # Optimal Solution (Bucket Sorting)
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0)+1

        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        # T.C. -> O(n)
        # S.C. -> O(n)