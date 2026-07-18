class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s and not t:
            return ''

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        l = 0
        have = {}
        result = ''
        min_len = float('inf')
        have_len = 0
        need_len = len(need)

        for r in range(len(s)):
            char = s[r]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                have_len += 1

            while have_len == need_len:
                curr = (r - l + 1)
                if curr < min_len:
                    min_len = curr
                    result = s[l:r+1]

                left = s[l]
                have[left] -= 1

                if left in need and have[left] < need[left]:
                    have_len -= 1

                l += 1

        return result