x = -1
n = 66
sudoku_array = [0]*66

sudoku_array[0] = [[6,3,4,8,9,7,2,1,5,x,x,x,x,x,x],
[1,7,2,3,4,5,6,9,8,x,x,x,x,x,x],
[9,5,8,6,1,2,3,7,4,x,x,x,x,x,x],
[2,6,3,5,7,8,9,4,1,x,x,x,x,x,x],
[4,8,1,9,6,3,7,5,2,x,x,x,x,x,x],
[7,9,5,4,2,1,8,3,6,x,x,x,x,x,x],
[3,1,7,2,5,6,4,8,9,3,1,7,2,5,6],
[5,4,6,7,8,9,1,2,3,4,6,5,7,8,9],
[8,2,9,1,3,4,5,6,7,8,2,9,1,3,4],
[x,x,x,x,x,x,6,5,4,1,3,2,8,9,7],
[x,x,x,x,x,x,2,9,8,7,4,6,5,1,3],
[x,x,x,x,x,x,3,7,1,9,5,8,4,6,2],
[x,x,x,x,x,x,8,3,6,2,7,1,9,4,5],
[x,x,x,x,x,x,9,4,2,5,8,3,6,7,1],
[x,x,x,x,x,x,7,1,5,6,9,4,3,2,8]]

sudoku_array[1] = [[5,2,1,3,6,4,9,7,8,x,x,x,x,x,x],
[8,4,3,5,9,7,6,1,2,x,x,x,x,x,x],
[9,7,6,8,1,2,3,5,4,x,x,x,x,x,x],
[1,3,2,4,5,6,7,8,9,x,x,x,x,x,x],
[6,9,4,1,7,8,2,3,5,x,x,x,x,x,x],
[7,8,5,2,3,9,1,4,6,x,x,x,x,x,x],
[2,1,7,6,4,5,8,9,3,7,5,6,4,1,2],
[3,5,8,9,2,1,4,6,7,8,1,2,5,9,3],
[4,6,9,7,8,3,5,2,1,4,9,3,6,7,8],
[x,x,x,x,x,x,1,4,2,5,6,7,3,8,9],
[x,x,x,x,x,x,3,5,8,2,4,9,1,6,7],
[x,x,x,x,x,x,6,7,9,1,3,8,2,4,5],
[x,x,x,x,x,x,2,1,4,9,7,5,8,3,6],
[x,x,x,x,x,x,7,3,5,6,8,4,9,2,1],
[x,x,x,x,x,x,9,8,6,3,2,1,7,5,4]]

sudoku_array[2] = [[3,7,9,1,2,4,5,8,6,x,x,x,x,x,x],
[1,2,8,3,5,6,4,9,7,x,x,x,x,x,x],
[4,5,6,7,8,9,3,2,1,x,x,x,x,x,x],
[2,9,4,5,7,1,8,6,3,x,x,x,x,x,x],
[5,3,7,6,9,8,2,1,4,x,x,x,x,x,x],
[6,8,1,2,4,3,9,7,5,x,x,x,x,x,x],
[9,4,5,8,6,7,1,3,2,4,5,6,7,8,9],
[7,1,2,9,3,5,6,4,8,1,7,9,2,3,5],
[8,6,3,4,1,2,7,5,9,2,3,8,1,4,6],
[x,x,x,x,x,x,2,6,1,3,8,4,9,5,7],
[x,x,x,x,x,x,5,7,3,6,9,1,8,2,4],
[x,x,x,x,x,x,8,9,4,7,2,5,3,6,1],
[x,x,x,x,x,x,3,1,5,8,4,7,6,9,2],
[x,x,x,x,x,x,4,2,6,9,1,3,5,7,8],
[x,x,x,x,x,x,9,8,7,5,6,2,4,1,3]]

sudoku_array[3] = [[7,5,2,9,6,4,1,3,8,x,x,x,x,x,x],
[1,4,8,3,2,5,6,9,7,x,x,x,x,x,x],
[9,6,3,8,7,1,5,4,2,x,x,x,x,x,x],
[3,1,6,5,9,2,7,8,4,x,x,x,x,x,x],
[4,2,7,6,1,8,9,5,3,x,x,x,x,x,x],
[5,8,9,7,4,3,2,6,1,x,x,x,x,x,x],
[6,7,4,2,8,9,3,1,5,4,6,7,2,8,9],
[8,9,5,1,3,7,4,2,6,5,8,9,1,3,7],
[2,3,1,4,5,6,8,7,9,1,2,3,4,5,6],
[x,x,x,x,x,x,1,3,2,6,4,5,9,7,8],
[x,x,x,x,x,x,6,4,7,2,9,8,5,1,3],
[x,x,x,x,x,x,9,5,8,3,7,1,6,4,2],
[x,x,x,x,x,x,2,6,1,7,3,4,8,9,5],
[x,x,x,x,x,x,5,8,3,9,1,2,7,6,4],
[x,x,x,x,x,x,7,9,4,8,5,6,3,2,1]]

sudoku_array[4] = [[9,6,8,3,4,7,1,2,5,x,x,x,x,x,x],
[4,7,5,1,9,2,8,3,6,x,x,x,x,x,x],
[2,1,3,6,8,5,9,4,7,x,x,x,x,x,x],
[8,9,4,7,6,3,2,5,1,x,x,x,x,x,x],
[7,5,1,9,2,4,3,6,8,x,x,x,x,x,x],
[6,3,2,8,5,1,4,7,9,x,x,x,x,x,x],
[3,4,7,5,1,9,6,8,2,9,5,3,4,7,1],
[1,2,6,4,7,8,5,9,3,4,7,1,2,6,8],
[5,8,9,2,3,6,7,1,4,6,2,8,9,5,3],
[x,x,x,x,x,x,8,4,6,5,9,7,1,3,2],
[x,x,x,x,x,x,9,5,7,3,1,2,6,8,4],
[x,x,x,x,x,x,2,3,1,8,6,4,5,9,7],
[x,x,x,x,x,x,1,2,5,7,8,9,3,4,6],
[x,x,x,x,x,x,3,6,8,2,4,5,7,1,9],
[x,x,x,x,x,x,4,7,9,1,3,6,8,2,5]]

sudoku_array[5] = [[4,5,3,8,9,7,2,6,1,x,x,x,x,x,x],
[6,9,7,4,1,2,5,8,3,x,x,x,x,x,x],
[8,1,2,5,3,6,7,9,4,x,x,x,x,x,x],
[7,2,6,9,8,4,3,1,5,x,x,x,x,x,x],
[9,8,1,7,5,3,4,2,6,x,x,x,x,x,x],
[5,3,4,2,6,1,8,7,9,x,x,x,x,x,x],
[1,7,9,3,4,8,6,5,2,9,7,8,4,1,3],
[2,4,5,6,7,9,1,3,8,5,4,6,2,9,7],
[3,6,8,1,2,5,9,4,7,3,1,2,5,6,8],
[x,x,x,x,x,x,4,2,5,7,8,9,6,3,1],
[x,x,x,x,x,x,7,1,9,6,2,3,8,5,4],
[x,x,x,x,x,x,3,8,6,1,5,4,9,7,2],
[x,x,x,x,x,x,2,7,1,8,9,5,3,4,6],
[x,x,x,x,x,x,5,6,4,2,3,1,7,8,9],
[x,x,x,x,x,x,8,9,3,4,6,7,1,2,5]]

sudoku_array[6] = [[6,2,7,8,9,3,4,1,5,x,x,x,x,x,x],
[8,5,9,2,4,1,6,3,7,x,x,x,x,x,x],
[3,1,4,5,7,6,8,2,9,x,x,x,x,x,x],
[7,6,3,9,2,4,1,5,8,x,x,x,x,x,x],
[4,9,1,3,5,8,2,7,6,x,x,x,x,x,x],
[5,8,2,6,1,7,3,9,4,x,x,x,x,x,x],
[2,3,6,7,8,9,5,4,1,7,8,9,3,2,6],
[9,4,8,1,3,5,7,6,2,3,4,5,1,8,9],
[1,7,5,4,6,2,9,8,3,1,6,2,4,5,7],
[x,x,x,x,x,x,2,7,5,8,3,4,6,9,1],
[x,x,x,x,x,x,8,9,6,2,1,7,5,3,4],
[x,x,x,x,x,x,3,1,4,5,9,6,2,7,8],
[x,x,x,x,x,x,1,2,9,6,5,8,7,4,3],
[x,x,x,x,x,x,4,3,7,9,2,1,8,6,5],
[x,x,x,x,x,x,6,5,8,4,7,3,9,1,2]]

sudoku_array[7] = [[3,8,2,6,9,7,5,1,4,x,x,x,x,x,x],
[4,9,7,3,1,5,6,2,8,x,x,x,x,x,x],
[6,1,5,8,2,4,7,3,9,x,x,x,x,x,x],
[7,5,6,9,8,3,1,4,2,x,x,x,x,x,x],
[9,4,1,7,6,2,8,5,3,x,x,x,x,x,x],
[8,2,3,4,5,1,9,6,7,x,x,x,x,x,x],
[1,3,4,5,7,8,2,9,6,5,4,8,3,7,1],
[2,6,8,1,4,9,3,7,5,9,1,6,4,8,2],
[5,7,9,2,3,6,4,8,1,7,2,3,5,9,6],
[x,x,x,x,x,x,6,4,7,1,8,9,2,3,5],
[x,x,x,x,x,x,8,1,9,2,3,5,6,4,7],
[x,x,x,x,x,x,5,3,2,4,6,7,8,1,9],
[x,x,x,x,x,x,7,6,4,8,9,2,1,5,3],
[x,x,x,x,x,x,1,5,3,6,7,4,9,2,8],
[x,x,x,x,x,x,9,2,8,3,5,1,7,6,4]]

