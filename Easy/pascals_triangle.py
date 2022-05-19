class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []

        for row in range(numRows):
            line = [1]
            for k in range(row):
                line.append( int(line[k] * (row-k) / (k+1)) )

            output.append(line)

        return output
