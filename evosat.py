"""
Document: sudoku_loader.py
Made by: Romeo Goosens, Joe Harrison
UVA_numbers: 10424458, 11770430
"""

"""
The implementation of this Sudoku solver is based on the paper:

    "A SAT-based Sudoku solver" by Tjark Weber

    https://www.lri.fr/~conchon/mpri/weber.pdf

If you want to understand the code below, in particular the function valid(),
which calculates the 324 clauses corresponding to 9 cells, you are strongly
encouraged to read the paper first.  The paper is very short, but contains
all necessary information.
"""

#import pycosat
import numpy as np
import cProfile
from pprint import pprint
import heapq
import random
from generation import Generation
from multiprocessing import Process, Value, Array, Pipe, Pool
import os

def read_cell(i, j,sol):
    for d in range(1, 10):
        if v(i, j, d) in sol:
            return d


def v(i, j, d):
    """
    Return the number of the variable of cell i, j and digit d,
    which is an integer in the range of 1 to 729 (including).
    """
    return 81 * (i - 1) + 9 * (j - 1) + d


def sudoku_clauses():
    """
    Create the (11745) Sudoku clauses, and return them as a list.
    Note that these clauses are *independent* of the particular
    Sudoku puzzle at hand.
    """
    res = []
    # for all cells, ensure that the each cell:
    for i in range(1, 10):
        for j in range(1, 10):
            # denotes (at least) one of the 9 digits (1 clause)
            res.append([v(i, j, d) for d in range(1, 10)])
            # does not denote two different digits at once (36 clauses)
            for d in range(1, 10):
                for dp in range(d + 1, 10):
                    res.append([-v(i, j, d), -v(i, j, dp)])

    def valid(cells):
        # Append 324 clauses, corresponding to 9 cells, to the result.
        # The 9 cells are represented by a list tuples.  The new clauses
        # ensure that the cells contain distinct values.
        for i, xi in enumerate(cells):
            for j, xj in enumerate(cells):
                if i < j:
                    for d in range(1, 10):
                        res.append([-v(xi[0], xi[1], d), -v(xj[0], xj[1], d)])

    # ensure rows and columns have distinct values
    for i in range(1, 10):
        valid([(i, j) for j in range(1, 10)])
        valid([(j, i) for j in range(1, 10)])
    # ensure 3x3 sub-grids "regions" have distinct values
    for i in 1, 4, 7:
        for j in 1, 4 ,7:
            valid([(i + k % 3, j + k // 3) for k in range(9)])

    assert len(res) == 81 * (1 + 36) + 27 * 324
    return res


# def solve(grid):
#     """
#     solve a Sudoku grid inplace
#     """
#     clauses = sudoku_clauses()
#     for i in range(1, 10):
#         for j in range(1, 10):
#             d = grid[i - 1][j - 1]
#             # For each digit already known, a clause (with one literal).
#             # Note:
#             #     We could also remove all variables for the known cells
#             #     altogether (which would be more efficient).  However, for
#             #     the sake of simplicity, we decided not to do that.
#             if d:
#                 clauses.append([v(i, j, d)])
#
#     # solve the SAT problem
#     sol = set(pycosat.solve(clauses))
#
#     def read_cell(i, j):
#         # return the digit of cell i, j according to the solution
#         for d in range(1, 10):
#             if v(i, j, d) in sol:
#                 return d
#
#     for i in range(1, 10):
#         for j in range(1, 10):
#             grid[i - 1][j - 1] = read_cell(i, j)

#Checks whether one of the literals in the clause is in the assignment
def checkClause(mult,clause):
    for literal in clause:
        if(mult[abs(literal) - 1] == literal):
            return 1
    return 0

def checkSatPerClause(assignment,clauses):
    vars = np.array([i for i in range(1,730)])
    assignment = np.array(assignment)
    mult = np.multiply(vars,assignment)
    mult = mult.reshape(729)
    satPerClause = 0
    for idx, clause in enumerate(clauses):
        satPerClause += checkClause(mult,clause)
    return satPerClause


def assignmentToGrid(assignment):
    vars = np.array([i for i in range(1, 730)])
    mult = np.multiply(vars, assignment)

    grid = np.zeros((9,9))
    for i in range(1, 10):
        for j in range(1, 10):
            grid[i - 1][j - 1] = read_cell(i, j,mult)
    return grid

# Filter known literals
def filterKnownLiterals(truthAssignment):
    for i in range(len(truthAssignment)):
        truthAssignment[i][fixedLiteralsT] = 1
        truthAssignment[i][fixedLiteralsF] = -1

    return truthAssignment

#E.g. Takes assignment1 = [1,1,-1,-1] and assignment2 = [-1,-1,1,1] and randomly select split point= 1 -> new1 = [1,1,1,1] and new2 = [-1,-1,-1,-1]
def crossover(assignment1,assignment2):
    #splitPoint = np.random.randint(1,729)
    splitPoint = 365
    assignment1 = assignment1.reshape(729)
    assignment2 = assignment2.reshape(729)

    new1 = np.concatenate((assignment1[:splitPoint],assignment2[splitPoint:]),axis=0)
    new2 = np.concatenate((assignment2[:splitPoint],assignment1[splitPoint:]),axis=0)

    return (new1,new2)

#E.g. Takes assignment = [1,1,-1,-1], and randomly flips assignment with mutation rate -> [-1,1,-1,-1]
def mutate(assignment):
    mutationrate = 1 / (len(assignment) - len(fixedLiteralsT) - len(fixedLiteralsF))
    flip = np.array(np.random.choice(a=[-1, 1], size=(1, len(assignment)), p=[mutationrate, 1 - mutationrate]))[0]
    flip[fixedLiteralsT] = 1
    flip[fixedLiteralsF] = -1
    mult = np.multiply(flip,assignment)
    return mult


# Generate children functions #
def createRandomChildren(n, num_variables):
    random = []
    for i in range(0, n):
        random.append(np.array(np.random.choice(a=[-1, 1], size=(1, num_variables)))[0])
    return random

def createCrossOvers(a, b, n):
    #check if a and b are not smaller than n, if so pick smallest
    if(len(a) < n or len(b) < n):
        n =  len(a) if len(a) < len(b) else len(b)

    cross = []
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if(len(cross) == n):
                break;
            cross.append(crossover(a[i],b[j])[0])
            cross.append(crossover(a[i],b[j])[1])

    return cross


def createNewGeneration(generation, scorePerChild, ppid, pid):
    if(generation.generation_i >= 10300):
        growth = int(1*(generation.generation_i / 300))
    else:
        growth = 0


    n_random = 6 + growth
    n_elite = 2 + growth
    n_mutated_elite = 2 + growth

    #Crossover Rates
    n_crossover_mutated_elite = 2 + growth
    n_crossover_mutated_random = 2  + growth
    n_crossover_unmutated_elite =  2 + growth
    n_crossover_unmutated_random =  2 + growth

    #Gets indices of the elite children of population
    idxs_elite = heapq.nlargest(n_elite, range(len(scorePerChild)), key=scorePerChild.__getitem__)
    idxs_elite = np.array(idxs_elite)

    #print information about the best elite
    if(generation.generation_i % 20 == 0):
        print(str(scorePerChild[idxs_elite[0]]) + "/" + str(generation.num_clauses), generation.generation_i, len(generation.children), ppid, pid)

    #Create children
    elite_children = np.array(generation.children[idxs_elite])
    random_children = np.array(createRandomChildren(n_random, generation.num_variables))

    if(n_mutated_elite > len(elite_children)):
        print("n_mutated_elite > elite_children")
        n_mutated_elite = len(elite_children)
    mutate_elite = np.array([mutate(elite_children[i]) for i in (0, n_mutated_elite-1)])

    #Create Crossovers
    crossover_unmutated_random  = np.array(createCrossOvers(elite_children, random_children, n_crossover_unmutated_random))
    crossover_unmutated_elite   = np.array(createCrossOvers(elite_children, elite_children, n_crossover_unmutated_elite))
    crossover_mutated_random    = np.array(createCrossOvers(mutate_elite, random_children, n_crossover_mutated_random))
    crossover_mutated_elite     = np.array(createCrossOvers(elite_children, elite_children, n_crossover_mutated_elite))

    # @todo make this more clean
    temp = np.array([])
    temp = np.append(temp, elite_children)
    temp = np.append(temp,random_children)
    temp = np.append(temp,mutate_elite)
    temp = np.append(temp,crossover_unmutated_random)
    temp = np.append(temp,crossover_unmutated_elite)
    temp = np.append(temp,crossover_mutated_random)
    temp = np.append(temp,crossover_mutated_elite)
    temp = np.array(temp)
    temp = temp.reshape(int(len(temp)/729), 729)

    children = np.array(temp)
    return Generation(generation, children, generation.num_clauses, generation.num_variables)

fixedLiteralsT = []
fixedLiteralsF = []
scorePerChild = []
SAT = False

def checkScoresChildren(clauses, children):
    scorePerChild = np.zeros(children.shape[0])
    for idx, assignment in enumerate(children):
        score = checkSatPerClause(assignment,clauses)
        if score == len(clauses):
            print(assignmentToGrid(assignment))
            return
        scorePerChild[idx] = score

    return scorePerChild


from functools import partial
import time

def loopOverChildren(generation, clauses, generation_i, maxgenerations):
    #Runs until assignment with all clauses SAT is found
    if hasattr(os, 'getppid'):  # only available on Unix
        print('parent process:', os.getppid())
        print('process id:', os.getpid())

    n_threads = 4
    pool = Pool(n_threads)
    while generation_i != maxgenerations:
        generation.children = filterKnownLiterals(generation.children)
        nchilds = len(generation.children)
        proccesses = []
        keyss = []
        scorePerChild = np.array([])


        for i in range(0, n_threads):
            children = generation.children[int(nchilds / n_threads) * i: int(nchilds / n_threads) * (i+1)]
            keyss.append(children)

        func = partial(checkScoresChildren, clauses)
        values = pool.map(func, keyss)


        for value in values:
            if(type(value) == type(np.array([]))):
                if(scorePerChild == np.array([])):
                    scorePerChild = value
                else:
                    scorePerChild = np.append(scorePerChild , value)
            else:
                print("IK DENK SAT")
                #We dont need to join :) I think :P
                return
        scorePerChild = scorePerChild.flatten()
        generation = createNewGeneration(generation, scorePerChild, os.getppid(),os.getpid())

        generation_i += 1
    pool.close()
    pool.join()

    print("UNSAT")
    return

#Tries to find assignment using an evolutionairy algorithm
def evosolve(grid):
    #Get clauses in CNF form from grid
    clauses = sudoku_clauses()

    #Number of variables TODO make dynamic in size
    num_variables = 9*9*9

    # for i in range(1,10):
    #     for j in range(1,10):
    #         d = grid[i - 1][j - 1]
    #         if (d != 0):
    #             for k in range(1, 10):
    #                 if (d == k):
    #                     literal = v(i, j, d)
    #                     fixedLiteralsT.append(literal - 1)
    #                     #clauses.append([literal])
    #                     # for x in range(1, 10):
    #                     #     if (x!= j):
    #                     #         literalj = v(i, x, d) - 1
    #                     #         if(literalj not in fixedLiteralsF):
    #                     #             fixedLiteralsF.append(literalj)
    #                     #     if (x!= i):
    #                     #         literali = v(x, j, d) - 1
    #                     #         if(literali not in fixedLiteralsF):
    #                     #             fixedLiteralsF.append(literali)
    #                 else:
    #                     literal = v(i,j,k)
    #                     if (literal not in fixedLiteralsF):
    #                        fixedLiteralsF.append(literal - 1)

    # #Append clauses with filled in literals TODO make dynamic in size
    for i in range(1, 10):
        for j in range(1, 10):
            d = grid[i - 1][j - 1]
            if(d != 0):
                for k in range (1,10):
                    if(d == k):
                        literal = v(i, j, d)
                        clauses.append([literal])
                        fixedLiteralsT.append(literal - 1)
                        # for x in range((i // 3) * 3, (3 * (1 + (i // 3)))):
                        #     for y in range((j // 3) * 3, (3 * (1 + (j // 3))) - 1):
                        #         literalxy = v(x+1, y+1, d) - 1
                        #         print(literalxy)
                        #         if(literalxy>729):
                        #             print(literalxy,x,y,d,i,j)
                        #         if(literalxy not in fixedLiteralsF):
                        #             fixedLiteralsF.append(literalxy)

                        for x in range(1, 10):
                            if (x!=j):
                                literalj = v(i, x, d) - 1
                                if(literalj not in fixedLiteralsF):
                                    fixedLiteralsF.append(literalj)
                            if (x!= i):
                                literali = v(x, j, d) - 1
                                if(literali not in fixedLiteralsF):
                                    fixedLiteralsF.append(literali)
                    else:

                        literal = v(i, j, k) - 1
                        if(literal not in fixedLiteralsF):
                            fixedLiteralsF.append(literal)

    print(fixedLiteralsT,fixedLiteralsF)

    #Number of clauses
    num_clauses = len(clauses)

    #Define population size
    populationSize = 16

    #Initial assignment of variables
    assignment = np.random.choice(a=[-1, 1], size=(populationSize, num_variables))

    #Keeps track of generation
    generation_i = 0
    maxgenerations = 100000

    generation = Generation(None, assignment, num_clauses, num_variables)

    proccesses = []
    for num in range(1):
        loopOverChildren(generation, clauses, generation_i, maxgenerations)
        p = Process(target=loopOverChildren, args=(generation, clauses, generation_i, maxgenerations))
        proccesses.append(p)
        p.start()


    for p in proccesses:
        p.join


if __name__ == '__main__':
    random.seed(2)
    np.random.seed(2)
    # hard Sudoku problem, see Fig. 3 in paper by Weber
    hard = [[0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 3],
            [0, 7, 4, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 0, 2],
            [0, 8, 0, 0, 4, 0, 0, 1, 0],
            [6, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 7, 8, 0],
            [5, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0]]

    simple = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    extremely_simple = [[1, 2, 6, 4, 3, 7, 9, 5, 8],
           [8, 0, 5, 6, 2, 1, 4, 7, 3],
           [3, 7, 4, 9, 8, 0, 0, 2, 6],
           [4, 5, 7, 1, 9, 3, 0, 6, 2],
           [9, 8, 3, 2, 4, 6, 5, 1, 7],
           [6, 0, 0, 5, 7, 8, 3, 9, 4],
           [2, 6, 9, 3, 1, 0, 7, 8, 5],
           [0, 4, 8, 7, 6, 9, 2, 0, 0],
           [7, 3, 1, 0, 5, 2, 6, 0, 0]]

    print(evosolve(hard))



    #solve(hard)
    #pprint(hard)
    #assert [[1, 2, 6, 4, 3, 7, 9, 5, 8],
    #        [8, 9, 5, 6, 2, 1, 4, 7, 3],
    #        [3, 7, 4, 9, 8, 5, 1, 2, 6],
    #        [4, 5, 7, 1, 9, 3, 8, 6, 2],
    #        [9, 8, 3, 2, 4, 6, 5, 1, 7],
    #        [6, 1, 2, 5, 7, 8, 3, 9, 4],
    #        [2, 6, 9, 3, 1, 4, 7, 8, 5],
    #        [5, 4, 8, 7, 6, 9, 2, 3, 1],
    #        [7, 3, 1, 8, 5, 2, 6, 4, 9]] == hard
