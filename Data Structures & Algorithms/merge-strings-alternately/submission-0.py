class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged = []
        i = 0
        j = 0

        n = len(word1)
        m = len(word2)

        while i < n and i < m:
            merged.append(word1[i])
            merged.append(word2[j])
            i+=1
            j+=1

        # Check that if words remains characters
        if i < n:
            merged.append(word1[i:])

        if j < m:
            merged.append(word2[j:])

        return ''.join(merged)
        # T.C. -> O(N + M) - where n i len of word1 and m is len of word2
        # S.C. -> O(N + M) - both strings stored in the merged arr