#Tanner Larson
#
#Project3
#Julie Workman

puzzle = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]

def check_valid(puzzel,cages):
    pass

def check_cages_valid(puzzle,cages):
    pass

def check_columns_valid(puzzle):
    pass

def check_columm_valid(puzzle): 
    pass

def check_rows_valid(puzzle):
    pass

def check_row_valid(puzzle):
    pass

def get_cages(): #FIGURE OUT HOW TO TEST THIS!!!!!
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
