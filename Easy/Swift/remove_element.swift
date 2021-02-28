class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        guard !nums.isEmpty else { return 0 }
        
        var l = 0
        for i in 0..<nums.count {
            if nums[i] != val {
                nums[l] = nums[i]
                l+=1
            }
        }
        
        return l
    }
}
