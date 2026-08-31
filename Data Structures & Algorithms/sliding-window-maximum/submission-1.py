class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # res = []
        # for i in range(len(nums) - k + 1):
        #     temp_s = []
        #     for j in range(i, i + k):
        #         temp_s.append(nums[j])
        #     res.append(max(temp_s))
        # return res
        # tc - O(N * k), sc - O(N)

        res = []
        l = 0
        r = 0
        q = collections.deque()

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res