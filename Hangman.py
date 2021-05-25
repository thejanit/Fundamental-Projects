import random
import time

print('\n !!! Welcome to the Hangman Game !!!')

player_name = input('Enter your name: ')
print('Hello ' + player_name + ' All The BEST')
time.sleep(2)

print("The Game is about to start!! Let's play the Game & Having Fun" )
time.sleep(2)

def mains():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    words_to_be_guess = ['Pomegranate', 'Avengers', 'Czech Republic', 'Tree', 'Family', 'Friends', 'India', 'Electronics']

    word = random.choice(words_to_be_guess)
    length = len(word)
    display = '_' * length
    already_guessed = []
    play_game = " "

def play_loop():
    global play_game
    play_game = input("Do you want to play the game again?? y = yes, n = no\n")

    while play_game not in ['y', 'n', 'yes', 'no']:
        play_game = input("Do you want to play the game again?? y = yes, n = no\n")

        if play_game == 'y' or 'yes':
            mains()

        else:
            print('Thank You for playing this Game!!')
            exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game

    limit = 5

    guess = input('The Hangman Word: ' + display + 'Enter your guess: \n')
    guess.strip()

    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= '9':
        print('Invalid Input. Try again...')
        hangman()

    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + '\n')

    elif guess in already_guessed:
        print('try another letter..\n')

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print('  ----------- \n'
                  '  |           \n'
                  '  |           \n'
                  '  |           \n'
                  '  |           \n'
                  '  |           \n'
                  '__|__\n')
            print('Wrong Guess', str(limit - count), 'Guessess remaining\n')

        elif count == 2:
            time.sleep(1)
            print('  ----------- \n'
                  '  |         | \n'
                  '  |         | \n'
                  '  |           \n'
                  '  |           \n'
                  '  |           \n'
                  '  |           \n'
                  '__|__\n')
            print('Wrong Guess', str(limit - count), 'Guessess remaining\n')

        elif count == 3:
            time.sleep(1)
            print('  ----------- \n'
                  '  |         | \n'
                  '  |         | \n'
                  '  |         | \n'
                  '  |           \n'
                  '  |           \n'
                  '  |           \n'
                  '__|__\n')
            print('Wrong Guess', str(limit - count), 'Guessess remaining\n')

        elif count == 4:
            time.sleep(1)
            print('  ----------- \n'
                  '  |         | \n'
                  '  |         | \n'
                  '  |         | \n'
                  '  |         o \n'
                  '  |           \n'
                  '  |           \n'
                  '  |           \n'
                  '__|__\n')
            print('Wrong Guess', str(limit - count), 'Guessess remaining\n')

        elif count == 5:
            time.sleep(1)
            print('  ----------- \n'
                  '  |         | \n'
                  '  |         | \n'
                  '  |         | \n'
                  '  |         o \n'
                  '  |        /|\ \n'
                  '  |        /|\ \n'
                  '  |        / \ \n'
                  '__|__\n')
            print('Wrong Guess', str(limit - count), 'Guessess remaining\n')


        if word == '_' * length:
            print('Congrats!! You Win!!')
            play_loop()

        elif count != limit:
            hangman()

mains()
hangman()
