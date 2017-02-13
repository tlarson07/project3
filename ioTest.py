#Tanner Larson
#
#Project3: ioTests
#Instructor: Julie Workman

from solverFuncs import *

puzzle = [[3,5,2,1,4],[5,1,3,4,2],[2,4,1,5,3],[1,2,4,3,5],[4,3,5,2,1]] #correct puzzle
puzzle = [[1,2,3,4,5],[3,1,4,5,2],[2,5,1,3,4],[5,4,2,1,3],[4,3,5,2,1]]  #correct puzzle
cages = get_cages()
print("\n")
print(initializePuzzle())
print("Rows valid:", check_rows_valid(puzzle))
print("Columns valid:", check_columns_valid(puzzle))
print("Cages valid:", check_cages_valid(puzzle,cages))
print("\nPUZZLE VALID =", check_valid(puzzle, cages))