sudoku_array[8] = [[5,6,4,1,9,3,8,2,7,x,x,x,x,x,x],
[8,9,7,6,2,5,1,4,3,x,x,x,x,x,x],
[3,1,2,4,8,7,6,9,5,x,x,x,x,x,x],
[9,7,3,2,1,6,5,8,4,x,x,x,x,x,x],
[6,5,1,3,4,8,9,7,2,x,x,x,x,x,x],
[4,2,8,7,5,9,3,6,1,x,x,x,x,x,x],
[2,4,5,8,6,1,7,3,9,6,8,1,4,5,2],
[7,8,9,5,3,2,4,1,6,3,2,5,8,9,7],
[1,3,6,9,7,4,2,5,8,9,4,7,3,6,1],
[x,x,x,x,x,x,1,2,3,4,5,6,7,8,9],
[x,x,x,x,x,x,8,4,5,1,7,9,2,3,6],
[x,x,x,x,x,x,9,6,7,2,3,8,1,4,5],
[x,x,x,x,x,x,3,7,1,5,6,4,9,2,8],
[x,x,x,x,x,x,5,8,2,7,9,3,6,1,4],
[x,x,x,x,x,x,6,9,4,8,1,2,5,7,3]]

sudoku_array[9] = [[9,6,3,4,8,5,7,2,1,x,x,x,x,x,x],
[7,5,2,1,9,6,8,4,3,x,x,x,x,x,x],
[8,1,4,2,7,3,9,6,5,x,x,x,x,x,x],
[2,4,7,5,1,9,3,8,6,x,x,x,x,x,x],
[6,8,9,3,4,7,5,1,2,x,x,x,x,x,x],
[1,3,5,6,2,8,4,9,7,x,x,x,x,x,x],
[4,9,6,7,3,1,2,5,8,3,4,9,6,7,1],
[3,2,1,8,5,4,6,7,9,1,2,8,4,5,3],
[5,7,8,9,6,2,1,3,4,5,6,7,8,9,2],
[x,x,x,x,x,x,3,8,6,9,7,5,1,2,4],
[x,x,x,x,x,x,4,9,2,8,1,6,7,3,5],
[x,x,x,x,x,x,5,1,7,2,3,4,9,8,6],
[x,x,x,x,x,x,8,4,5,6,9,3,2,1,7],
[x,x,x,x,x,x,9,6,1,7,5,2,3,4,8],
[x,x,x,x,x,x,7,2,3,4,8,1,5,6,9]]

sudoku_array[10] = [[4,1,2,9,7,5,8,6,3,x,x,x,x,x,x],
[5,3,8,6,2,1,9,7,4,x,x,x,x,x,x],
[7,6,9,8,4,3,2,5,1,x,x,x,x,x,x],
[6,7,3,2,8,9,4,1,5,x,x,x,x,x,x],
[8,9,5,1,3,4,6,2,7,x,x,x,x,x,x],
[2,4,1,5,6,7,3,9,8,x,x,x,x,x,x],
[1,2,4,3,5,6,7,8,9,6,3,5,4,1,2],
[3,5,6,7,9,8,1,4,2,9,7,8,5,6,3],
[9,8,7,4,1,2,5,3,6,4,1,2,7,9,8],
[x,x,x,x,x,x,3,1,4,5,6,7,2,8,9],
[x,x,x,x,x,x,2,5,7,3,8,9,1,4,6],
[x,x,x,x,x,x,6,9,8,1,2,4,3,5,7],
[x,x,x,x,x,x,4,2,1,8,9,3,6,7,5],
[x,x,x,x,x,x,8,6,3,7,5,1,9,2,4],
[x,x,x,x,x,x,9,7,5,2,4,6,8,3,1]]

sudoku_array[11] = [[2,8,6,9,3,7,1,5,4,x,x,x,x,x,x],
[3,9,4,8,5,1,2,6,7,x,x,x,x,x,x],
[7,1,5,2,6,4,3,8,9,x,x,x,x,x,x],
[8,3,7,6,9,5,4,1,2,x,x,x,x,x,x],
[9,4,1,7,8,2,6,3,5,x,x,x,x,x,x],
[6,5,2,4,1,3,7,9,8,x,x,x,x,x,x],
[1,2,3,5,7,8,9,4,6,2,7,1,8,5,3],
[4,6,8,1,2,9,5,7,3,4,8,6,9,2,1],
[5,7,9,3,4,6,8,2,1,5,9,3,6,7,4],
[x,x,x,x,x,x,4,6,7,8,1,9,2,3,5],
[x,x,x,x,x,x,1,8,9,3,2,5,4,6,7],
[x,x,x,x,x,x,2,3,5,6,4,7,1,8,9],
[x,x,x,x,x,x,7,9,8,1,3,2,5,4,6],
[x,x,x,x,x,x,6,1,2,7,5,4,3,9,8],
[x,x,x,x,x,x,3,5,4,9,6,8,7,1,2]]

sudoku_array[12] = [[3,4,5,8,9,7,1,2,6,x,x,x,x,x,x],
[2,9,8,6,5,1,4,3,7,x,x,x,x,x,x],
[7,1,6,3,2,4,5,8,9,x,x,x,x,x,x],
[5,3,4,9,6,8,7,1,2,x,x,x,x,x,x],
[9,6,1,4,7,2,8,5,3,x,x,x,x,x,x],
[8,7,2,5,1,3,9,6,4,x,x,x,x,x,x],
[1,2,3,7,8,9,6,4,5,9,7,8,1,2,3],
[4,5,7,1,3,6,2,9,8,3,1,6,7,4,5],
[6,8,9,2,4,5,3,7,1,4,5,2,9,8,6],
[x,x,x,x,x,x,4,6,7,2,8,9,3,5,1],
[x,x,x,x,x,x,5,8,9,1,3,4,6,7,2],
[x,x,x,x,x,x,1,2,3,5,6,7,8,9,4],
[x,x,x,x,x,x,8,3,4,6,9,5,2,1,7],
[x,x,x,x,x,x,9,5,6,7,2,1,4,3,8],
[x,x,x,x,x,x,7,1,2,8,4,3,5,6,9]]

sudoku_array[13] = [[8,6,3,9,5,4,2,1,7,x,x,x,x,x,x],
[2,9,5,7,6,1,4,3,8,x,x,x,x,x,x],
[7,1,4,8,2,3,6,5,9,x,x,x,x,x,x],
[4,5,9,6,7,8,1,2,3,x,x,x,x,x,x],
[6,8,1,2,3,9,5,7,4,x,x,x,x,x,x],
[3,7,2,1,4,5,8,9,6,x,x,x,x,x,x],
[1,2,6,4,9,7,3,8,5,1,2,4,7,9,6],
[5,4,7,3,8,2,9,6,1,7,3,5,8,2,4],
[9,3,8,5,1,6,7,4,2,9,8,6,3,5,1],
[x,x,x,x,x,x,4,5,6,2,1,7,9,8,3],
[x,x,x,x,x,x,2,1,9,3,4,8,5,6,7],
[x,x,x,x,x,x,8,3,7,5,6,9,4,1,2],
[x,x,x,x,x,x,5,9,3,6,7,1,2,4,8],
[x,x,x,x,x,x,1,2,8,4,5,3,6,7,9],
[x,x,x,x,x,x,6,7,4,8,9,2,1,3,5]]

sudoku_array[14] = [[7,8,3,6,9,1,4,2,5,x,x,x,x,x,x],
[9,5,6,8,2,4,3,7,1,x,x,x,x,x,x],
[1,4,2,3,7,5,6,8,9,x,x,x,x,x,x],
[2,3,1,4,5,8,7,9,6,x,x,x,x,x,x],
[6,7,4,2,3,9,1,5,8,x,x,x,x,x,x],
[8,9,5,1,6,7,2,3,4,x,x,x,x,x,x],
[3,1,7,9,8,6,5,4,2,1,3,6,7,8,9],
[4,2,8,5,1,3,9,6,7,2,4,8,1,3,5],
[5,6,9,7,4,2,8,1,3,5,7,9,2,4,6],
[x,x,x,x,x,x,1,7,4,3,6,2,9,5,8],
[x,x,x,x,x,x,2,8,5,4,9,1,6,7,3],
[x,x,x,x,x,x,3,9,6,7,8,5,4,1,2],
[x,x,x,x,x,x,4,2,1,6,5,3,8,9,7],
[x,x,x,x,x,x,6,3,8,9,1,7,5,2,4],
[x,x,x,x,x,x,7,5,9,8,2,4,3,6,1]]

sudoku_array[15] = [[6,7,3,8,9,2,4,5,1,x,x,x,x,x,x],
[4,9,5,3,1,7,6,8,2,x,x,x,x,x,x],
[8,1,2,6,5,4,7,9,3,x,x,x,x,x,x],
[7,3,4,9,6,8,2,1,5,x,x,x,x,x,x],
[9,2,8,5,7,1,3,4,6,x,x,x,x,x,x],
[5,6,1,4,2,3,9,7,8,x,x,x,x,x,x],
[3,5,6,7,8,9,1,2,4,7,6,8,9,5,3],
[1,8,9,2,4,6,5,3,7,2,9,1,4,8,6],
[2,4,7,1,3,5,8,6,9,3,5,4,7,2,1],
[x,x,x,x,x,x,3,9,1,5,7,6,2,4,8],
[x,x,x,x,x,x,4,5,8,1,2,3,6,7,9],
[x,x,x,x,x,x,6,7,2,8,4,9,1,3,5],
[x,x,x,x,x,x,7,1,5,9,8,2,3,6,4],
[x,x,x,x,x,x,9,8,6,4,3,7,5,1,2],
[x,x,x,x,x,x,2,4,3,6,1,5,8,9,7]]

