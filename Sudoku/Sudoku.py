# This program solves Sudoku puzzles that can be solved using direct logic.
#  That is to say, it does not think more than one step ahead.
#  It can solve most medium difficulty puzzles.

#open text file containing unsolved sudoku puzzle, formatted as is
f = open("board.txt","r")
#read data from text file, save as list in var board
board = map(int,f.read().split())
#close file
f.close()

#removes options from entry in a list (eg. row, column, box) if those numbers are already solved in another square in the list
def removeOptions (lst):
    #vars in the list which have been solved (only one option) stored in used
    used = [x[0] for x in lst if len(x) == 1]
    #for unsolved squares (multiple options), solved options from the list are filtered out; solved squares remain unchanged
    lst = [filter(lambda y: y not in used, item) if len(item)>1 else item for item in lst]
    #filtered list returned
    return lst

#if square is only one which can take on certain value in a list, it takes on that value
def exclusive(lst):
    #when all options of list added together, options that only appear once stored in singles
    singles = [x for x in sum(lst,[]) if sum(lst,[]).count(x)==1]
    #for squares that contain singles, other options are filtered out
    lst = [filter(lambda y: y in singles, item) if len(filter(lambda y: y in singles, item))>0 else item for item in lst]
    #filtered list returned
    return lst

#formatting of text file board into all initial options
for num in range(81):
    #unsolved squares take on all possible options
    if board[num] == 0:
        board[num] = [1,2,3,4,5,6,7,8,9]
    #solved squares become single-length lists
    else:
        board[num] = [board[num]]

#runs the two filtering functions on rows, columns, and boxes
#repeats until board is solved, or only 81 options left (one per square)
while len(sum(board,[]))>81:
    #for each of the 9 lists (rows, columns, boxes)
    for num in range(9):
        #square indices in num-th row defined
        row = [board[x] for x in range(num*9,num*9+9)]
        #both filtering functions used on row
        row = exclusive(removeOptions(row))
        #row in board takes on the new row values
        board[num*9:num*9+9] = row

        #square indices in num-th column defined
        column = [board[x] for x in range(num,num+73,9)]
        #both filtering functions used on column
        column = exclusive(removeOptions(column))
        #column in board takes on new column values
        board[num:num+73:9] = column

        #upperleft square index in num-th box defined as bx1
        bx1 = num*3+18*(num/3)
        #box indices of num-th box defined based on bx1
        box = board[bx1:bx1+3]+board[bx1+9:bx1+12]+board[bx1+18:bx1+21]
        #both filtering functions used on box
        box = exclusive(removeOptions(box))
        #box in board takes on new box values
        board[bx1:bx1+3] = box[0:3]
        board[bx1+9:bx1+12] = box[3:6]
        board[bx1+18:bx1+21] = box[6:9]

#after board is solved, list of integers stored in complete
complete = [each[0] for each in board]
#each row of the completed board is printed on a separated line
for line in range(0,81,9):
    print complete[line:line+9]
