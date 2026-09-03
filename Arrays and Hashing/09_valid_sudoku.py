# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true


from typing import List

# Trabalhar primeiro as linhas
# Trabalhar as colunas

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        columns = dict()
        squares = dict()
        for row_index, row in enumerate(board):
            # Rows
            row_digits = [n for n in row if n.isdigit()]
            if len(set(row_digits)) != len(row_digits):
                print("row conditi")
                return False
            for column_index,digit in enumerate(row):
                if digit.isdigit():
                    # Columns
                    column = columns.get(column_index)
                    if column:
                        if digit in column:
                            print("col condition")
                            return False
                        else:
                            columns[column_index].append(digit)
                    else:
                        columns[column_index] = list()
                        columns[column_index].append(digit)
                        
                    # square_index = round((row_index / 3) * 3 + (column_index / 3)) TODO: check why this does not work
                    #But this does
                    square_index = (row_index // 3) * 3 + (column_index // 3)
                    square = squares.get(square_index) 
                    if square:
                        if digit in square:
                            print("square condition")
                            return False
                        else:
                            squares[square_index].append(digit)
                    else:
                        squares[square_index] = list()
                        squares[square_index].append(digit)
                            
                        
        print(f"squares: {squares}")              
        print(f"columns:",columns)  
                    
        return True
    
instance = Solution()


print(instance.isValidSudoku([
 ["1","2",".",".","3",".",".",".","."],
 ["4","1",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 [".",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
 ]))


# print(instance.isValidSudoku([
#  ["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]
#  ]))