sudoku_array[16] = [[9,7,8,1,3,2,4,5,6,x,x,x,x,x,x],
[3,1,6,7,4,5,9,8,2,x,x,x,x,x,x],
[4,5,2,9,6,8,7,1,3,x,x,x,x,x,x],
[2,3,4,6,1,7,8,9,5,x,x,x,x,x,x],
[1,6,7,8,5,9,2,3,4,x,x,x,x,x,x],
[5,8,9,3,2,4,6,7,1,x,x,x,x,x,x],
[6,9,5,2,7,1,3,4,8,1,2,5,6,7,9],
[7,2,1,4,8,3,5,6,9,3,4,7,1,2,8],
[8,4,3,5,9,6,1,2,7,6,8,9,3,4,5],
[x,x,x,x,x,x,4,5,1,2,7,3,8,9,6],
[x,x,x,x,x,x,6,8,2,4,9,1,5,3,7],
[x,x,x,x,x,x,7,9,3,5,6,8,4,1,2],
[x,x,x,x,x,x,2,1,4,7,5,6,9,8,3],
[x,x,x,x,x,x,8,3,5,9,1,2,7,6,4],
[x,x,x,x,x,x,9,7,6,8,3,4,2,5,1]]

sudoku_array[17] = [[1,3,6,2,5,4,9,8,7,x,x,x,x,x,x],
[8,4,7,3,9,1,2,5,6,x,x,x,x,x,x],
[2,5,9,7,8,6,4,3,1,x,x,x,x,x,x],
[3,1,8,4,2,5,6,7,9,x,x,x,x,x,x],
[5,9,2,6,1,7,3,4,8,x,x,x,x,x,x],
[6,7,4,8,3,9,1,2,5,x,x,x,x,x,x],
[9,8,1,5,4,2,7,6,3,5,9,1,4,2,8],
[4,6,3,9,7,8,5,1,2,3,4,8,6,9,7],
[7,2,5,1,6,3,8,9,4,6,7,2,5,1,3],
[x,x,x,x,x,x,1,2,7,9,6,3,8,5,4],
[x,x,x,x,x,x,3,4,8,7,1,5,9,6,2],
[x,x,x,x,x,x,6,5,9,8,2,4,3,7,1],
[x,x,x,x,x,x,2,3,1,4,5,6,7,8,9],
[x,x,x,x,x,x,4,7,5,1,8,9,2,3,6],
[x,x,x,x,x,x,9,8,6,2,3,7,1,4,5]]

sudoku_array[18] = [[3,4,5,8,9,7,1,2,6,x,x,x,x,x,x],
[2,9,8,6,5,1,4,3,7,x,x,x,x,x,x],
[7,1,6,3,2,4,5,8,9,x,x,x,x,x,x],
[5,3,4,9,6,8,7,1,2,x,x,x,x,x,x],
[9,6,1,4,7,2,8,5,3,x,x,x,x,x,x],
[8,7,2,5,1,3,9,6,4,x,x,x,x,x,x],
[1,2,3,7,8,9,6,4,5,1,2,3,9,7,8],
[4,5,7,1,3,6,2,9,8,7,5,4,3,6,1],
[6,8,9,2,4,5,3,7,1,9,8,6,5,4,2],
[x,x,x,x,x,x,8,3,4,2,1,7,6,9,5],
[x,x,x,x,x,x,9,1,6,5,3,8,4,2,7],
[x,x,x,x,x,x,7,5,2,6,4,9,8,1,3],
[x,x,x,x,x,x,4,8,9,3,7,1,2,5,6],
[x,x,x,x,x,x,1,2,3,4,6,5,7,8,9],
[x,x,x,x,x,x,5,6,7,8,9,2,1,3,4]]

sudoku_array[19] = [[6,8,9,2,4,7,3,5,1,x,x,x,x,x,x],
[2,3,7,1,5,6,8,9,4,x,x,x,x,x,x],
[1,4,5,3,8,9,6,7,2,x,x,x,x,x,x],
[9,7,1,4,3,5,2,8,6,x,x,x,x,x,x],
[5,6,8,7,2,1,9,4,3,x,x,x,x,x,x],
[4,2,3,6,9,8,7,1,5,x,x,x,x,x,x],
[8,9,6,5,1,2,4,3,7,8,9,6,1,2,5],
[7,5,4,8,6,3,1,2,9,7,5,3,6,8,4],
[3,1,2,9,7,4,5,6,8,4,2,1,9,3,7],
[x,x,x,x,x,x,3,4,1,9,8,2,7,5,6],
[x,x,x,x,x,x,8,5,2,6,7,4,3,1,9],
[x,x,x,x,x,x,9,7,6,3,1,5,2,4,8],
[x,x,x,x,x,x,6,8,3,2,4,9,5,7,1],
[x,x,x,x,x,x,7,9,5,1,3,8,4,6,2],
[x,x,x,x,x,x,2,1,4,5,6,7,8,9,3]]

sudoku_array[20] = [[7,5,2,1,6,9,3,4,8,x,x,x,x,x,x],
[9,6,3,4,7,8,1,2,5,x,x,x,x,x,x],
[4,8,1,2,3,5,6,7,9,x,x,x,x,x,x],
[1,4,5,7,8,6,9,3,2,x,x,x,x,x,x],
[2,7,6,9,4,3,5,8,1,x,x,x,x,x,x],
[3,9,8,5,2,1,7,6,4,x,x,x,x,x,x],
[6,1,7,8,9,4,2,5,3,4,6,7,1,8,9],
[8,2,9,3,5,7,4,1,6,5,8,9,2,3,7],
[5,3,4,6,1,2,8,9,7,1,2,3,4,5,6],
[x,x,x,x,x,x,1,2,4,3,7,5,9,6,8],
[x,x,x,x,x,x,3,6,8,2,9,4,5,7,1],
[x,x,x,x,x,x,5,7,9,6,1,8,3,2,4],
[x,x,x,x,x,x,6,3,1,8,4,2,7,9,5],
[x,x,x,x,x,x,7,4,2,9,5,6,8,1,3],
[x,x,x,x,x,x,9,8,5,7,3,1,6,4,2]]

sudoku_array[21] = [[7,8,3,2,1,5,6,9,4,x,x,x,x,x,x],
[9,2,1,7,4,6,8,5,3,x,x,x,x,x,x],
[5,4,6,8,3,9,7,2,1,x,x,x,x,x,x],
[8,9,7,1,2,4,5,3,6,x,x,x,x,x,x],
[4,1,2,6,5,3,9,7,8,x,x,x,x,x,x],
[3,6,5,9,7,8,4,1,2,x,x,x,x,x,x],
[6,7,9,3,8,1,2,4,5,1,6,7,3,8,9],
[1,5,8,4,9,2,3,6,7,5,8,9,1,2,4],
[2,3,4,5,6,7,1,8,9,2,3,4,5,6,7],
[x,x,x,x,x,x,4,1,2,3,5,6,9,7,8],
[x,x,x,x,x,x,5,7,3,4,9,8,6,1,2],
[x,x,x,x,x,x,6,9,8,7,1,2,4,3,5],
[x,x,x,x,x,x,7,2,1,6,4,5,8,9,3],
[x,x,x,x,x,x,8,3,4,9,2,1,7,5,6],
[x,x,x,x,x,x,9,5,6,8,7,3,2,4,1]]

sudoku_array[22] = [[3,4,1,2,6,7,9,8,5,x,x,x,x,x,x],
[6,7,2,5,9,8,3,4,1,x,x,x,x,x,x],
[8,9,5,4,1,3,7,6,2,x,x,x,x,x,x],
[2,1,6,8,3,4,5,9,7,x,x,x,x,x,x],
[4,3,7,9,5,2,8,1,6,x,x,x,x,x,x],
[9,5,8,6,7,1,2,3,4,x,x,x,x,x,x],
[7,8,3,1,2,6,4,5,9,1,7,8,2,3,6],
[5,6,4,7,8,9,1,2,3,6,4,5,7,8,9],
[1,2,9,3,4,5,6,7,8,2,3,9,1,4,5],
[x,x,x,x,x,x,5,4,6,3,1,2,9,7,8],
[x,x,x,x,x,x,2,9,7,4,8,6,3,5,1],
[x,x,x,x,x,x,3,8,1,5,9,7,6,2,4],
[x,x,x,x,x,x,8,6,4,7,2,1,5,9,3],
[x,x,x,x,x,x,9,1,2,8,5,3,4,6,7],
[x,x,x,x,x,x,7,3,5,9,6,4,8,1,2]]

sudoku_array[23] = [[4,5,7,9,6,8,1,2,3,x,x,x,x,x,x],
[2,9,1,5,3,7,8,4,6,x,x,x,x,x,x],
[6,8,3,2,1,4,9,5,7,x,x,x,x,x,x],
[8,6,5,4,9,2,3,7,1,x,x,x,x,x,x],
[9,1,4,6,7,3,5,8,2,x,x,x,x,x,x],
[7,3,2,8,5,1,6,9,4,x,x,x,x,x,x],
[3,4,8,1,2,5,7,6,9,3,2,8,1,4,5],
[1,2,6,7,8,9,4,3,5,1,6,7,2,8,9],
[5,7,9,3,4,6,2,1,8,4,5,9,3,6,7],
[x,x,x,x,x,x,9,4,6,8,3,1,5,7,2],
[x,x,x,x,x,x,8,5,7,2,9,6,4,1,3],
[x,x,x,x,x,x,1,2,3,5,7,4,6,9,8],
[x,x,x,x,x,x,6,7,2,9,1,5,8,3,4],
[x,x,x,x,x,x,5,9,4,6,8,3,7,2,1],
[x,x,x,x,x,x,3,8,1,7,4,2,9,5,6]]

sudoku_array[24] = [[8,7,5,6,2,1,3,4,9,x,x,x,x,x,x],
[9,2,4,8,5,3,6,1,7,x,x,x,x,x,x],
[6,3,1,9,7,4,2,5,8,x,x,x,x,x,x],
[7,9,8,3,1,2,5,6,4,x,x,x,x,x,x],
[5,1,2,4,6,7,8,9,3,x,x,x,x,x,x],
[4,6,3,5,9,8,1,7,2,x,x,x,x,x,x],
[3,5,6,7,8,9,4,2,1,6,7,3,8,5,9],
[2,4,7,1,3,5,9,8,6,4,5,1,3,2,7],
[1,8,9,2,4,6,7,3,5,8,9,2,4,1,6],
[x,x,x,x,x,x,8,5,9,2,1,6,7,4,3],
[x,x,x,x,x,x,2,6,4,5,3,7,9,8,1],
[x,x,x,x,x,x,1,7,3,9,4,8,2,6,5],
[x,x,x,x,x,x,3,4,7,1,2,5,6,9,8],
[x,x,x,x,x,x,6,1,2,7,8,9,5,3,4],
[x,x,x,x,x,x,5,9,8,3,6,4,1,7,2]]

