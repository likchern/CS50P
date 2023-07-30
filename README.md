# Tic Tac Toe AI
#### Video Demo:  https://youtu.be/ZQ1iMZJ_JGw
#### Description:
####        This project is a simple project meant to warm up for the next course I plan to take which is the Introduction to AI. I wanted to make something related to AI but not overly complex or be overly reliant on prewitten tools as to understand how things work. This project can be separated into two segments which is the game component and the AI component. The project is relatively small hence all the functionality is implemented in the ttt.py file.

####        For the game component, I decided to use numbers instead of blanks to mark the state of the game as the user will interact with the game through the terminal and not mouse-click. The display and placement mechanisms are implemented in the Game class, while the logic could also be included into this class, CS50P requires the student to have multiple functions with the same indendation as main, as the other mechanims of the game such as win() and moves_left() directly interact with the minimax algorithm, I decided to place them outside the class. 
####        The win() function is designed only to handle the check for the current player and not both players because in tic tac toe there are three states, the player wins, the opponent wins or its a tie. while either side winning ends the game hence checking the who wins after checking whether an end state is reached will be faster than iterating over the list to check for both players.

####       For the AI component, there are finite number of states hence this is a pure strategy game, the AI will always tie if the player plays the optimal solution and will win elsewise. Tic tac toe can be viewed as a dynamic sequential game where the player will try to maximize their score during their turn and the AI will pick the minimum strategy during their turn to minimize their score. This game is non-probabilistic because the algorithm will iterate through every possible game. While optimization isn't required. The depth or the turns required and alpha beta pruning where used to optimize the performance by eliminating unecessary iterations. minimax is a recursive function that will play the game with itself until the best score is achieved, is_max determines whether the current turn player is the max player or the min player. The moves that are tried also directly interact with the board and then are undone after the check instead of creating a copy every time a new iteration is started. The program works even without the alpha beta, depth can also be removed without affecting the result of the program.

####        The score of 10 is decided as the maximum number of turns is 9, hence regardless of how long it takes to win or lose, the depth parameter does not change the end result of score, it only changes the magnitude.

