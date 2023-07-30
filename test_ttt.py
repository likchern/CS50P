from ttt import Game,win,moves_left,find_best_move
import pytest

def main():
    test_play()
    test_win()
    test_moves_left()
    test_find_best_move()

def test_play():
    #check that placement works if pos is valid
    test=Game()
    test.play(0,'o')
    assert(test.board) == ['o',1,2,3,4,5,6,7,8]


def test_win():
    #check that both x and o can win
    assert(win(['o','o','o','x','x','o','x','x','o'])) == 'o'
    assert(win(['x','o','o','x','x','o','x','x','o'])) == 'x'
    #horizontal check works
    assert(win(['o','o','o','x','x',5,6,7,8])) == 'o'
    #vertical check works
    assert(win(['o','o','o','x','x',5,6,7,8])) == 'o'
    #diagonal check works  
    assert(win(['o',1,'o','x','o','x','o',7,8])) == 'o'
    assert(win(['x',1,2,'o','x','o','o',7,'x'])) == 'x'

#check that the board state evaluation is working properly
#tie state
def test_moves_left():
    assert(moves_left(['o',1,'o','x','x','o','x','x','o'])) == True
    assert(moves_left(['o','o','o','x','x','o','x','x','o'])) == False


#the best move either wins the game or prevents the user from winning
def test_find_best_move():
    assert(find_best_move(['o',1,'o','x',4,5,6,7,8])) == 1
    assert(find_best_move(['o',1,'o','x','x',5,6,7,8])) == 5

if __name__=='__main__':
    main()