sudoku_array[25] = [[8,1,9,4,2,7,3,5,6,x,x,x,x,x,x],
[2,4,3,5,1,6,7,8,9,x,x,x,x,x,x],
[6,5,7,8,3,9,1,2,4,x,x,x,x,x,x],
[1,7,4,6,5,8,9,3,2,x,x,x,x,x,x],
[3,8,6,2,9,4,5,7,1,x,x,x,x,x,x],
[5,9,2,3,7,1,6,4,8,x,x,x,x,x,x],
[4,3,5,1,6,2,8,9,7,3,2,4,5,1,6],
[9,6,8,7,4,5,2,1,3,5,9,6,7,4,8],
[7,2,1,9,8,3,4,6,5,7,1,8,3,2,9],
[x,x,x,x,x,x,5,8,9,6,4,7,1,3,2],
[x,x,x,x,x,x,6,7,2,1,3,9,8,5,4],
[x,x,x,x,x,x,3,4,1,8,5,2,9,6,7],
[x,x,x,x,x,x,9,5,8,4,6,3,2,7,1],
[x,x,x,x,x,x,1,2,6,9,7,5,4,8,3],
[x,x,x,x,x,x,7,3,4,2,8,1,6,9,5]]

sudoku_array[26] = [[8,7,3,9,6,2,5,4,1,x,x,x,x,x,x],
[2,9,1,5,8,4,6,7,3,x,x,x,x,x,x],
[5,6,4,7,3,1,9,8,2,x,x,x,x,x,x],
[6,4,9,1,2,3,7,5,8,x,x,x,x,x,x],
[7,2,8,4,5,9,3,1,6,x,x,x,x,x,x],
[3,1,5,6,7,8,2,9,4,x,x,x,x,x,x],
[9,8,6,3,4,7,1,2,5,3,4,7,6,8,9],
[1,5,2,8,9,6,4,3,7,8,9,6,1,2,5],
[4,3,7,2,1,5,8,6,9,2,5,1,3,4,7],
[x,x,x,x,x,x,7,4,3,1,6,2,9,5,8],
[x,x,x,x,x,x,9,1,8,5,7,3,2,6,4],
[x,x,x,x,x,x,2,5,6,9,8,4,7,3,1],
[x,x,x,x,x,x,3,7,2,4,1,5,8,9,6],
[x,x,x,x,x,x,5,9,1,6,2,8,4,7,3],
[x,x,x,x,x,x,6,8,4,7,3,9,5,1,2]]

sudoku_array[27] = [[2,7,8,4,9,5,1,3,6,x,x,x,x,x,x],
[5,9,1,8,6,3,2,4,7,x,x,x,x,x,x],
[4,6,3,2,7,1,5,8,9,x,x,x,x,x,x],
[8,3,5,9,4,7,6,2,1,x,x,x,x,x,x],
[9,4,7,6,1,2,8,5,3,x,x,x,x,x,x],
[6,1,2,5,3,8,9,7,4,x,x,x,x,x,x],
[3,5,6,7,8,9,4,1,2,6,5,3,8,9,7],
[1,2,4,3,5,6,7,9,8,1,2,4,3,5,6],
[7,8,9,1,2,4,3,6,5,9,8,7,1,4,2],
[x,x,x,x,x,x,8,4,6,2,1,5,9,7,3],
[x,x,x,x,x,x,9,2,1,7,3,6,5,8,4],
[x,x,x,x,x,x,5,7,3,8,4,9,2,6,1],
[x,x,x,x,x,x,6,8,9,3,7,1,4,2,5],
[x,x,x,x,x,x,2,3,4,5,6,8,7,1,9],
[x,x,x,x,x,x,1,5,7,4,9,2,6,3,8]]

sudoku_array[28] = [[6,4,5,1,3,2,9,7,8,x,x,x,x,x,x],
[2,9,8,7,4,5,3,6,1,x,x,x,x,x,x],
[3,7,1,9,6,8,5,4,2,x,x,x,x,x,x],
[4,8,9,3,1,7,2,5,6,x,x,x,x,x,x],
[5,6,7,8,2,9,1,3,4,x,x,x,x,x,x],
[1,2,3,4,5,6,7,8,9,x,x,x,x,x,x],
[8,3,4,2,7,1,6,9,5,1,2,3,4,7,8],
[9,1,6,5,8,3,4,2,7,5,6,8,1,3,9],
[7,5,2,6,9,4,8,1,3,4,7,9,2,5,6],
[x,x,x,x,x,x,1,4,6,2,5,7,8,9,3],
[x,x,x,x,x,x,2,5,8,3,9,4,7,6,1],
[x,x,x,x,x,x,3,7,9,6,8,1,5,4,2],
[x,x,x,x,x,x,5,3,1,8,4,6,9,2,7],
[x,x,x,x,x,x,7,6,2,9,1,5,3,8,4],
[x,x,x,x,x,x,9,8,4,7,3,2,6,1,5]]

sudoku_array[29] = [[3,7,5,1,4,2,6,9,8,x,x,x,x,x,x],
[9,8,1,6,7,3,2,4,5,x,x,x,x,x,x],
[6,4,2,9,8,5,3,1,7,x,x,x,x,x,x],
[8,9,7,2,3,1,4,5,6,x,x,x,x,x,x],
[5,6,4,8,9,7,1,2,3,x,x,x,x,x,x],
[1,2,3,5,6,4,7,8,9,x,x,x,x,x,x],
[2,5,8,3,1,6,9,7,4,1,6,2,5,3,8],
[7,3,9,4,2,8,5,6,1,9,8,3,2,7,4],
[4,1,6,7,5,9,8,3,2,5,7,4,9,6,1],
[x,x,x,x,x,x,1,2,3,4,5,7,6,8,9],
[x,x,x,x,x,x,4,5,7,8,9,6,1,2,3],
[x,x,x,x,x,x,6,8,9,2,3,1,4,5,7],
[x,x,x,x,x,x,2,1,5,3,4,8,7,9,6],
[x,x,x,x,x,x,3,4,6,7,2,9,8,1,5],
[x,x,x,x,x,x,7,9,8,6,1,5,3,4,2]]

sudoku_array[30] = [[2,8,7,5,9,4,1,3,6,x,x,x,x,x,x],
[4,9,6,3,1,7,2,5,8,x,x,x,x,x,x],
[5,1,3,2,6,8,4,7,9,x,x,x,x,x,x],
[8,6,4,9,3,5,7,2,1,x,x,x,x,x,x],
[9,5,1,6,7,2,8,4,3,x,x,x,x,x,x],
[7,3,2,8,4,1,9,6,5,x,x,x,x,x,x],
[1,2,8,4,5,6,3,9,7,4,6,1,2,5,8],
[6,7,9,1,2,3,5,8,4,9,7,2,6,3,1],
[3,4,5,7,8,9,6,1,2,8,5,3,4,9,7],
[x,x,x,x,x,x,9,2,6,5,1,4,8,7,3],
[x,x,x,x,x,x,7,5,3,6,2,8,9,1,4],
[x,x,x,x,x,x,8,4,1,7,3,9,5,6,2],
[x,x,x,x,x,x,1,7,9,2,8,5,3,4,6],
[x,x,x,x,x,x,4,6,8,3,9,7,1,2,5],
[x,x,x,x,x,x,2,3,5,1,4,6,7,8,9]]

sudoku_array[31] = [[3,2,7,8,9,5,1,4,6,x,x,x,x,x,x],
[4,9,6,3,1,7,2,5,8,x,x,x,x,x,x],
[5,8,1,6,4,2,3,7,9,x,x,x,x,x,x],
[8,5,4,9,6,3,7,1,2,x,x,x,x,x,x],
[9,6,2,5,7,1,8,3,4,x,x,x,x,x,x],
[7,1,3,4,2,8,9,6,5,x,x,x,x,x,x],
[1,4,5,7,8,9,6,2,3,5,1,4,9,8,7],
[2,3,8,1,5,6,4,9,7,8,2,6,5,1,3],
[6,7,9,2,3,4,5,8,1,9,3,7,4,6,2],
[x,x,x,x,x,x,2,4,5,1,8,3,6,7,9],
[x,x,x,x,x,x,1,7,9,6,4,2,3,5,8],
[x,x,x,x,x,x,3,6,8,7,5,9,1,2,4],
[x,x,x,x,x,x,8,3,4,2,6,1,7,9,5],
[x,x,x,x,x,x,9,1,2,3,7,5,8,4,6],
[x,x,x,x,x,x,7,5,6,4,9,8,2,3,1]]

sudoku_array[32] = [[1,2,6,8,9,5,4,3,7,x,x,x,x,x,x],
[5,3,7,6,1,4,8,2,9,x,x,x,x,x,x],
[9,4,8,3,7,2,6,5,1,x,x,x,x,x,x],
[3,5,1,9,4,8,7,6,2,x,x,x,x,x,x],
[6,8,2,5,3,7,1,9,4,x,x,x,x,x,x],
[7,9,4,2,6,1,3,8,5,x,x,x,x,x,x],
[8,7,9,1,2,3,5,4,6,7,9,1,8,2,3],
[2,1,3,4,5,6,9,7,8,4,2,3,5,6,1],
[4,6,5,7,8,9,2,1,3,5,6,8,4,9,7],
[x,x,x,x,x,x,3,2,4,1,5,6,7,8,9],
[x,x,x,x,x,x,8,5,9,2,4,7,1,3,6],
[x,x,x,x,x,x,1,6,7,3,8,9,2,4,5],
[x,x,x,x,x,x,4,3,1,6,7,2,9,5,8],
[x,x,x,x,x,x,6,8,2,9,1,5,3,7,4],
[x,x,x,x,x,x,7,9,5,8,3,4,6,1,2]]

