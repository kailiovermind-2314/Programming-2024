"""
A classic problem. Given an unfilled sudoku, determine if the setup is valid.
The solution can simply be brute-forced.
"""
from itertools import chain

partialsudoku = [
  ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
  ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
  ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
  ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
  ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
  ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
  ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
  ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
  ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]

repetitions = []
rowvalid = False
columnvalid = False
boxvalid = False

# Check for repetitions in a row
for row in partialsudoku:
  row = list(filter(('.').__ne__, row))
  if len(row) == len(set(row)):
    rowvalid = True

# Check for repetitions in a column
for i in range(len(partialsudoku)):
  column = []
  for j in range(len(partialsudoku)):
    column.append(partialsudoku[j][i])
  
  column = list(filter(('.').__ne__, column))
  if len(column) == len(set(column)):
    columnvalid = True

# Check for repetitions in a box
for i in range(0, len(partialsudoku), 3):
  for j in range(0, len(partialsudoku), 3):
    box = list(filter(('.').__ne__, list(chain.from_iterable([row[j:j+3] for row in partialsudoku[i:i+3]]))))
    if len(box) == len(set(box)):
      boxvalid = True

print(rowvalid and columnvalid and boxvalid)
