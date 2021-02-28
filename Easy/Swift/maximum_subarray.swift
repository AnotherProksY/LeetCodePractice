class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        var dp = Array(repeating: 0, count: nums.count)
        dp[0] = nums[0]
        
        for i in 1..<nums.count {
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        }
        
        if let max = dp.max() {
            return max
        } else {
            return nums[0]
        }
    }
}