sudoku_array[33] = [[3,8,7,9,6,5,2,1,4,x,x,x,x,x,x],
[5,9,2,8,4,1,3,6,7,x,x,x,x,x,x],
[6,1,4,3,7,2,5,9,8,x,x,x,x,x,x],
[1,7,9,2,3,4,8,5,6,x,x,x,x,x,x],
[2,3,8,1,5,6,4,7,9,x,x,x,x,x,x],
[4,5,6,7,8,9,1,2,3,x,x,x,x,x,x],
[8,2,5,4,9,7,6,3,1,7,9,4,2,8,5],
[9,6,3,5,1,8,7,4,2,6,8,5,9,1,3],
[7,4,1,6,2,3,9,8,5,3,1,2,6,4,7],
[x,x,x,x,x,x,2,1,4,9,5,6,7,3,8],
[x,x,x,x,x,x,3,5,6,8,7,1,4,2,9],
[x,x,x,x,x,x,8,9,7,4,2,3,1,5,6],
[x,x,x,x,x,x,4,6,8,2,3,9,5,7,1],
[x,x,x,x,x,x,1,2,3,5,6,7,8,9,4],
[x,x,x,x,x,x,5,7,9,1,4,8,3,6,2]]

sudoku_array[34] = [[3,4,5,8,9,7,1,2,6,x,x,x,x,x,x],
[2,9,8,6,5,1,4,3,7,x,x,x,x,x,x],
[7,1,6,3,2,4,5,8,9,x,x,x,x,x,x],
[5,3,4,9,6,8,7,1,2,x,x,x,x,x,x],
[9,6,1,4,7,2,8,5,3,x,x,x,x,x,x],
[8,7,2,5,1,3,9,6,4,x,x,x,x,x,x],
[1,2,3,7,8,9,6,4,5,7,9,8,1,3,2],
[4,5,7,1,3,6,2,9,8,5,1,3,6,4,7],
[6,8,9,2,4,5,3,7,1,6,2,4,9,5,8],
[x,x,x,x,x,x,8,3,4,9,7,5,2,6,1],
[x,x,x,x,x,x,9,5,2,8,6,1,4,7,3],
[x,x,x,x,x,x,7,1,6,3,4,2,8,9,5],
[x,x,x,x,x,x,5,6,7,2,8,9,3,1,4],
[x,x,x,x,x,x,4,8,9,1,3,7,5,2,6],
[x,x,x,x,x,x,1,2,3,4,5,6,7,8,9]]

sudoku_array[35] = [[5,9,4,6,8,3,7,2,1,x,x,x,x,x,x],
[7,6,2,9,1,5,8,3,4,x,x,x,x,x,x],
[8,3,1,2,7,4,9,5,6,x,x,x,x,x,x],
[2,8,9,4,6,1,5,7,3,x,x,x,x,x,x],
[3,5,6,7,9,8,4,1,2,x,x,x,x,x,x],
[1,4,7,3,5,2,6,9,8,x,x,x,x,x,x],
[9,7,8,1,3,6,2,4,5,6,7,3,8,9,1],
[4,1,5,8,2,9,3,6,7,8,9,1,4,5,2],
[6,2,3,5,4,7,1,8,9,4,5,2,6,7,3],
[x,x,x,x,x,x,9,3,6,2,1,7,5,4,8],
[x,x,x,x,x,x,5,7,4,3,6,8,2,1,9],
[x,x,x,x,x,x,8,2,1,5,4,9,7,3,6],
[x,x,x,x,x,x,7,9,8,1,2,5,3,6,4],
[x,x,x,x,x,x,6,1,2,7,3,4,9,8,5],
[x,x,x,x,x,x,4,5,3,9,8,6,1,2,7]]

sudoku_array[36] = [[7,9,6,1,2,5,3,4,8,x,x,x,x,x,x],
[3,5,8,9,4,6,7,1,2,x,x,x,x,x,x],
[2,1,4,7,8,3,5,9,6,x,x,x,x,x,x],
[6,7,5,8,9,1,2,3,4,x,x,x,x,x,x],
[1,2,3,5,7,4,6,8,9,x,x,x,x,x,x],
[4,8,9,3,6,2,1,5,7,x,x,x,x,x,x],
[9,4,1,2,3,7,8,6,5,1,2,3,4,7,9],
[5,6,7,4,1,8,9,2,3,4,5,7,1,6,8],
[8,3,2,6,5,9,4,7,1,6,8,9,2,3,5],
[x,x,x,x,x,x,1,4,6,2,9,5,7,8,3],
[x,x,x,x,x,x,2,5,7,3,1,8,9,4,6],
[x,x,x,x,x,x,3,8,9,7,4,6,5,2,1],
[x,x,x,x,x,x,5,1,2,8,3,4,6,9,7],
[x,x,x,x,x,x,6,3,4,9,7,1,8,5,2],
[x,x,x,x,x,x,7,9,8,5,6,2,3,1,4]]

sudoku_array[37] = [[9,6,8,1,2,3,4,5,7,x,x,x,x,x,x],
[5,3,2,6,7,4,1,8,9,x,x,x,x,x,x],
[4,7,1,9,8,5,6,2,3,x,x,x,x,x,x],
[8,9,4,2,1,6,7,3,5,x,x,x,x,x,x],
[7,2,5,4,3,8,9,6,1,x,x,x,x,x,x],
[6,1,3,7,5,9,8,4,2,x,x,x,x,x,x],
[2,8,9,3,4,1,5,7,6,1,2,4,9,3,8],
[1,4,7,5,6,2,3,9,8,7,5,6,2,1,4],
[3,5,6,8,9,7,2,1,4,9,3,8,5,7,6],
[x,x,x,x,x,x,6,8,9,2,1,3,4,5,7],
[x,x,x,x,x,x,4,5,7,8,6,9,1,2,3],
[x,x,x,x,x,x,1,2,3,5,4,7,8,6,9],
[x,x,x,x,x,x,9,4,5,3,7,1,6,8,2],
[x,x,x,x,x,x,7,6,1,4,8,2,3,9,5],
[x,x,x,x,x,x,8,3,2,6,9,5,7,4,1]]
sudoku_array[38] = [[7,4,6,8,9,3,5,1,2,x,x,x,x,x,x],
[2,1,3,6,7,5,4,9,8,x,x,x,x,x,x],
[9,8,5,2,4,1,6,7,3,x,x,x,x,x,x],
[6,2,7,3,8,9,1,4,5,x,x,x,x,x,x],
[8,5,9,1,2,4,3,6,7,x,x,x,x,x,x],
[1,3,4,5,6,7,2,8,9,x,x,x,x,x,x],
[5,9,8,4,3,6,7,2,1,6,9,4,5,8,3],
[4,7,1,9,5,2,8,3,6,5,7,2,9,1,4],
[3,6,2,7,1,8,9,5,4,8,1,3,7,2,6],
[x,x,x,x,x,x,3,6,8,2,5,9,4,7,1],
[x,x,x,x,x,x,5,7,9,1,4,8,3,6,2],
[x,x,x,x,x,x,1,4,2,3,6,7,8,9,5],
[x,x,x,x,x,x,2,1,3,9,8,5,6,4,7],
[x,x,x,x,x,x,4,8,5,7,2,6,1,3,9],
[x,x,x,x,x,x,6,9,7,4,3,1,2,5,8]]

sudoku_array[39] = [[4,2,8,7,9,6,1,5,3,x,x,x,x,x,x],
[5,9,1,4,8,3,2,7,6,x,x,x,x,x,x],
[6,7,3,5,1,2,4,8,9,x,x,x,x,x,x],
[2,8,9,1,4,5,3,6,7,x,x,x,x,x,x],
[1,6,7,2,3,8,5,9,4,x,x,x,x,x,x],
[3,4,5,6,7,9,8,1,2,x,x,x,x,x,x],
[8,3,4,9,5,7,6,2,1,7,9,4,5,3,8],
[9,1,2,8,6,4,7,3,5,6,8,2,9,4,1],
[7,5,6,3,2,1,9,4,8,5,1,3,2,7,6],
[x,x,x,x,x,x,2,1,3,9,7,5,6,8,4],
[x,x,x,x,x,x,5,6,4,8,3,1,7,9,2],
[x,x,x,x,x,x,8,7,9,4,2,6,1,5,3],
[x,x,x,x,x,x,3,8,6,2,5,9,4,1,7],
[x,x,x,x,x,x,4,9,7,1,6,8,3,2,5],
[x,x,x,x,x,x,1,5,2,3,4,7,8,6,9]]

sudoku_array[40] = [[6,3,5,7,9,2,1,4,8,x,x,x,x,x,x],
[8,9,7,3,1,4,6,5,2,x,x,x,x,x,x],
[4,1,2,5,6,8,9,3,7,x,x,x,x,x,x],
[3,4,9,8,7,5,2,6,1,x,x,x,x,x,x],
[2,7,6,9,4,1,5,8,3,x,x,x,x,x,x],
[5,8,1,6,2,3,7,9,4,x,x,x,x,x,x],
[7,5,4,2,8,9,3,1,6,4,5,7,2,8,9],
[1,2,3,4,5,6,8,7,9,1,2,3,4,5,6],
[9,6,8,1,3,7,4,2,5,6,8,9,1,3,7],
[x,x,x,x,x,x,1,3,2,5,4,6,9,7,8],
[x,x,x,x,x,x,6,4,7,2,9,8,5,1,3],
[x,x,x,x,x,x,9,5,8,3,7,1,6,4,2],
[x,x,x,x,x,x,2,6,1,7,3,4,8,9,5],
[x,x,x,x,x,x,5,8,3,9,1,2,7,6,4],
[x,x,x,x,x,x,7,9,4,8,6,5,3,2,1]]

