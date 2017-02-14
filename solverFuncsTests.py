import unittest
from solverFuncs import *

puzzle1 = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]] #no duplicates
puzzle2 = [[0,1,2,3,4],[6,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]] #duplicate at index puzzle2[1][0]
puzzle3 = [[0,1,2,3,4],[5,6,7,8,9],[5,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]] #duplicate at index puzzle3[3][0]
puzzle4 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] #initializePuzzle

class TestCase(unittest.TestCase):
    def test_getCellValue_CorrectIndex_CorrectCell_1(self):
        self.assertAlmostEqual(getCellValue(puzzle1, 0), 0)
    def test_getCellValue_CorrectIndex_CorrectCell_2(self):
        self.assertAlmostEqual(getCellValue(puzzle1, 24), 24)
    def test_getCellValue_CorrectIndex_CorrectCell_3(self):
        self.assertAlmostEqual(getCellValue(puzzle1,15), 15)

    def test_checkRowValid_NoDuplicates_True_1(self):
        self.assertTrue(checkRowValid(puzzle1, 0))
    def test_checkRowValid_Duplicates_False_2(self):
        self.assertFalse(checkRowValid(puzzle2,1))
    def test_checkRowValid_DuplicateZeros_True_2(self):
        self.assertTrue(checkRowValid(puzzle4, 0))

    def test_check_rows_valid_NoDuplicates_True_1(self):
        self.assertTrue(check_rows_valid(puzzle1))
    def test_check_rows_valid_Duplicates_False_2(self):
        self.assertFalse(check_rows_valid(puzzle2))

    def test_checkColValid_NoDuplicates_True_1(self):
        self.assertTrue(checkColummValid(puzzle1,0))
    def test_checkColValid_Duplicates_False_2(self):
        self.assertFalse(checkColummValid(puzzle3,0))

    def test_check_columns_valid_NoDuplicates_True_1(self):
        self.assertTrue(check_columns_valid(puzzle1))
    def test_check_columns_valid_Duplicates_False_2(self):
        self.assertFalse(check_columns_valid(puzzle3))

    def test_checkZeros_Zeros_False_1(self):
        self.assertFalse(checkZeros(puzzle1))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
