class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Brute --
        # len1 = len(s1)
        # len2 = len(s2)
        # for i in range(len2-len1+1): # This Range Divides The Iteration In Equally That We Will Get The Number Of S1 To Check In S2
        #     subs = s2[i:i+len1]
        #     if sorted(s1) == sorted(subs):
        #         return True
        # return False
        # T.C.-> O(n * m)-> where n is the loop iteration and m is the string operations
        # S.C.-> O(m) -> Length Of Strings, Stores Sorted Strings

        # Optimal --
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        count1 = [0]*26
        count2 = [0]*26
        for i in range(n1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        if count1 == count2:
            return True
        for i in range(n1,n2):
            count2[ord(s2[i]) - ord('a')]+=1
            count2[ord(s2[i-n1]) - ord('a')]-=1
            if count1 == count2:
                return True
        return False
        # T.C. -> O(n)
        # S.C. -> O(1)