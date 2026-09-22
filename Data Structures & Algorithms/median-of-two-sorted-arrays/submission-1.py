class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            mid1 = (l + r) // 2
            mid2 = half - (mid1+1) - 1

            l1 = A[mid1] if mid1 >= 0 else float('-infinity')
            l2 = B[mid2] if mid2 >= 0 else float('-infinity')
            r1 = A[mid1 + 1] if (mid1 + 1) < len(A) else float('infinity')
            r2 = B[mid2 + 1] if (mid2 + 1) < len(B) else float('infinity')

            if l1 <= r2 and l2 <= r1:
                # ODD
                if total % 2 == 1:
                    return min(r1, r2)

                #EVEN
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2

            elif l1 > r2:
                r = mid1 - 1
            else:
                l = mid1 + 1