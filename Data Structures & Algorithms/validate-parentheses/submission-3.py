class Solution:
    def isValid(self, s: str) -> bool:
        
        # while True:
        #     changed = False
        #     for pair in ["()", "[]", "{}"]:
        #         if pair in s:
        #             s = s.replace(pair, "")
        #             changed = True
        #     if not changed:
        #         break
        # return s == ""

        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack
        # O(N), O(N)