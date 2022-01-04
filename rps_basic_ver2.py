print('Rock...')
print('Paper...')
print('Scissor...')

# input player
player1 = input('Player 1, make your move: ')
print('*******No cheating*******\n' * 50)
player2 = input('Player 2, make your move: ')

# same move
if player1 == player2:
    # logic if they are using same move
    print('it\'s a tie')
# rock 
elif player1 == 'rock':
    if player2 == 'scissor':
        # logic rock vs scissor
        print('player1 wins!')
    elif player2 == 'paper':
        # logic rock vs paper
        print('player2 wins!')
# paper
elif player1 == 'paper':
    if player2 == 'rock':
         # logic paper vs rock
        print('player1 wins!')
    elif player2 == 'scissor':
         # logic paper vs scissor
        print('player2 wins!')
# scissor
elif player1 == 'scissor':
    if player2 == 'paper':
         # logic scissor vs paper
        print('player1 wins!')
    elif player2 == 'rock':
         # logic scissor vs rock
        print('player2 wins!')
else:
    # logic if the input are betweem rock, paper, and scissor
    print('Something went wrong!')
