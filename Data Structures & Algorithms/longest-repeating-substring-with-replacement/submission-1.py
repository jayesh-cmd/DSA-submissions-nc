class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        max_len = 0

        for i in range(n):

            char_count = {}
            max_freq = 0

            for j in range(i, n):

                char_count[s[j]] = char_count.get(s[j], 0) + 1

                max_freq = max(max_freq, char_count[s[j]])

                window = j - i + 1

                changes_need = window - max_freq

                if changes_need <= k:
                    max_len = max(max_len, window)
                else:
                    break

        return max_len