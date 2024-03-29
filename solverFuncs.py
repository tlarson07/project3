#Tanner Larson
#
#Project3
#Julie Workman

#puzzle = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]

def initializePuzzle():
    """
    returns puzzle filled with zeros

    """
    return([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

def get_cages():
    """
    returns list of cages

    """
    cages = []
    numberOfCages = int(input("Number of cages: "))

    for i in range(numberOfCages):
        cage = input("Cage number %d: " %i).split() #allows for mulitple input in a single line
        cages.append([int(i) for i in cage]) #addes user input to a list, casting each num as an int, and adds that list to cages
    return(cages)

def getCellValue(puzzle, cellIndex):
    """
    returns cell value for given cell index

    Arguments:
    puzzle -- (list of lists)
    cellIndex   -- (int) index of cell between 0 and 24
    """
    row = cellIndex // 5
    col = cellIndex % 5

    return(puzzle[row][col])

def updatePuzzle(puzzle, cellValue, cellIndex):
    row = cellIndex // 5
    col = cellIndex % 5
    puzzle[row][col] = cellValue
    return(puzzle)

def checkColummValid(puzzle, columnIndex):
    """
    returns True if no duplicates in a single column

    Arguments
    puzzle -- (list of lists)
    columnIndex -- (int) between 0 and 4 representing column being checked
    """
    numCounter = dict()
    col= list()
    for i in range(5):
        col.append(puzzle[i][columnIndex])

    for i in col:
        if i < 1:
            continue
        numCounter[i] = numCounter.get(i,0) + 1 #creates a dictionary representing the number of occurances for each number in a list
    for i in numCounter:
        if numCounter[i] > 1: #if the number of occurances is greater than one
            return(False)
    return(True)

def check_columns_valid(puzzle):
    for col in range(len(puzzle)):
        if checkColummValid(puzzle, col) == False:
            return(False)
    return(True)

def checkRowValid(puzzle, rowIndex):
    """
    returns True if no duplicates in a single row

    Arguments:
    puzzle -- (list of lists)
    rowIndex    -- (int) between 0 and 4 representing row being checked
    """
    numCounter = dict()
    row = puzzle[rowIndex]

    for i in row:
        if i < 1:
            continue
        numCounter[i] = numCounter.get(i,0) + 1 #creates a dictionary representing the number of occurances for each number in a list
    for i in numCounter:
        if numCounter[i] > 1: #if the number of occurances is greater than one
            return(False)
    return(True)

def check_rows_valid(puzzle):
    for row in range(len(puzzle)):
        if checkRowValid(puzzle, row) == False:
            return(False)
    return(True)

def checkCageValid(puzzle, cages, cageIndex):
    """
    returns True if sum of cage's cells are less than or equal to the required sum

    Arguments :
    puzzle    -- (list of lists)
    cages     -- (list of lists) cage contains: sum, numCells, cageIndex
    cageIndex -- (int) between 0 and numCages
    """
    cage = cages[cageIndex]
    cageSum = cage[0]
    puzzleIndexes = cage[2:]
    puzzleValues = [getCellValue(puzzle, i) for i in puzzleIndexes]
    cageSumTest = 0

    for cellIndex in puzzleIndexes: #sum of cage
        cageSumTest += getCellValue(puzzle, cellIndex)

    if checkZeros(puzzleValues) == True and cageSum == cageSumTest:
        return(True)
    elif checkZeros(puzzleValues) == False and cageSumTest < cageSum:
        return(True)
    else:
        return(False)



def check_cages_valid(puzzle,cages):
    for i in range(len(cages)):
        if checkCageValid(puzzle, cages, i) == False:
            return(False)
    return(True)

def check_valid(puzzle,cages):
    """
    returns True if puzzle is still valid for the following: row, columns, and cages

    Arguments :
    puzzle    -- (list of lists)
    cages     -- (list of lists) cage contains: sum, numCells, cellIndexes
    """
    if check_cages_valid(puzzle,cages) and check_rows_valid(puzzle) and check_columns_valid(puzzle) == True:
        return(True)
    return(False)

def checkZeros(puzzle):
    """
    returns True if puzzle contains no zeros
    """
    for i in puzzle:
        if i == 0:
            return(False)
    return(True)

def printPuzzle(puzzle):
    for row in puzzle:
        for cell in row:
            print(cell,"",end="")
        print()
