import unittest
from solverFuncs import *

puzzle = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]

class TestCase(unittest.TestCase):
    def test_cellLocation_CorrectIndex_CorrectCell_1(self):
        self.assertAlmostEqual(cellLocation(puzzle, 0), 0)
    def test_cellLocation_CorrectIndex_CorrectCell_2(self):
        self.assertAlmostEqual(cellLocation(puzzle, 24), 24)
    def test_cellLocation_CorrectIndex_CorrectCell_3(self):
        self.assertAlmostEqual(cellLocation(puzzle,15), 15)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
