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