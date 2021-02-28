class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        var index = 0
        
        for (i, n) in nums.enumerated() {
            if target <= n {
                index = i
                break
            } else {
                index = i+1
            }
        }
        
        return index
    }
}
