class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Kind Of Brute
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    return shortest[:i]
        return shortest