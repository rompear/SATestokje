"""
Document: sudoku_loader.py
Made by: Romeo Goosens, Joe Harrison
UVA_numbers: 10424458, 11770430
"""
import pycosat
import subprocess
from sudoko_loader import Loader

"""
Mapping the index of a sudoku to a variable
"""
def v(i, j, d, dim):
    return dim*dim*(i-1) + dim*(j-1) + d

"""
Make the claues of a given sudokus
"""
def sudoku_clauses(coord1, coord2, dim):
    (x1,y1) = coord1
    (x2,y2) = coord2

    res = []
    # for all cells, ensure that the each cell:
    for i in range(1, 10):
        for j in range(1, 10):
            # denotes (at least) one of the 9 digits (1 clause)
            cltemp = ([v(i, j, d, dim) for d in range(1, 10)])
            res.append(cltemp)
            # does not denote two different digits at once (36 clauses)
            for d in range(1, 10):
                for dp in range(d + 1, 10):
                    res.append([-v(i, j, d, dim), -v(i, j, dp, dim)])

    if(x1 is not 1 and y2 is not 1):
        for i in range(y2+1, y1+y2):
            for j in range(x1+1, x1+x2):
                # denotes (at least) one of the 9 digits (1 clause)
                cl1 = [v(i, j, d, dim) for d in range(1, 10)]
                # if(cl1 not in res):
                res.append(cl1)
                # does not denote two different digits at once (36 clauses)
                for d in range(1, 10):
                    for dp in range(d + 1, 10):
                        cl2 = [-v(i, j, d, dim), -v(i, j, dp, dim)]
                        if(cl2 not in res):
                            res.append(cl2)

    def valid(cells):
        # Append 324 clauses, corresponding to 9 cells, to the result.
        # The 9 cells are represented by a list tuples.  The new clauses
        # ensure that the cells contain distinct values.
        for i, xi in enumerate(cells):
            for j, xj in enumerate(cells):
                if i < j:
                    for d in range(1, 10):
                        cl = [-v(xi[0], xi[1], d,dim), -v(xj[0], xj[1], d,dim)]
                        if(cl not in res):
                            res.append(cl)


    # ensure rows and columns have distinct values
    for i in range(1, 10):
        valid([(i, j) for j in range(1, 10)])
        valid([(j, i) for j in range(1, 10)])

    if(x1 is not 1 and y2 is not 1):
        # ensure rows and columns have distinct values
        for i in range(y2+1, y1+y2):
            valid([(i, j) for j in range(x1+1, x1+x2)])
            valid([(j, i) for j in range(x1+1, x1+x2)])

    # ensure 3x3 sub-grids "regions" have distinct values
    for i in 1, 4, 7:
        for j in 1, 4 ,7:
            valid([(i + k % 3, j + k // 3) for k in range(9)])

    if(x1 is not 1 and y2 is not 1):
        for i in x1 + 1, x1 + 4, x1 + 7:
            for j in x1 + 1, x1 + 4, x1 + 7:
                valid([(i + k % 3, j + k // 3) for k in range(9)])

    # assert len(res) == 81 * (1 + 36) + 27 * 324
    return res

"""
Determine the coordinates of the two sudokus given an overlapping sudoku
"""
def getCoords(grid):
    x1 = 0
    y1 = len(grid) - 1

    for i in range(0,len(grid)):
        if(grid[y1][i] is not -1):
            break
        else:
            x1 = i

    for i in range(len(grid)-1,-1,-1):
        if(grid[i][x1] is not -1):
            break
        else:
            y1 = i

    x2 = len(grid) - 1
    y2 = 0

    for i in range(len(grid)-1,-1,-1):
        if(grid[y2][i] is not -1):
            break
        else:
            x2 = i

    for i in range(0,len(grid)):
        if(grid[i][x2] is not -1):
            break
        else:
            y2 = i


    return (x1 + 1,y1 + 1),(x2 + 1,y2 + 1)



"""
Write the zchaff files to csv file.
"""
def writeToCSV(lines, file, type):
    import csv
    try:
        with open(file, 'a') as csvfile:
            fieldnames = ['max_decision', '#decision', 'detail', '#vars','#clauses','#literals','added_confilcts', 'shrink', 'deleted_conflict_clauses', 'delete_clauses', 'added_confilcts_literals', 'deleted_total_literals', 'implications', 'run_time', 'type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writerow({fieldnames[0]: lines[0 + 6], fieldnames[1]: lines[1 + 6], fieldnames[2]: lines[2 + 6], fieldnames[3]: lines[3 + 6], fieldnames[4]: lines[4 + 6], fieldnames[5]: lines[5 + 6], fieldnames[6]: lines[6 + 6], fieldnames[7]: lines[7 + 6], fieldnames[8]: lines[8 + 6], fieldnames[9]: lines[9 + 6], fieldnames[10]: lines[10 + 6], fieldnames[11]: lines[11 + 6], fieldnames[12]: lines[12 + 6], fieldnames[13]: lines[13 + 6], fieldnames[14]: type})

    except Exception as e:
        print(lines)

"""
Solve a sudoku
"""
def solve(grid, n_sudoku, type, percent):
    (x1,y1), (x2,y2) = getCoords(grid)
    dim = max(len(grid),len(grid[0]))
    """
    solve a Sudoku grid inplace
    """
    clauses = sudoku_clauses((x1,y1), (x2,y2),dim)
    for i in range(1, 10):
        for j in range(1, 10):
            d = grid[i - 1][j - 1]
            # For each digit already known, a clause (with one literal).
            # Note:
            #     We could also remove all variables for the known cells
            #     altogether (which would be more efficient).  However, for
            #     the sake of simplicity, we decided not to do that.
            if d:
                clauses.append([v(i, j, d, dim)])

    if(x1 is not 1 and y2 is not 1):
        for i in range(y2+1, y1+y2):
            for j in range(x1+1, x1+x2):
                d = grid[i - 1][j - 1]
                # For each digit already known, a clause (with one literal).
                # Note:
                #     We could also remove all variables for the known cells
                #     altogether (which would be more efficient).  However, for
                #     the sake of simplicity, we decided not to do that.
                if d:
                    lit = [v(i, j, d, dim)]
                    if(lit not in clauses):
                        clauses.append(lit)


    #Get number of variables
    import numpy as np
    a = np.array(clauses)
    a = np.unique(a)

    # solve the SAT problem
    sol = set(pycosat.solve(clauses))

    # Write cnf form
    outfile = open('sudoku.cnf', 'w')
    print("p cnf", len(a), len(clauses), file=outfile)
    for clause in clauses:
        string = ''
        for var in clause:
            string = string + str(var) + ' '
        string = string[:-1]
        outfile.write('\n'+string+' 0')
    outfile.close()

    # Start Zchaff process
    cmd = './zchaff64/zchaff ' + 'sudoku.cnf' + ' > solver-output.zchaff'
    process = subprocess.Popen(cmd ,stdout=subprocess.PIPE, shell=True)
    process.wait()
    with open('solver-output.zchaff', 'r') as f:
        lines = []
        for line in f:
            lines.append(line)
        writeToCSV(lines, 'results/'+str(percent)+'procent/sudoku_'+str(n_sudoku)+'.csv', type)


    """
    Inner function to read cells
    """
    def read_cell(i, j):
        # return the digit of cell i, j according to the solution
        for d in range(1, 10):
            if v(i, j, d, dim) in sol:
                return d

    # Decode the sudoku's
    for i in range(1, y1+y2):
        for j in range(1, x1+x2):

            if(grid[i-1][j-1] is not -1):
                grid[i - 1][j - 1] = str(read_cell(i, j))

    for i in range(1, 10):
        for j in range(1, 10):
            if(grid[i-1][j-1] is not -1):
                grid[i - 1][j - 1] = str(read_cell(i, j))

"""
Make the overlap sudoku in two seperate ones
"""
def getSubGrids(grid):
    coords = getCoords(grid)
    overlap1 = []
    overlap2 = []
    for i in range(9):
        row = []
        for j in range(9):
            row.append(int(grid[i][j]))
        overlap1.append(row)
    for i in range(coords[1][1],len(grid)):
        row = []
        for j in range(coords[0][0],len(grid[0])):
            row.append(int(grid[i][j]))
        overlap2.append(row)
    return overlap1, overlap2

"""
Get the total number of cells:
"""
def getTotalNumbers(grid):
    totalNumbers = 0
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if(grid[i][j]>0):
                totalNumbers += 1
    return totalNumbers

"""
Get the total number of cells in the overlapping region:
"""
def getNumbersInOverlap(grid):
    coords = getCoords(grid)
    numbersInOverlap = 0
    for i in range(coords[0][0],coords[0][1] - 1):
        for j in range(coords[1][1],coords[1][0] - 1):
            if(grid[i][j]>0):
                numbersInOverlap += 1
    return numbersInOverlap

if __name__ == '__main__':
    from pprint import pprint

    x = -1
    overlap = [[0,6,0,0,0,0,0,5,9,x,x,x,x,x,x],
               [9,3,0,4,8,0,0,0,0,x,x,x,x,x,x],
               [0,0,0,0,0,7,3,0,0,x,x,x,x,x,x],
               [0,5,0,0,1,0,0,4,6,x,x,x,x,x,x],
               [0,0,0,0,0,6,0,9,0,x,x,x,x,x,x],
               [0,8,1,2,0,0,0,0,0,x,x,x,x,x,x],
               [0,0,0,7,0,0,0,0,0,0,0,0,0,0,0],
               [8,0,4,0,0,1,0,0,0,0,0,0,6,0,0],
               [0,9,0,0,0,0,0,0,0,0,0,0,0,0,0],
               [x,x,x,x,x,x,0,0,0,0,0,9,5,3,0],
               [x,x,x,x,x,x,0,7,0,4,0,0,0,0,0],
               [x,x,x,x,x,x,5,8,0,0,1,0,0,9,0],
               [x,x,x,x,x,x,0,0,2,1,0,0,0,0,0],
               [x,x,x,x,x,x,0,0,0,0,9,8,0,6,1],
               [x,x,x,x,x,x,6,1,0,0,0,0,0,7,0]]

    overlappy =[[0,6,0,0,0,0,0,5,9,x,x,x,x,x,x,x],
                [9,3,0,4,8,0,0,0,0,x,x,x,x,x,x,x],
                [0,0,0,0,0,7,3,0,0,x,x,x,x,x,x,x],
                [0,5,0,0,1,0,0,4,6,x,x,x,x,x,x,x],
                [0,0,0,0,0,6,0,9,0,x,x,x,x,x,x,x],
                [0,8,1,2,0,0,0,0,0,x,x,x,x,x,x,x],
                [0,0,0,0,7,0,0,0,0,x,x,x,x,x,x,x],
                [8,0,4,0,0,1,0,3,5,7,8,0,0,0,0,0],
                [0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [x,x,x,x,x,x,x,0,0,0,0,0,0,0,0,0],
                [x,x,x,x,x,x,x,0,0,0,0,0,0,0,0,0],
                [x,x,x,x,x,x,x,0,0,0,0,0,0,0,0,0],
                [x,x,x,x,x,x,x,0,0,0,0,0,0,0,0,0],
                [x,x,x,x,x,x,x,0,6,0,0,0,0,0,0,0],
                [x,x,x,x,x,x,x,0,9,0,0,0,0,0,0,0],
                [x,x,x,x,x,x,x,0,0,0,0,0,0,0,0,0]]

    overlapland = [[0,2,0,0,0,0,0,0,0,x,x,x,x,x,x,x,x],
                   [0,0,0,6,0,0,0,0,3,x,x,x,x,x,x,x,x],
                   [0,7,4,0,8,0,0,0,0,x,x,x,x,x,x,x,x],
                   [0,0,0,0,0,3,0,0,2,x,x,x,x,x,x,x,x],
                   [0,8,0,0,4,0,0,1,0,x,x,x,x,x,x,x,x],
                   [6,0,0,5,0,0,0,0,0,x,x,x,x,x,x,x,x],
                   [0,0,0,0,1,0,7,8,0,x,x,x,x,x,x,x,x],
                   [5,0,0,0,0,9,0,0,0,x,x,x,x,x,x,x,x],
                   [0,0,0,0,0,0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [x,x, x, x, x, x, x, x, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [x,x, x, x, x, x, x, x, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [x,x, x, x, x, x, x, x, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [x,x, x, x, x, x, x, x, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [x,x, x, x, x, x, x, x, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [x,x, x, x, x, x, x, x, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [x,x, x, x, x, x, x, x, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [x,x, x, x, x, x, x, x, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    overlap1 = [[0,6,0,0,0,0,0,5,9],
               [9,3,0,4,8,0,0,0,0],
               [0,0,0,0,0,7,3,0,0],
               [0,5,0,0,1,0,0,4,6],
               [0,0,0,0,0,6,0,9,0],
               [0,8,1,2,0,0,0,0,0],
               [0,0,0,7,0,0,0,0,0],
               [8,0,4,0,0,1,0,0,0],
               [0,9,0,0,0,0,0,0,0]]

    overlap2 = [[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,6,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,9,5,3,0],
               [0,7,0,4,0,0,0,0,0],
               [5,8,0,0,1,0,0,9,0],
               [0,0,2,1,0,0,0,0,0],
               [0,0,0,0,9,8,0,6,1],
               [6,1,0,0,0,0,0,7,0]]


    overlap1, overlap2 = getSubGrids(overlappy)

    """
    This code block will compute all the sudoku's for every puched out percentaged and write statistics obtained from zchaff,
    to the corresponding csv files in the result folder
    """
    percent = [10, 20, 30, 40, 50, 60, 70 ,80, 90]
    for i in range(1,9):
        for k in percent:
            loader = Loader(i)
            loader.filter_sudoku(k / 100)
            for j, overlap_i in enumerate(loader.sudoku_array):
                print(j)
                overlap1, overlap2 = getSubGrids(overlap_i)
                solve(overlap1, i, '1', k)
                solve(overlap2, i, '2', k)
                solve(overlap_i, i, 'all', k)
        exit()
