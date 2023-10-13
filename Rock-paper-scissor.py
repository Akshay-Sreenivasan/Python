# WAP that simulates a game of rock paper scissor.The program should ask the user for their choice(rock,paper or scissors) and then randomly generate a choice for the computer. the progeam should then print out the winner of the game(either the user and the computer choose the same option ,the game is tie)
# *Rock beats scissors
# *Scissors beats paper
# *Paper beats rock
import random
print('**********Select from the list**********')
print('1).Rock')
print('2).Paper')
print('3).Scissors')
usr=input('Enter the choice: ')
r=['rock','paper','scissors']
com = random.choice(r)
if (usr==com):
    print("It's a tie")
elif(com==r[0] and usr==r[2]):
    print('Computer Wins')
elif(com==r[1] and usr==r[0]):
    print('Computer Wins')
elif(com==r[2] and usr==r[1]):
    print('Computer Wins')
elif(usr==r[0] and com==r[2]):
    print('User wins')
elif(usr==r[1] and com==r[0]):
    print('User wins')
elif(usr==r[2] and com==r[1]):
    print('User wins')
else:
    print('***invalid input***')