class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tcount = {}
        for k in range(len(t)):
            tcount[t[k]] = tcount.get(t[k], 0) + 1

        l = 0
        min_len = float('inf')
        sub = ''
        have = 0
        need = len(tcount)
        win = {}

        for r in range(len(s)):
            char = s[r]
            win[char] = win.get(char, 0) + 1

            if char in tcount and win[char] == tcount[char]:
                have += 1

            while have == need:
                if (r-l+1) < min_len:
                    min_len = (r-l+1)
                    sub = s[l:r+1]

                left_char = s[l]
                win[left_char] = win.get(left_char, 0) - 1

                if left_char in tcount and win[left_char] < tcount[left_char]:
                    have -= 1

                l += 1

        return sub