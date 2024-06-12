class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if (numRows == 1):
             return [[1]]
        elif (numRows == 2):
             return [[1], [1, 1]]
        
        pascals_triangle = [[1], [1, 1]]

        for n in range(1, numRows - 1):
            row = [1]
            for i in range(len(pascals_triangle[n]) - 1):
                row.append(pascals_triangle[n][i] + pascals_triangle[n][i + 1])
            
            row.append(1)
            pascals_triangle.append(row)
        
        return pascals_triangle