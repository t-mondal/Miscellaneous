import numpy as np

def invert(x):
  return int(not(x))

invert = np.vectorize(invert)

with open('board.txt', 'r') as f:
  board = invert(np.fromfile(f, int, -1, ' '))

# matrix side length is length of grid squared since there are rows and columns for each cell in the grid
msize = board.shape[0]

size = int(msize**0.5)

# matrix to hold augmented matrix values
matrix = np.zeros((msize, msize*2), dtype='i4')

# function to return left matrix of augmented matrix
def left(matrix):
  left = matrix[:,:msize]
  return left

# function to return right matrix of augmented matrix
def right(matrix):
  right = matrix[:,msize:]
  return right

# set up initial matrix where each row represents each square in the grid and each column represents each square
# there is a 1 in a cell if a the column's representative cell can toggle the row's representative cell

matrix[range(msize), range(msize)] = 1
matrix[range(msize-1), range(1, msize)] = 1
matrix[range(1, msize), range(msize-1)] = 1

matrix[range(size-1, msize-1, size), range(size, msize, size)] = 0
matrix[range(size, msize, size), range(size-1, msize-1, size)] = 0

matrix[range(msize-size), range(size, msize)] = 1
matrix[range(size, msize), range(msize-size)] = 1


# setting up identity on the right side of the identity matrix
matrix[range(msize), range(msize, msize*2)] = 1

# modified Gauss-Jordan elimination where values are mod 2; eg. 1 + 1 = 0
# left matrix: initial matrix -> identity matrix
# right matrix: identity matrix -> result matrix

print left(matrix)

for column in range(msize):
  print matrix
  if matrix[(column, column)] == 0:
    i = column
    while matrix[(i, column)] == 0:
      i += 1
    matrix[column] = (matrix[column] + matrix[i]) % 2
  for row in range(msize):
    if row != column:
      if matrix[(row, column)] == 1:
        matrix[row] = (matrix[row] + matrix[column]) % 2

right_matrix = right(matrix)

result = np.zeros(msize, dtype = 'i4')

for entry in range(msize):
  result[entry] = (np.sum(board * right_matrix[entry]))%2

with open('result.txt', 'w') as out:
  for x in range(size):
    for y in range(size):
      out.write(str(result[size*x+y]) + ' ')
    out.write('\n')