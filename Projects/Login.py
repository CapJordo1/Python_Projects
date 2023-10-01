#import time module to improve UX
import time

#initialize password str variable
pword = 'tootie'
attempts = 3
#start of password entry loop
while True:
    user_input = input('\n' + 'Attempts Remaining: ' + str(attempts) + '\nPlease enter a password: ')
    #'pword' if/else loop start || if initial password is correct, breaks. Else, repeats until correct.
    if user_input == pword:
        print('correct')
        break
    else:
        #'attempts' if/else loop start || continues until either user_input == pword OR attempts < 1.
        attempts = attempts - 1
        if attempts < 1:
            break