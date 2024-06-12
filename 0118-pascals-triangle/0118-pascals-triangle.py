class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = []

        for row_number in range(numRows):
            # Start each row with 1s
            row = [1] * (row_number + 1)

            # Calculate the values for current row
            for j in range(1, row_number):
                row[j] = pascals_triangle[row_number -1][j-1] + pascals_triangle[row_number -1][j]

            # Add to pascal's triangle
            pascals_triangle.append(row)

        return pascals_triangle