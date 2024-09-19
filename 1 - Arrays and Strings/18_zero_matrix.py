'''
Zero Matrix: 
Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to 0.
'''
import unittest


# Time: O(MxN) Space O(M+N)
def zero_matrix(matrix:list[list[int]]) -> list[list[int]]:

    cols = set()
    rows = set()
    for rowIndex in range(len(matrix)):
        for colIndex in range(len(matrix[rowIndex])):
            if matrix[rowIndex][colIndex] == 0:
                cols.add(colIndex)
                rows.add(rowIndex)

    for rowIndex in rows:
        matrix[rowIndex] = [0]*len(matrix)
    
    for i in range(len(matrix)):
        for colIndex in cols:
            matrix[i][colIndex] = 0

    
    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
