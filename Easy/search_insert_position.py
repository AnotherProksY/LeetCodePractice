class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0

        for i, n in enumerate(nums):
            if target <= n:
                index = i
                break
            else:
                index = i+1

        return index
