class Solution {

    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var check_val = [Int: Int]()

        for (i, n) in nums.enumerated() {

            let second_num = target - n
            
            if let second_ind = check_val[second_num] {
                return [i, second_ind]
            }
            
            check_val[n] = i
        }

        return []
    }
}