sudoku_array[41] = [[9,6,7,1,4,2,5,3,8,x,x,x,x,x,x],
[8,4,1,7,5,3,2,6,9,x,x,x,x,x,x],
[5,2,3,9,6,8,4,7,1,x,x,x,x,x,x],
[4,9,8,2,7,1,6,5,3,x,x,x,x,x,x],
[6,7,5,3,8,4,9,1,2,x,x,x,x,x,x],
[3,1,2,5,9,6,7,8,4,x,x,x,x,x,x],
[1,5,6,8,2,9,3,4,7,5,6,1,8,2,9],
[7,8,9,4,3,5,1,2,6,8,9,3,4,5,7],
[2,3,4,6,1,7,8,9,5,2,4,7,3,1,6],
[x,x,x,x,x,x,6,1,4,7,2,5,9,3,8],
[x,x,x,x,x,x,5,3,2,9,8,6,1,7,4],
[x,x,x,x,x,x,9,7,8,3,1,4,5,6,2],
[x,x,x,x,x,x,7,8,9,1,3,2,6,4,5],
[x,x,x,x,x,x,2,6,3,4,5,8,7,9,1],
[x,x,x,x,x,x,4,5,1,6,7,9,2,8,3]]

sudoku_array[42] = [[7,9,8,1,3,6,2,4,5,x,x,x,x,x,x],
[4,1,5,9,2,8,3,6,7,x,x,x,x,x,x],
[3,2,6,7,4,5,1,9,8,x,x,x,x,x,x],
[5,7,1,3,8,9,6,2,4,x,x,x,x,x,x],
[9,4,3,2,6,7,8,5,1,x,x,x,x,x,x],
[8,6,2,5,1,4,9,7,3,x,x,x,x,x,x],
[2,5,7,8,9,1,4,3,6,1,5,7,2,8,9],
[6,8,9,4,5,3,7,1,2,4,8,9,3,5,6],
[1,3,4,6,7,2,5,8,9,2,6,3,4,1,7],
[x,x,x,x,x,x,2,7,5,8,9,6,1,3,4],
[x,x,x,x,x,x,3,9,8,7,1,4,5,6,2],
[x,x,x,x,x,x,1,6,4,5,3,2,7,9,8],
[x,x,x,x,x,x,6,2,1,9,7,5,8,4,3],
[x,x,x,x,x,x,8,4,3,6,2,1,9,7,5],
[x,x,x,x,x,x,9,5,7,3,4,8,6,2,1]]

sudoku_array[43] = [[9,5,3,8,7,6,4,1,2,x,x,x,x,x,x],
[7,6,2,9,1,4,5,3,8,x,x,x,x,x,x],
[8,1,4,5,3,2,7,6,9,x,x,x,x,x,x],
[6,8,9,1,2,7,3,5,4,x,x,x,x,x,x],
[1,2,7,3,4,5,9,8,6,x,x,x,x,x,x],
[3,4,5,6,8,9,1,2,7,x,x,x,x,x,x],
[2,9,8,4,5,1,6,7,3,8,1,9,2,4,5],
[4,7,1,2,6,3,8,9,5,4,2,7,1,3,6],
[5,3,6,7,9,8,2,4,1,5,3,6,7,8,9],
[x,x,x,x,x,x,3,5,6,1,4,2,9,7,8],
[x,x,x,x,x,x,9,8,2,7,5,3,4,6,1],
[x,x,x,x,x,x,7,1,4,9,6,8,3,5,2],
[x,x,x,x,x,x,4,6,8,2,7,1,5,9,3],
[x,x,x,x,x,x,5,2,9,3,8,4,6,1,7],
[x,x,x,x,x,x,1,3,7,6,9,5,8,2,4]]

sudoku_array[44] = [[9,6,4,3,8,7,2,1,5,x,x,x,x,x,x],
[8,2,5,4,9,1,6,3,7,x,x,x,x,x,x],
[7,3,1,5,6,2,9,4,8,x,x,x,x,x,x],
[2,8,9,1,4,5,3,7,6,x,x,x,x,x,x],
[1,4,7,2,3,6,5,8,9,x,x,x,x,x,x],
[3,5,6,8,7,9,1,2,4,x,x,x,x,x,x],
[4,9,8,6,2,3,7,5,1,3,2,4,8,9,6],
[5,7,3,9,1,8,4,6,2,8,9,1,5,3,7],
[6,1,2,7,5,4,8,9,3,6,5,7,2,1,4],
[x,x,x,x,x,x,1,4,9,2,3,5,6,7,8],
[x,x,x,x,x,x,2,7,5,1,6,8,3,4,9],
[x,x,x,x,x,x,3,8,6,4,7,9,1,2,5],
[x,x,x,x,x,x,5,1,4,9,8,2,7,6,3],
[x,x,x,x,x,x,6,2,7,5,4,3,9,8,1],
[x,x,x,x,x,x,9,3,8,7,1,6,4,5,2]]

sudoku_array[45] = [[2,8,3,7,9,6,5,4,1,x,x,x,x,x,x],
[4,9,1,5,3,8,6,7,2,x,x,x,x,x,x],
[5,6,7,2,1,4,9,8,3,x,x,x,x,x,x],
[8,3,6,9,7,5,2,1,4,x,x,x,x,x,x],
[9,5,2,8,4,1,7,3,6,x,x,x,x,x,x],
[7,1,4,3,6,2,8,5,9,x,x,x,x,x,x],
[1,2,9,4,5,7,3,6,8,7,9,4,5,1,2],
[3,4,5,6,8,9,1,2,7,5,6,8,4,9,3],
[6,7,8,1,2,3,4,9,5,2,1,3,6,8,7],
[x,x,x,x,x,x,2,1,3,8,7,5,9,6,4],
[x,x,x,x,x,x,7,4,6,9,3,1,8,2,5],
[x,x,x,x,x,x,8,5,9,6,4,2,7,3,1],
[x,x,x,x,x,x,9,3,1,4,5,6,2,7,8],
[x,x,x,x,x,x,5,7,2,3,8,9,1,4,6],
[x,x,x,x,x,x,6,8,4,1,2,7,3,5,9]]

sudoku_array[46] = [[1,2,3,5,6,4,8,9,7,x,x,x,x,x,x],
[8,4,5,9,7,1,6,2,3,x,x,x,x,x,x],
[9,7,6,8,2,3,5,4,1,x,x,x,x,x,x],
[2,1,7,6,3,5,9,8,4,x,x,x,x,x,x],
[4,3,8,2,1,9,7,6,5,x,x,x,x,x,x],
[5,6,9,7,4,8,3,1,2,x,x,x,x,x,x],
[6,8,1,4,5,7,2,3,9,4,5,8,7,6,1],
[7,9,4,3,8,2,1,5,6,2,3,7,9,8,4],
[3,5,2,1,9,6,4,7,8,1,6,9,5,3,2],
[x,x,x,x,x,x,5,8,4,3,9,2,6,1,7],
[x,x,x,x,x,x,9,6,7,5,8,1,4,2,3],
[x,x,x,x,x,x,3,1,2,6,7,4,8,5,9],
[x,x,x,x,x,x,7,9,3,8,2,6,1,4,5],
[x,x,x,x,x,x,8,4,5,9,1,3,2,7,6],
[x,x,x,x,x,x,6,2,1,7,4,5,3,9,8]]

sudoku_array[47] = [[6,1,9,2,3,7,4,8,5,x,x,x,x,x,x],
[3,2,8,1,4,5,6,9,7,x,x,x,x,x,x],
[4,7,5,6,8,9,1,3,2,x,x,x,x,x,x],
[8,4,7,9,5,6,2,1,3,x,x,x,x,x,x],
[9,5,2,8,1,3,7,4,6,x,x,x,x,x,x],
[1,3,6,4,7,2,9,5,8,x,x,x,x,x,x],
[7,8,4,3,2,1,5,6,9,8,1,2,7,4,3],
[5,6,1,7,9,8,3,2,4,7,9,6,8,5,1],
[2,9,3,5,6,4,8,7,1,3,5,4,9,6,2],
[x,x,x,x,x,x,2,4,8,9,6,3,1,7,5],
[x,x,x,x,x,x,6,3,7,5,8,1,2,9,4],
[x,x,x,x,x,x,9,1,5,4,2,7,3,8,6],
[x,x,x,x,x,x,4,8,6,2,3,9,5,1,7],
[x,x,x,x,x,x,7,9,3,1,4,5,6,2,8],
[x,x,x,x,x,x,1,5,2,6,7,8,4,3,9]]

sudoku_array[48] = [[3,4,7,5,9,8,1,2,6,x,x,x,x,x,x],
[2,5,6,1,3,4,9,7,8,x,x,x,x,x,x],
[1,8,9,6,7,2,3,4,5,x,x,x,x,x,x],
[6,7,8,4,5,9,2,1,3,x,x,x,x,x,x],
[4,9,2,3,8,1,5,6,7,x,x,x,x,x,x],
[5,1,3,2,6,7,4,8,9,x,x,x,x,x,x],
[8,2,5,7,4,3,6,9,1,2,3,4,5,7,8],
[9,6,4,8,1,5,7,3,2,1,5,8,4,6,9],
[7,3,1,9,2,6,8,5,4,6,7,9,1,2,3],
[x,x,x,x,x,x,1,4,5,3,2,6,8,9,7],
[x,x,x,x,x,x,2,6,8,4,9,7,3,5,1],
[x,x,x,x,x,x,3,7,9,8,1,5,2,4,6],
[x,x,x,x,x,x,4,1,3,7,6,2,9,8,5],
[x,x,x,x,x,x,5,2,6,9,8,1,7,3,4],
[x,x,x,x,x,x,9,8,7,5,4,3,6,1,2]]

