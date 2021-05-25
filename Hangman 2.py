import random
import time

player_name = input('Enter your name: ')
print("Hello " + player_name + " Best of Luck")
time.sleep(2)

print('Game is about to begin!!!')

words = ['Pomegranate', 'Avengers', 'Republic', 'Tree', 'Family', 'Friends', 'India', 'Electronics']

word = random.choice(words)

print('\nGuess the letters...')

old_guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for letter in word:
        if letter in old_guesses:
            print(letter)
        else:
            print('_')

        failed += 1

    if failed == 0:
        print('\nHurray!! YOU WIN !!!')
        print('The word is', word)
        break

    guess = input('Guess a letter: ')

    old_guesses = old_guesses + guess

    if guess not in word:
        turns -= 1
        print('Wrong Guess')
        print('You have', + turns,  'left')

        if turns == 0:
            print('You Loose!!!')