Name1 = 'Jordan'
Age1 = 27
Profile1 = f'Name: {Name1}\nAge: {Age1}'

def namefetch():
    user_input = input("Enter Profile: ")

    if user_input.lower() == 'profile1':
        print(Profile1)
    else:
        print('Incorrect Input')
namefetch()