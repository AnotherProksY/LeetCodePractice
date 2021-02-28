class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        guard !nums.isEmpty else { return 0 }
        
        var l = 0
        for i in 0..<nums.count {
            if nums[i] != nums[l] {
                l+=1
                nums[l] = nums[i]
            }
        }
        
        return l+1
    }
}
