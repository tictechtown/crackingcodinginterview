'''
Tic Tac Win: 
Design an algorithm to figure out if someone has won a game of tic-tac-toe.
'''


'''
-1 if X move
1 if O move
0 if no move
'''

def tictacwin(board:list[list[int]], play:int, move: tuple[int, int]) -> bool:

    # move has been made, we check col, row and diag
    board[move[0]][move[1]] = play
    n = len(board)
    sum_row = sum(board[move[0]])
    sum_col = sum([board[i][move[1]] for i in range(len(board)) ])

    if sum_row == play*n or sum_col == play*n:
        return True
    return False