class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        guard x >= 0 else { return false }
                
        var reverse = 0
                
        var reducing = x
        while reducing > 0 {
            reverse *= 10
            reverse += reducing % 10
            reducing /= 10
        }
        
        return x == reverse
    }
}
