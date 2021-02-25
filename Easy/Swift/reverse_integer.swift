class Solution {
    func reverse(_ x: Int) -> Int {
        let minRange = -2_147_483_648
        let maxRange = 2_147_483_647

        let sign = x>0 ? 1 : -1
        let abs_x = String(abs(x)).reversed()

        let rev = sign * Int(String(abs_x))!

        if rev < minRange || rev > maxRange {
            return 0
        } else {
            return rev
        }
    }
}
