"""A number-guessing game."""

from random import randint

#choose random number between 1 and 100
numberOfTries = 0
number = randint(1, 100)

#greet player
print('Hey there!')

#get player name
name = input('What is your name? ')

#let the player know what the game is
print("I'm thinking of a number between 1 and 100")
print('Can you guess what the number is?')


#repeat forever:
while True:
    #get guess
    guess = input('What is your guess? ')
    #make sure guess is a valid guess
    try:
        guess = int(guess)
    except ValueError:
        print("For shame! Do you not know what a number is?")

    if guess < 1 and guess > 100:
        print('Seriously? Pick a number between 1 and 100!')  

    #increase number of guesses
    numberOfTries += 1      

    #if guess is incorrect:
    if guess < number:
        #give hint
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')    
    else:
        #congratulate player
        print(f'Great job {name}!')
        print(f'You guessed the answer in {numberOfTries} tries!')
        break
        

