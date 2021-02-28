class Solution {
    func plusOne(_ digits: [Int]) -> [Int] {
        var dummy = digits
        dummy[dummy.endIndex-1] += 1

        var output = [Int]()
        
        var digitMem = 0
        for d in dummy.reversed() {
            let nd = d+digitMem
            digitMem = 0

            if nd == 10 {
                digitMem+=1
                output.append(0)
            } else {
                output.append(nd)
            }
        }
        if digitMem == 1 { output.append(digitMem) }
        
        return output.reversed()
    }
}
