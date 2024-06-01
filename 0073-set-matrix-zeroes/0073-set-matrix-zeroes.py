class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, columns = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_columns = set()

        # Find all zeroes and record their row & column
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)
        
        # Set rows to zero
        for i in zero_rows:
            for j in range(columns):
                matrix[i][j] = 0

        # Set columns to zero
        for j in zero_columns:
            for i in range(rows):
                matrix[i][j] = 0