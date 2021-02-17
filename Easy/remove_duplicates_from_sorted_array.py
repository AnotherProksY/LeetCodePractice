class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        l = 0
        for i in range(len(nums)):
            if nums[i] != nums[l]:
                l+=1
                nums[l] = nums[i]

        return l+