class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n < 1: return
        nums1[m:m+n] = [nums2[i] for i in range(n)]
        nums1.sort()
