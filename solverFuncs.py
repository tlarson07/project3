#Tanner Larson
#
#Project3
#Julie Workman

puzzle = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]

def initializePuzzle():
    """
    returns puzzle filled with zeros

    """
    puzzle = []
    row = [0 for a in range(5)]
    return([row for b in range(5)])

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

def cellLocation(puzzle, cellIndex):
    """
    returns cell for for given cell index

    Arguments:
    puzzle -- (list of lists)
    cellIndex   -- (int) index of cell between 0 and 24
    """
    row = cellIndex // 5
    col = cellIndex % 5

    return(puzzle[row][col])

def checkColummValid(puzzle, columnIndex):
    """
    returns True is no duplicates in a single column

    Arguments
    puzzle -- (list of lists)
    columnIndex -- (int) between 0 and 4 representing column being checked
    """
    numCounter = dict()
    col= list()
    for i in range(5):
        col.append(puzzle[i][columnIndex])

    for i in col:
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

def check_cages_valid(puzzle,cages):
    pass

def check_valid(puzzel,cages):
    pass
