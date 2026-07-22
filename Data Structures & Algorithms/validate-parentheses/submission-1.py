class Solution:
    def isValid(self, s: str) -> bool:
        
        while True:

            changed = False

            for pair in ["()", "[]", "{}"]:
                if pair in s:
                    s = s.replace(pair, "")
                    changed = True

            if not changed:
                break

        return s == ""