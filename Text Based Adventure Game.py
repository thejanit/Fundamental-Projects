player_name = input('Enter your name: ')
energy_level = 10

directions = ('East', 'West', 'North', 'South')

print('Ready to Play...!!')

directions_input = input('Enter direction where you want to go?? :  ')

if directions_input == 'East':
    print(player_name, ' You are going in this direction with energy level {}, Be careful!!...Danger||Surprise.. is waiting for you.'
                       ' It is a Lion, You will be eaten By Lion YOU FINISH BYE!!'.format(energy_level))


elif directions_input == 'West':
    print(player_name, ' You are going in this direction with energy level {}, Be careful!!..Here it is a snake '
                       'and you bite by snake, Dont worry, It is less poisnous. So, your energy level is reduced.'
                       'Your new energy level is {}'.format(energy_level, energy_level - 2))
    directions_input = input('Now re-enter direction where you want to go?? :  ')


elif directions_input == 'North':
    print(player_name, ' You are going in this direction with energy level {}, Here it is a FIRE!!!. CAREFUL.'
                       ' So, you are fired'.format(energy_level - 6) )

elif directions_input == 'South':
    print(player_name, ' You are going in this direction with energy level {}. Here it is a Deep Lake. CAREFUL.. You suddenly jump'
                       ', no your energy levbel is {}'.format(energy_level, energy_level - 6))

else:
    print(player_name, ' You did not understand the Game, Dont Worry')


