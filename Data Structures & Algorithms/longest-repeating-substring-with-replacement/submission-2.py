class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        max_len = 0

        for i in range(len(s)):

            char_count = {}
            max_freq = 0

            for j in range(i, len(s)):

                char_count[s[j]] = char_count.get(s[j], 0) + 1

                max_freq = max(max_freq, char_count[s[j]])

                window = j - i + 1

                need = window - max_freq

                if need <= k:
                    max_len = max(max_len, window)
                else:
                    break

        return max_len