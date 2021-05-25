print('!!! Welcome to Number Guessing Game...!!!')
print("Let's Play & having FUN!!!")

import random
inp = random.randint(1,11)

user_guess = int(input('Enter a number between 1 to 10: '))

while user_guess not in range(1,11):
    print('Enter a correct value..!!')
    user_guess = int(input('Enter a number within range of 1 to 10: '))

while True:
    if user_guess < inp:
        print('Guessed number is smaller, Plz increase guessing!!')
        user_guess = int(input('Enter a greater number: '))

    elif user_guess > inp:
        print('Guessed number is greater, Plz decrease guessing!!' )
        user_guess = int(input('Enter a lesser number: '))

    else:
        print('!!!You got Right.. Wooya!! You WINS!!!')
        break