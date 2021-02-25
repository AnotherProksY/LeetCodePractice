class Solution {
    func romanToInt(_ s: String) -> Int {
        let r_map: [Character: Int] = [
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        ]
        
        guard s.count > 1 else {
            return r_map[Character(s)]!
        }
        
        var num = [Int]()
        
        for c in s {
            num.append(r_map[c]!)
        }
        
        var i = 0
        var endIndex = s.count-1
        while i < endIndex {
            if num[i] < num[i+1] {
                num[i] = num[i+1] - num[i]
                num.remove(at: i+1)
                endIndex -= 1
            }
            i+=1
        }
        
        return num.reduce(0, +)
    }
}
