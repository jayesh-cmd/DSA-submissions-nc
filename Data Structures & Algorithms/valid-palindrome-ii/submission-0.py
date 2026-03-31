class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # Brute --
        # def is_pal(sub_s):
        #     return sub_s == sub_s[::-1]
        # if is_pal(s):
        #     return True
        # for i in range(len(s)):
        #     temp_str = s[:i] + s[i+1:]
        #     if is_pal(temp_str):
        #         return True
        # return False
        # T.C. -> O(n^2) -> loop through string, creating new temp str
        # S.C. -> O(n) -> Stroing temp

        # Optimal ---
        l, r = 0, len(s)-1

        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                skipl = s[l+1 : r+1]
                skipr = s[l : r]
                return (skipl == skipl[::-1] or (skipr == skipr[::-1]))
        return True
        # T.C. -> O(n)
        # S.C. -> O(n) Slicing creates temp string