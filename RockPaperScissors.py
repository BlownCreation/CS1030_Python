from random import randint

chosen = randint(1,3)
#makes the computer choose a random number 1-3 with each number associated with rock, paper, or scissors.
                                        
if(chosen == 1):
    computer = 'rock'

elif(chosen == 2):
    computer = 'paper'

else:
    computer = 'scissors'

player = input('rock, paper or scissors?')
#makes the player type in their input

if(player == computer):
    print('Draw')

elif(player == 'rock' and computer == 'paper') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
    print('You win')

else:
    print('Computer Wins')
#computes all logical possibilities and prints out the proper response