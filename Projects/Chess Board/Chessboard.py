# Chessboard

import numpy as np
import random

cols =['1','2','3','4','5','6','7','8']
rows = ['A','B','C','D','E','F','G','H']

cols_alpha_index = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
rows_index_alpha = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}

# 8 x 8 chessboard - currently not using
c_b = [['A1','A2','A3','A4','A5','A6','A7','A8'],
       ['B1','B2','B3','B4','B5','B6','B7','B8'],
       ['C1','C2','C3','C4','C5','C6','C7','C8'],
       ['D1','D2','D3','D4','D5','D6','D7','D8'],
       ['E1','E2','E3','E4','E5','E6','E7','E8'],
       ['F1','F2','F3','F4','F5','F6','F7','F8'],
       ['G1','G2','G3','G4','G5','G6','G7','G8'],
       ['H1','H2','H3','H4','H5','H6','H7','H8']]


# Visual chessboard with letters - this is what is showing up in the blackbox
for this in range(8):
    for that in range(8):
        all_rows = rows[this] + cols[that]
        print(all_rows, end =' ')
    print()

# Chessboard with 0 values

# Function - 2D array

def cb_array():
    arr = []
    row,col = (8,8)
    arr=[[0]*col]*row
    for row in arr:
        print(row)
    return arr
print(cb_array())
