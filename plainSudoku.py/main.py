board =  [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
         ]

def draw_sudoku(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:            #adds a line every 3 rows
            print("---------------------")

        for j in range(len(b[0])):
            if j % 3 == 0 and j!= 0:        #adds a separating line every 3 elements
                print("|", end="")

            if j == 8:                      #prints the last element in every row without anything after 
                print(b[i][j])

            else:
                print(str(b[i][j]) + " ", end="")   #prints the last row without a line

def search_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i , j)  #returns the index of the empty cell in the grid
    return None

def is_valid(b,num,pos):                
    for i in range(len(b[0])):                      
        if b[pos[0]][i] == num and pos[1] != i:            #checks if the number is present in the row
            return False
    
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i:             #checks if the number is present in the column
            return False

    #check the grid of the given position
    x_grid = pos[1] // 3                                    #gets the column of the grid(box)
    y_grid = pos[0] // 3                                    #gets the row of the grid
    for i in range(y_grid * 3,y_grid *3 +3):                
        for j in range(x_grid *3, x_grid *3 + 3):
            if b[i][j] == num and (i,j) != pos:             #checks if the number is present in a grid(box)
                return False

    return True 

draw_sudoku(board)