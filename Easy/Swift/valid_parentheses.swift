class Solution {
    func isValid(_ s: String) -> Bool {
        // Open brackets postition
        var om = [Character]()
        
        // Close brackets mapping
        let cm: [Character: Character] = [
            ")":"(",
            "]":"[",
            "}":"{"
        ]
        
        for b in s {
            if "([{".contains(b) {
                om.append(b)
            } else {
                if !om.isEmpty && cm[b] == om.last {
                    om.removeLast()
                } else {
                    return false
                }
            }
        }
        
        if !om.isEmpty { return false } else { return true }
    }
}
