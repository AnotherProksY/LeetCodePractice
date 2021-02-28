class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        guard strs.count > 0 else { return "" }
        
        var commonPrefix = strs.first!
        
        for str in strs[1...] {
            while !str.hasPrefix(commonPrefix) {
                commonPrefix = String(commonPrefix.dropLast())
            }
        }

        return commonPrefix
    }
}
