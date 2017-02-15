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

    while cellIndex < 25:
        cellValue = getCellValue(puzzle, cellIndex) + 1
        puzzle = updatePuzzle(puzzle,cellValue,cellIndex)
        printPuzzle(puzzle)
        checks +=1

        if check_valid(puzzle, cages) == True: #move to next index
            cellIndex += 1
        else:
            while cellValue >= 5: #backtracking
                printPuzzle(puzzle)
                puzzle = updatePuzzle(puzzle,0,cellIndex)
                cellIndex -= 1
                backtracks += 1
                cellValue = getCellValue(puzzle, cellIndex)

    print("\n---Solution---\n")
    printPuzzle(puzzle)
    print()
    print("checks:", checks, "backtracks", backtracks)

if __name__ =='__main__':
    main()
