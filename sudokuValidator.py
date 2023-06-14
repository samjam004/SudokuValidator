#Samuel Mount
#Jun 14, 2023

#Accepts a 9x9 board 2D array and determines if it's a valid sudoku puzzle,
#independent of completion status
def isValid(board):
    ROWS = 9
    COLS = 9

    rows, cols, boxs = {}, {}, {}

    for r in range(ROWS):
        for c in range(COLS):

            #Skips incomplete boxes
            if board[r][c] == ".":
                continue
            
            #Creates a new set with the row as the key 
            #if one doesn't exist already
            if r not in rows:
                rows[r] = set()
                        
            #Creates a new set with the column as the key 
            #if one doesn't exist already
            if c not in cols:
                cols[c] = set()

            #Creates a new set with the 3x3 box as the key 
            #if one doesn't exist already
            if (c // 3, r // 3) not in boxs:
                boxs[(c // 3, r // 3)] = set()
            
            #If there is a repeating value (1-9) in any of the 
            #sets, the function will return false
            if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or 
                board[r][c] in boxs[(c // 3, r // 3)]):
                return False
            
            #Will add the value of the current row and column to it's
            #respective set
            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            boxs[(c // 3, r // 3)].add(board[r][c])

    #If there are no repeats besides empty boxes marked with ".", returns true
    return True



if __name__ == "__main__":
    
    ex1_board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    ex2_board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    print(isValid(ex1_board))
    print(isValid(ex2_board))