sudoku_array[49] = [[1,3,2,9,6,8,4,7,5,x,x,x,x,x,x],
[8,4,5,3,7,2,6,9,1,x,x,x,x,x,x],
[9,6,7,4,5,1,3,8,2,x,x,x,x,x,x],
[2,7,1,8,9,4,5,6,3,x,x,x,x,x,x],
[5,8,3,6,1,7,2,4,9,x,x,x,x,x,x],
[6,9,4,5,2,3,7,1,8,x,x,x,x,x,x],
[7,1,9,2,4,5,8,3,6,7,2,5,9,4,1],
[3,5,6,7,8,9,1,2,4,6,8,9,7,3,5],
[4,2,8,1,3,6,9,5,7,4,1,3,2,6,8],
[x,x,x,x,x,x,3,4,8,5,9,2,1,7,6],
[x,x,x,x,x,x,7,6,9,3,4,1,5,8,2],
[x,x,x,x,x,x,2,1,5,8,7,6,4,9,3],
[x,x,x,x,x,x,4,9,3,1,5,8,6,2,7],
[x,x,x,x,x,x,5,8,2,9,6,7,3,1,4],
[x,x,x,x,x,x,6,7,1,2,3,4,8,5,9]]

sudoku_array[50] = [[4,8,7,5,3,9,2,6,1,x,x,x,x,x,x],
[1,6,9,4,2,8,5,7,3,x,x,x,x,x,x],
[2,3,5,1,6,7,9,8,4,x,x,x,x,x,x],
[7,4,6,9,8,3,1,5,2,x,x,x,x,x,x],
[9,2,8,7,1,5,4,3,6,x,x,x,x,x,x],
[5,1,3,2,4,6,7,9,8,x,x,x,x,x,x],
[6,7,2,8,9,4,3,1,5,4,6,7,2,8,9],
[8,9,4,3,5,1,6,2,7,5,8,9,1,3,4],
[3,5,1,6,7,2,8,4,9,1,2,3,5,6,7],
[x,x,x,x,x,x,1,3,2,6,4,5,9,7,8],
[x,x,x,x,x,x,7,5,4,2,9,8,3,1,6],
[x,x,x,x,x,x,9,6,8,3,7,1,4,5,2],
[x,x,x,x,x,x,2,7,1,8,3,4,6,9,5],
[x,x,x,x,x,x,4,8,3,9,5,6,7,2,1],
[x,x,x,x,x,x,5,9,6,7,1,2,8,4,3]]

sudoku_array[51] = [[4,6,8,2,1,5,9,7,3,x,x,x,x,x,x],
[7,1,9,6,3,8,5,2,4,x,x,x,x,x,x],
[5,3,2,7,4,9,8,6,1,x,x,x,x,x,x],
[2,4,1,5,6,3,7,8,9,x,x,x,x,x,x],
[6,7,3,8,9,1,2,4,5,x,x,x,x,x,x],
[8,9,5,4,7,2,1,3,6,x,x,x,x,x,x],
[9,8,4,1,2,6,3,5,7,1,2,8,9,6,4],
[1,2,7,3,5,4,6,9,8,5,4,7,1,2,3],
[3,5,6,9,8,7,4,1,2,9,3,6,8,7,5],
[x,x,x,x,x,x,2,3,1,8,9,5,6,4,7],
[x,x,x,x,x,x,8,6,4,2,7,3,5,1,9],
[x,x,x,x,x,x,9,7,5,6,1,4,2,3,8],
[x,x,x,x,x,x,5,4,6,7,8,2,3,9,1],
[x,x,x,x,x,x,7,8,9,3,6,1,4,5,2],
[x,x,x,x,x,x,1,2,3,4,5,9,7,8,6]]

sudoku_array[52] = [[8,9,1,2,3,7,4,5,6,x,x,x,x,x,x],
[6,7,5,4,8,9,1,2,3,x,x,x,x,x,x],
[3,4,2,1,5,6,7,8,9,x,x,x,x,x,x],
[2,6,7,5,4,8,9,3,1,x,x,x,x,x,x],
[5,1,8,9,7,3,6,4,2,x,x,x,x,x,x],
[4,3,9,6,1,2,5,7,8,x,x,x,x,x,x],
[1,2,4,3,6,5,8,9,7,6,4,5,3,1,2],
[7,5,3,8,9,1,2,6,4,3,9,1,5,8,7],
[9,8,6,7,2,4,3,1,5,8,7,2,4,6,9],
[x,x,x,x,x,x,4,7,6,2,8,9,1,3,5],
[x,x,x,x,x,x,1,2,3,4,5,6,9,7,8],
[x,x,x,x,x,x,5,8,9,1,3,7,2,4,6],
[x,x,x,x,x,x,6,3,1,9,2,8,7,5,4],
[x,x,x,x,x,x,7,4,2,5,6,3,8,9,1],
[x,x,x,x,x,x,9,5,8,7,1,4,6,2,3]]

sudoku_array[53] = [[4,9,7,5,6,8,1,3,2,x,x,x,x,x,x],
[6,1,2,9,7,3,8,4,5,x,x,x,x,x,x],
[5,8,3,4,1,2,9,6,7,x,x,x,x,x,x],
[8,3,5,6,9,4,2,7,1,x,x,x,x,x,x],
[9,6,1,2,5,7,4,8,3,x,x,x,x,x,x],
[7,2,4,8,3,1,5,9,6,x,x,x,x,x,x],
[2,5,6,7,8,9,3,1,4,6,7,8,2,9,5],
[1,7,9,3,4,5,6,2,8,3,5,9,1,7,4],
[3,4,8,1,2,6,7,5,9,1,2,4,3,8,6],
[x,x,x,x,x,x,8,4,1,2,6,5,9,3,7],
[x,x,x,x,x,x,9,7,5,4,1,3,8,6,2],
[x,x,x,x,x,x,2,6,3,8,9,7,4,5,1],
[x,x,x,x,x,x,5,9,2,7,8,1,6,4,3],
[x,x,x,x,x,x,4,8,6,5,3,2,7,1,9],
[x,x,x,x,x,x,1,3,7,9,4,6,5,2,8]]

sudoku_array[54] = [[5,2,4,9,8,6,7,3,1,x,x,x,x,x,x],
[9,6,3,5,1,7,8,4,2,x,x,x,x,x,x],
[8,1,7,4,2,3,9,5,6,x,x,x,x,x,x],
[6,8,1,2,3,9,5,7,4,x,x,x,x,x,x],
[3,7,2,1,4,5,6,9,8,x,x,x,x,x,x],
[4,5,9,6,7,8,2,1,3,x,x,x,x,x,x],
[1,4,5,7,6,2,3,8,9,2,4,6,5,1,7],
[7,3,6,8,9,4,1,2,5,7,8,9,3,6,4],
[2,9,8,3,5,1,4,6,7,1,3,5,8,2,9],
[x,x,x,x,x,x,6,3,4,8,9,7,1,5,2],
[x,x,x,x,x,x,2,9,8,4,5,1,7,3,6],
[x,x,x,x,x,x,5,7,1,6,2,3,9,4,8],
[x,x,x,x,x,x,8,5,3,9,6,4,2,7,1],
[x,x,x,x,x,x,9,1,6,5,7,2,4,8,3],
[x,x,x,x,x,x,7,4,2,3,1,8,6,9,5]]

sudoku_array[55] = [[8,2,6,7,1,9,5,3,4,x,x,x,x,x,x],
[1,5,4,2,6,3,7,9,8,x,x,x,x,x,x],
[9,3,7,4,5,8,2,6,1,x,x,x,x,x,x],
[3,7,5,8,4,6,9,1,2,x,x,x,x,x,x],
[2,1,8,9,3,7,6,4,5,x,x,x,x,x,x],
[6,4,9,5,2,1,8,7,3,x,x,x,x,x,x],
[5,6,2,1,7,4,3,8,9,2,1,4,5,6,7],
[7,9,1,3,8,2,4,5,6,8,9,7,2,3,1],
[4,8,3,6,9,5,1,2,7,5,6,3,4,9,8],
[x,x,x,x,x,x,5,3,4,7,8,9,1,2,6],
[x,x,x,x,x,x,7,9,8,1,2,6,3,4,5],
[x,x,x,x,x,x,6,1,2,3,4,5,7,8,9],
[x,x,x,x,x,x,2,4,1,9,5,8,6,7,3],
[x,x,x,x,x,x,8,6,3,4,7,1,9,5,2],
[x,x,x,x,x,x,9,7,5,6,3,2,8,1,4]]

sudoku_array[56] = [[2,7,8,6,9,3,4,5,1,x,x,x,x,x,x],
[3,9,5,4,8,1,6,7,2,x,x,x,x,x,x],
[6,1,4,2,5,7,8,9,3,x,x,x,x,x,x],
[8,3,7,9,4,6,1,2,5,x,x,x,x,x,x],
[9,6,2,8,1,5,3,4,7,x,x,x,x,x,x],
[5,4,1,7,3,2,9,6,8,x,x,x,x,x,x],
[1,2,3,5,6,9,7,8,4,5,2,1,9,6,3],
[4,5,6,3,7,8,2,1,9,8,6,3,5,7,4],
[7,8,9,1,2,4,5,3,6,9,7,4,8,1,2],
[x,x,x,x,x,x,9,5,7,6,1,2,4,3,8],
[x,x,x,x,x,x,1,2,8,4,3,5,6,9,7],
[x,x,x,x,x,x,4,6,3,7,9,8,2,5,1],
[x,x,x,x,x,x,3,4,2,1,5,6,7,8,9],
[x,x,x,x,x,x,6,7,1,2,8,9,3,4,5],
[x,x,x,x,x,x,8,9,5,3,4,7,1,2,6]]

sudoku_array[57] = [[5,6,7,2,8,9,3,4,1,x,x,x,x,x,x],
[4,8,9,1,3,7,5,6,2,x,x,x,x,x,x],
[1,2,3,4,5,6,8,9,7,x,x,x,x,x,x],
[6,4,5,9,7,8,1,2,3,x,x,x,x,x,x],
[2,9,8,5,1,3,6,7,4,x,x,x,x,x,x],
[3,7,1,6,2,4,9,8,5,x,x,x,x,x,x],
[7,3,4,8,9,5,2,1,6,3,4,5,7,8,9],
[9,5,2,7,6,1,4,3,8,1,7,9,2,5,6],
[8,1,6,3,4,2,7,5,9,2,6,8,1,3,4],
[x,x,x,x,x,x,5,4,1,6,8,2,9,7,3],
[x,x,x,x,x,x,6,7,2,4,9,3,8,1,5],
[x,x,x,x,x,x,8,9,3,7,5,1,6,4,2],
[x,x,x,x,x,x,1,2,4,8,3,6,5,9,7],
[x,x,x,x,x,x,3,6,5,9,1,7,4,2,8],
[x,x,x,x,x,x,9,8,7,5,2,4,3,6,1]]

