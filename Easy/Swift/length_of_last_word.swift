class Solution {
    func lengthOfLastWord(_ s: String) -> Int {
        if let word = s.split(separator: " ").last {
            return word.count
        } else {
            return 0
        }
    }
}
