class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Optimal Solution ---
        need = {}
        for char in t:
            need[char] = need.get(char,0) + 1

        min_len = float('inf')
        result = ''
        l = 0
        need_len = len(need)
        have_len = 0

        have = {}
        for r in range(len(s)):
            char = s[r]
            have[char] = have.get(char,0) + 1

            if char in need and have[char] == need[char]:
                have_len += 1

            while have_len == need_len:

                curr_w = r - l + 1
                if curr_w < min_len:
                    min_len = curr_w
                    result = s[l:r+1]

                left = s[l]
                have[left] -= 1

                if left in need and have[left] < need[left]:
                    have_len -= 1

                l += 1

        return result
        # T.C. -> O(S + T)
        # S.C. -> O(1)