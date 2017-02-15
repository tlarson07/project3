#Tanner Larson
#
#Project3: ioTests
#Instructor: Julie Workman

from solverFuncs import *

#puzzle = [[1,2,3,4,5],[3,1,4,5,2],[2,5,1,3,4],[0,0,0,0,0],[0,0,0,0,0]]
#puzzle = [[3,5,2,1,4],[5,1,3,4,2],[2,4,1,5,3],[1,2,4,3,5],[4,3,5,2,1]] #correct
puzzle = [[1,2,3,4,5],[3,1,4,5,2],[2,5,1,3,4],[5,4,2,1,3],[4,3,5,2,1]] #correct

cages = get_cages()
print("\n")
print("Rows valid:", check_rows_valid(puzzle))
print("Columns valid:", check_columns_valid(puzzle))
print("Cage1 valid:", checkCageValid(puzzle, cages, 0))
print("Cages valid:", check_cages_valid(puzzle,cages))
print("\nPUZZLE VALID =", check_valid(puzzle, cages))
