#Ask user its answer
#If choice is valid or not
# If yes generate computer choice
# compare both the choices and declare winner also display emoji of rock paper scissor in the answer
#--------------------------------------------------------------------------------------------------
import random
choices = ('r','s','p')
emojis = {'r': '🪨', 's': '✂️', 'p' : '📄'}


while True :
    #if userguess != 'r' and userguess != 'p' and userguess != 's' :
    #    print('Invalid Choice')
    userguess = input('Rock, Paper or scissor?(r/p/s):').lower()
    if userguess not in choices :
        print('Invalid Choice')

    computer_choice = random.choice(choices)
    #if userguess =='r':
        #print('🪨')
    #elif user

    print(f'You choose {emojis[userguess]}')
    print(f'Computer choose  {emojis[computer_choice]}')

    if userguess == computer_choice:
        print('its a tie')
    elif (
    (userguess == 'r' and computer_choice == 's') or 
    (userguess == 's' and computer_choice == 'p') or 
    (userguess == 'p' and computer_choice == 'r')):
        print ('You Win')
    else : 
        print ('You Lose')

    should_continue = input('Continue? (y/n): ').lower()
    if should_continue == 'n':
      break
    #elif \
    # (userguess == 'r' and computer_choice == 's') or \
    # (userguess == 's' and computer_choice == 'p') or \
    #(userguess == 'p' and computer_choice == 'r'):