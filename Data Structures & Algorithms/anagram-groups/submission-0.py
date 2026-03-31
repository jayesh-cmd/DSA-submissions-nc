import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = collections.defaultdict(list)
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char) - ord('a')] += 1
            d[tuple(count)].append(string)
        return list(d.values())
        # Time Complexity: O(m × n) , m = number of strings in strs, n = average length of each string
        # Space Complexity: O(m × n), We store all strings in the dictionary, and each string has length n