#use backtracking concept to solve a sudoku board

#roadmap for backtracking solution:
    #pick empty square on board, then try all nums
        #as soon as viable number is found, move onto next empty square in same row, or next row if necessary, and repeat ^^^
#backtracking step::: erase value that is invalid, go to previous square, and repeat (recursive) 

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]

]

def solve(b):
    find =  find_empty(b) # tuple of row and column
    if not find: #base case of recursive algorithm
        return True
    else:
        row, col = find # set var row, col to respective val in tuple

    for i in range(1, 10): #loop thru 1 - 9 and check if by adding such sol to board if it is valid
        if valid(b, i, (row, col)): # if the value i is VALID, then set it to such value
            b[row][col] = i

            if solve(b): #recursively call solve with new value added to board, until we find new solution
                return True

            b[row][col] = 0 #if solve is not true, BACKTRACK, and reset the value at hand to 0, and repeat such process recursively
    return False




def valid(b, num, pos): # need to check row, column, and the slot we are in
    #check row
    for i in range(len(b[0])): #len of row
        if b[pos[0]][i] == num and pos[1] != i: #pos[0] is row value, pos[1] is col value
            return False # check if number inserted into row is not the same as existing number
        
    #check col
    for i in range(len(b)):
        if b[i][pos[1]] == num and pos[0] != i: #if num inserted at column value is equal to any other values in col
            return False
        

    #check 3 X 3 box (9 boxes in usual sudoku) 
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x*3 + 3): #creating the loop in the range of the box ! 
            if b[i][j] == num and (i, j) != pos:
                return False
            

    return True

            


def print_board(b):
    for i in range(len(b)): # i is row
        if i % 3 == 0 and i != 0:#divide board with lines every 3rd row (i % 3)
            print("- - - - - - - - - - - - - - - ") 

        for x in range(len(b[0])): #x is column
            if x % 3 == 0:
                print(" | ", end = "")
                

            if x == 8:
                print(str(b[i][x]) + " |") #if it is last value, no space for subsequent value
            else:
                print(str(b[i][x]) + " ", end="") # if it is not, then add space

#print_board(board)

def find_empty(b): # simple function to find empty slots in board
    for x in range(len(b)):
        for y in range(len(b[0])):
            if b[x][y] == 0:
                return (x, y) # return a tuple of x, y position in board (row, col)
    return None
            




def main() -> None: 
    print("_____________________________________")
    print("Unsolved Solution")
    print("_____________________________________")
    print_board(board)
    solve(board)
    print("_____________________________________")
    print("Solved Solution")
    print("_____________________________________")
    
    print()
    print_board(board)

if __name__ == '__main__':
    main()