sudoku_array[58] = [[1,8,9,3,5,6,7,2,4,x,x,x,x,x,x],
[3,5,7,1,2,4,9,6,8,x,x,x,x,x,x],
[2,4,6,7,8,9,1,5,3,x,x,x,x,x,x],
[9,6,5,4,3,8,2,7,1,x,x,x,x,x,x],
[7,2,4,9,6,1,3,8,5,x,x,x,x,x,x],
[8,1,3,2,7,5,4,9,6,x,x,x,x,x,x],
[4,3,8,6,9,7,5,1,2,4,3,6,8,9,7],
[5,9,1,8,4,2,6,3,7,8,9,1,4,5,2],
[6,7,2,5,1,3,8,4,9,5,2,7,3,1,6],
[x,x,x,x,x,x,1,2,8,3,4,5,6,7,9],
[x,x,x,x,x,x,7,5,3,1,6,9,2,4,8],
[x,x,x,x,x,x,9,6,4,2,7,8,1,3,5],
[x,x,x,x,x,x,2,7,1,6,5,4,9,8,3],
[x,x,x,x,x,x,3,8,5,9,1,2,7,6,4],
[x,x,x,x,x,x,4,9,6,7,8,3,5,2,1]]

sudoku_array[59] = [[5,6,7,2,8,9,1,3,4,x,x,x,x,x,x],
[1,2,3,4,5,6,8,7,9,x,x,x,x,x,x],
[4,8,9,1,3,7,2,5,6,x,x,x,x,x,x],
[6,4,5,7,9,8,3,1,2,x,x,x,x,x,x],
[2,9,8,5,1,3,4,6,7,x,x,x,x,x,x],
[3,7,1,6,2,4,5,9,8,x,x,x,x,x,x],
[8,3,4,9,7,5,6,2,1,3,4,5,7,8,9],
[9,5,2,8,6,1,7,4,3,1,8,9,2,5,6],
[7,1,6,3,4,2,9,8,5,2,6,7,1,3,4],
[x,x,x,x,x,x,1,5,4,6,7,2,3,9,8],
[x,x,x,x,x,x,2,6,8,4,9,3,5,7,1],
[x,x,x,x,x,x,3,7,9,8,5,1,6,4,2],
[x,x,x,x,x,x,4,1,2,7,3,8,9,6,5],
[x,x,x,x,x,x,5,3,6,9,1,4,8,2,7],
[x,x,x,x,x,x,8,9,7,5,2,6,4,1,3]]

sudoku_array[60] = [[8,6,7,9,4,1,3,5,2,x,x,x,x,x,x],
[5,1,2,8,7,3,9,6,4,x,x,x,x,x,x],
[9,4,3,6,2,5,1,7,8,x,x,x,x,x,x],
[1,7,4,3,9,6,2,8,5,x,x,x,x,x,x],
[3,2,5,4,1,8,7,9,6,x,x,x,x,x,x],
[6,9,8,7,5,2,4,3,1,x,x,x,x,x,x],
[2,3,1,5,8,9,6,4,7,5,8,9,1,2,3],
[7,8,9,2,6,4,5,1,3,2,4,6,7,8,9],
[4,5,6,1,3,7,8,2,9,1,3,7,4,5,6],
[x,x,x,x,x,x,3,5,1,4,2,8,6,9,7],
[x,x,x,x,x,x,7,6,2,3,9,1,5,4,8],
[x,x,x,x,x,x,9,8,4,6,7,5,3,1,2],
[x,x,x,x,x,x,1,3,5,8,6,2,9,7,4],
[x,x,x,x,x,x,2,7,6,9,1,4,8,3,5],
[x,x,x,x,x,x,4,9,8,7,5,3,2,6,1]]

sudoku_array[61] = [[5,7,3,9,1,8,2,4,6,x,x,x,x,x,x],
[1,6,2,4,5,3,8,9,7,x,x,x,x,x,x],
[9,8,4,2,7,6,1,5,3,x,x,x,x,x,x],
[4,1,5,8,3,7,9,6,2,x,x,x,x,x,x],
[6,3,7,1,2,9,5,8,4,x,x,x,x,x,x],
[8,2,9,6,4,5,3,7,1,x,x,x,x,x,x],
[7,9,6,3,8,1,4,2,5,6,8,1,3,9,7],
[3,4,8,5,6,2,7,1,9,4,2,3,5,6,8],
[2,5,1,7,9,4,6,3,8,5,9,7,4,2,1],
[x,x,x,x,x,x,8,5,3,1,7,9,2,4,6],
[x,x,x,x,x,x,9,6,7,2,4,8,1,3,5],
[x,x,x,x,x,x,1,4,2,3,5,6,7,8,9],
[x,x,x,x,x,x,2,7,1,8,6,4,9,5,3],
[x,x,x,x,x,x,3,8,4,9,1,5,6,7,2],
[x,x,x,x,x,x,5,9,6,7,3,2,8,1,4]]

sudoku_array[62] = [[5,8,1,6,7,2,3,4,9,x,x,x,x,x,x],
[6,7,4,8,9,3,1,2,5,x,x,x,x,x,x],
[2,3,9,4,5,1,6,7,8,x,x,x,x,x,x],
[9,2,7,3,4,6,8,5,1,x,x,x,x,x,x],
[1,4,6,5,2,8,9,3,7,x,x,x,x,x,x],
[3,5,8,7,1,9,4,6,2,x,x,x,x,x,x],
[4,9,2,1,3,5,7,8,6,3,1,9,2,4,5],
[7,6,5,9,8,4,2,1,3,4,8,5,6,7,9],
[8,1,3,2,6,7,5,9,4,6,2,7,1,3,8],
[x,x,x,x,x,x,4,5,8,1,3,2,9,6,7],
[x,x,x,x,x,x,1,2,9,7,4,6,5,8,3],
[x,x,x,x,x,x,3,6,7,9,5,8,4,1,2],
[x,x,x,x,x,x,8,3,5,2,6,1,7,9,4],
[x,x,x,x,x,x,9,4,1,5,7,3,8,2,6],
[x,x,x,x,x,x,6,7,2,8,9,4,3,5,1]]

sudoku_array[63] = [[2,3,6,9,7,8,4,5,1,x,x,x,x,x,x],
[4,9,7,3,1,5,6,8,2,x,x,x,x,x,x],
[5,8,1,2,6,4,7,9,3,x,x,x,x,x,x],
[7,5,3,8,9,6,1,2,4,x,x,x,x,x,x],
[9,6,2,7,4,1,8,3,5,x,x,x,x,x,x],
[8,1,4,5,3,2,9,7,6,x,x,x,x,x,x],
[3,4,5,6,8,9,2,1,7,8,5,4,3,6,9],
[1,2,9,4,5,7,3,6,8,7,9,1,2,4,5],
[6,7,8,1,2,3,5,4,9,6,2,3,7,1,8],
[x,x,x,x,x,x,7,3,5,4,1,8,9,2,6],
[x,x,x,x,x,x,9,8,6,5,7,2,1,3,4],
[x,x,x,x,x,x,1,2,4,9,3,6,5,8,7],
[x,x,x,x,x,x,8,9,3,2,4,5,6,7,1],
[x,x,x,x,x,x,4,5,2,1,6,7,8,9,3],
[x,x,x,x,x,x,6,7,1,3,8,9,4,5,2]]

sudoku_array[64] = [[3,7,5,9,6,8,1,4,2,x,x,x,x,x,x],
[2,9,8,5,4,1,6,7,3,x,x,x,x,x,x],
[6,1,4,3,7,2,9,8,5,x,x,x,x,x,x],
[7,4,2,8,9,5,3,1,6,x,x,x,x,x,x],
[9,5,6,7,1,3,4,2,8,x,x,x,x,x,x],
[8,3,1,6,2,4,7,5,9,x,x,x,x,x,x],
[4,8,9,2,3,7,5,6,1,7,8,9,2,3,4],
[5,6,7,1,8,9,2,3,4,1,5,6,7,8,9],
[1,2,3,4,5,6,8,9,7,2,3,4,1,5,6],
[x,x,x,x,x,x,4,7,5,3,1,2,9,6,8],
[x,x,x,x,x,x,9,8,2,4,6,7,3,1,5],
[x,x,x,x,x,x,6,1,3,5,9,8,4,7,2],
[x,x,x,x,x,x,3,4,8,6,2,1,5,9,7],
[x,x,x,x,x,x,7,5,9,8,4,3,6,2,1],
[x,x,x,x,x,x,1,2,6,9,7,5,8,4,3]]

sudoku_array[65] = [[3,4,5,2,6,7,8,9,1,x,x,x,x,x,x],
[1,8,9,3,4,5,6,7,2,x,x,x,x,x,x],
[2,6,7,1,8,9,3,4,5,x,x,x,x,x,x],
[9,7,8,4,1,2,5,6,3,x,x,x,x,x,x],
[6,1,2,5,7,3,9,8,4,x,x,x,x,x,x],
[5,3,4,6,9,8,1,2,7,x,x,x,x,x,x],
[8,9,3,7,2,1,4,5,6,1,3,7,8,9,2],
[7,5,6,8,3,4,2,1,9,6,8,4,5,3,7],
[4,2,1,9,5,6,7,3,8,9,2,5,6,1,4],
[x,x,x,x,x,x,1,4,2,7,5,8,9,6,3],
[x,x,x,x,x,x,5,6,3,2,1,9,4,7,8],
[x,x,x,x,x,x,9,8,7,3,4,6,2,5,1],
[x,x,x,x,x,x,3,2,4,5,6,1,7,8,9],
[x,x,x,x,x,x,6,7,1,8,9,2,3,4,5],
[x,x,x,x,x,x,8,9,5,4,7,3,1,2,6]]
