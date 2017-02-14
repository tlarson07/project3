#Tanner Larson
#
#Project3
#Instructor: Julie Workman

from solverFuncs import *

def main():
    puzzle = initializePuzzle()
    cages = get_cages()
    cellIndex = 0
    checks = 0
    backtracks = 0

    while check_valid(puzzle,cages) and checkZeros(puzzle) == False:
        checks += 1
        cellValue = getCellValue(puzzle, cellIndex) + 1
        puzzle = updatePuzzle(puzzle,cellValue,cellIndex)
        while check_valid(puzzle, cages) == False and cellValue <=5:
            cellValue = getCellValue(puzzle, cellIndex) + 1
            puzzle = updatePuzzle(puzzle,cellValue,cellIndex)
        if cellValue > 5:
            puzzle = updatePuzzle(puzzle,0,cellIndex)
            cellIndex -= 1
            backtracks += 1
            continue
        cellIndex +=1


    print("\n---Solution---\n")
    for row in puzzle:
        for i in row:
            print(i, "", end ="")
        print()
    print()
    print("checks:", checks, "backtracks", backtracks)

if __name__ =='__main__':
    main()
