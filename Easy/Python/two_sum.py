class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_val = {}
        
        for i in range(len(nums)):
            second_num = target - nums[i]
            
            if(second_num in check_val.keys()):
                second_ind = nums.index(second_num)
                if(i != second_ind): return sorted([i, second_ind])
                
            check_val.update({nums[i]: i})
            
        return check_val