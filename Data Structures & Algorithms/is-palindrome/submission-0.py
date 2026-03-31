class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Using Built In Alphanum Func. --
        # alphanumstr = ""
        # for char in s:
        #     if char.isalnum():
        #         alphanumstr += char.lower()
        # return alphanumstr == alphanumstr[::-1]
        # Time Complaxity - O(n)
        # Space Complaxity - O(n)

        # Without inbuilt function -----

        left, right = 0, len(s) -1

        while left<right:
            while left<right and not self.isalpha(s[left]):
                left+=1
            while right>left and not self.isalpha(s[right]):
                right-=1
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True

    def isalpha(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9")) 
    # Time complexity: O(n) because you scan each character in the string once.
    # Space complexity: O(1) because you only use a few index variables (left/right) and do not create new strings.

