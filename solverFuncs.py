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
    return[row for b in range(5)]

def check_valid(puzzel,cages):
    pass

def check_cages_valid(puzzle,cages):
    pass

def check_columns_valid(puzzle):
    pass

def checkColummValid(puzzle):
    pass

def check_rows_valid(puzzle):
    for row in range(len(puzzle)):
        if checkRowValid(puzzle, row) == False:
            return(False)
    return(True)


def checkRowValid(puzzle, rowIndex):
    """
    returns True if no duplicates in a single row

    Arguments:
    puzzle -- (list of lists)
    row    -- (list) of numbers from puzzle
    """
    numCounter = dict()
    row = puzzle[rowIndex]
    for i in row:
        numCounter[i] = numCounter.get(i,0) + 1
    for i in numCounter:
        if numCounter[i] > 1:
            return(False)
    return(True)

def get_cages():
    """
    returns list of cages

    """
    cages = []
    numberOfCages = int(input("Number of cages: "))
    for i in range(numberOfCages):
        cage = input("Cage number %d: " %i).split()
        cages.append([int(i) for i in cage])
    return cages

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
