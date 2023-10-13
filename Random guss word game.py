import random
name = input("What is your name? ")
print("Good Luck ! ", name)
words = ['apple','orange','computer','keyboard','paper','python']
word=random.choice(words)
print('Guess the Characters: ')
guesses=''
chance=6
while chance > 0:
    falied=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            falied=falied+1
    if (falied==0):
        print(name,'Wins')
        print('The word is:',word)
        break
    print()
    guess=input('guess a character: ')
    guesses+=guess
    if guess not in word:
        chance-=1
        print('Wrong')
        print('You have',chance,'more guesses')
        if chance==0:
            print(name,'Loose')