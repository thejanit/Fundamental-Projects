import random

choices  = ['Rock', 'Paper', 'Scissor']
cpu = random.choice(choices)
player = False
player_score = 0
cpu_score = 0

while True:
    player = input("Choose from this: Rock, Paper and Scissor: ").capitalize()

    if player == cpu:
        print('Tie!!')

    elif player == 'Rock':
        if cpu == 'Paper':
            print('You Loose!!!')
            cpu_score += 1
        else:
            print('YOU Win!!')
            player_score += 1

    elif player == 'Paper':
        if cpu == 'Scissor':
            print('You Loose!!!')
            cpu_score += 1
        else:
            print('YOU Win!!')
            player_score +=1

    elif player == 'Scissor':
        if cpu == 'Rock':
            print('You Loose!!!')
            cpu_score += 1
        else:
            print('YOU Win!!')
            player_score += 1

    elif player == 'End':
        print(f'Final Score: CPU hits {cpu_score} and Player hits {player_score}')
        break