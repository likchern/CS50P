"""
this class handles the interaction with the board and the display
"""
class Game:
    def __init__(self):
        self.board=[*range(0,9)]

    #display board state
    def __str__(self):
        board_str = f"""
         {self.board[0]} | {self.board[1]} | {self.board[2]}
        -----------
         {self.board[3]} | {self.board[4]} | {self.board[5]}
        -----------
         {self.board[6]} | {self.board[7]} | {self.board[8]}
        """
        return board_str

    #sets the x or o 
    def play(self,position,player):
        while moves_left(self.board):
            try:
                if not isinstance(int(position),int):
                    raise ValueError
                for b in range(len(self.board)):
                    if int(position) == self.board[b]:
                        self.board[b] = player
                        return    
                raise ValueError
            except ValueError:
                position=input('Invalid position: ')

"""
driver function
"""
def main():
    board=Game()
    player1='o'
    player2='x'
    while True:
        print(board)
        #human player
        position=input('position: ')
        board.play(position,player1)
        #if the game ends don't continue to player 'x'
        if win(board.board) == player1:
            print(board)
            print(f'{player1} wins!')
            break
        if not moves_left(board.board):
            print(board)
            print('its a tie!')
            break
        """
        replace the line below with these two lines if you want to play with another player
        position=input('position: ')
        board.play(position,player2)
        """
        board.play(find_best_move(board.board),player2)
        if win(board.board) == player2:
            print(board)
            print(f'{player2} wins!')
            break
        if not moves_left(board.board):
            print('its a tie!')
            break

"""
win condition
"""
def win(board):
    #horizontal win
    for i in range(0,7,3):
        if board[i] ==  board[i+1] and board[i+2] == board[i]:
            return board[i]
    #vertical win
    for i in range(0,3):
        if board[i] ==  board[i+3] and board[i+6] == board[i]:
            return board[i]
    #diagonal win
    if board[0] == board[4] and board[4] == board[8]:
        return board[4]
    if board[2] == board[4] and board[4] == board[6]:
        return board[4]
    return 

"""
check whether all spaces have been filled
"""
def moves_left(board):
    for box in board:
        if not (box == 'x' or box == 'o'):
            return True
    return False

"""
calculate the score of the game
"""
def minimax(board, depth, is_max,alpha=None,beta=None) : 
    SIZE=9
    #base case for recursion(game ends)
    if win(board)=='o':
        return 10 - depth
    elif win(board)=='x':
        return -10 + depth
    elif not moves_left(board):
        return 0
    
    if (is_max) :     
        best = -1000 
  
        # Traverse all cells 
        for i in range(SIZE):
               
            # Check if cell is empty 
            if not (board[i]=='o' or board[i]=='x'):
                temp=board[i]
                board[i] = 'o'

                # Call minimax recursively and choose 
                # the maximum value 
                best = max( best, minimax(board,depth + 1, not is_max, alpha, beta) )
                alpha = max( best, alpha)
                # Undo the move 
                board[i] = temp
                #alpha beta pruning
                if alpha is not None and beta is not None and beta <= alpha:
                    break
                
        return best
  
    # If this minimizer's move 
    else :
        best = 1000 
  
        # Traverse all cells 
        for i in range(SIZE) :         
            
            # Check if cell is empty 
            if not (board[i]=='o' or board[i]=='x'):
                temp=board[i]

                # Make the move 
                board[i] = 'x'

                # Call minimax recursively and choose the minimum value 
                best = min( best, minimax(board, depth + 1,not is_max, alpha, beta) )
                beta = min( beta, best)
                # Undo the move 
                board[i] = temp
            #alpha beta pruning
            if alpha is not None and beta is not None and beta <= alpha:
                    break
                
        return best

"""
find the best move
"""
def find_best_move(board) : 
    best_val = 1000 
    """
    Traverse all cells, evaluate minimax function for 
        all empty cells. And return the cell with optimal value. 
    """
    SIZE=9
    for i in range(SIZE) :     
        # Check if cell is empty 
        if not (board[i]=='o' or board[i]=='x'):
            temp = board[i]
            # Make the move 
            board[i] = 'x'
            # compute evaluation function for this move
            move_val = minimax(board, 0, True,-100,100) 

            # Undo the move 
            board[i] = temp
            if (move_val < best_val) :     
                best_val=move_val           
                best_move = i
    
    return best_move

if __name__ == '__main__':
    main()