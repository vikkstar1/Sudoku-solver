from main import search_empty
from main import is_valid
from main import board
from main import draw_sudoku
def solve(b):
    find = search_empty(b)              
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):                           #checks every value for the empty cell
        if is_valid(b,i,(row,col)):
            b[row][col] = i                         #sets the new value that works
            if(solve(b)):                           #recursive call with the new value in the cell
                return True

            b[row][col] =0                           
                                                     #if the value does not work it sets it to 0
    return False        

draw_sudoku(board)
solve(board)
print("_______________")

draw_sudoku(board)