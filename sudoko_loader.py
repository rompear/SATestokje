"""
Document: sudoku_loader.py
Made by: Romeo Goosens, Joe Harrison
UVA_numbers: 10424458, 11770430
"""

import os
import sys
import numpy as np
import random


"""
The class is a loader for all the possible sudokus, see main for testing this class
"""
class Loader(object):
    n = 0
    sudoku_array = [0]*109
    """docstring for Loader"""
    def __init__(self, n):
        super(Loader, self).__init__()
        self.n = n

        if(self.n == 1):
            import sudoku_1 as sudoku
        elif(self.n == 2):
            import sudoku_2 as sudoku
        elif(self.n == 3):
            import sudoku_3 as sudoku
        elif(self.n == 4):
            import sudoku_4 as sudoku
        elif(self.n == 5):
            import sudoku_5 as sudoku
        elif(self.n == 6):
            import sudoku_6 as sudoku
        elif(self.n == 7):
            import sudoku_7 as sudoku
        elif(self.n == 8):
            import sudoku_8 as sudoku
        self.sudoku_array = sudoku.sudoku_array

    def filter_sudoku(self, p):
        for i, sdk in enumerate(self.sudoku_array):
            sdk = np.array(sdk)
            sdk = sdk.astype(int)
            sdk_indices = np.where(sdk>0)
            random_sdk_indices = np.random.choice(sdk_indices[1].shape[0], int(sdk.size * p))
            sdk[(sdk_indices[0][random_sdk_indices], sdk_indices[1][random_sdk_indices])] = 0
            self.sudoku_array[i] = sdk.tolist()


if __name__ == '__main__':
    # Test the loader
    loader = Loader(1)
    loader = Loader(2)
    loader = Loader(3)
    loader = Loader(4)
    loader = Loader(5)
    loader = Loader(6)
    loader = Loader(7)
    loader = Loader(8)