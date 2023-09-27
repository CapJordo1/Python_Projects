#Python Exercise - Dictionaries & Loops#
import time
# A list containing three seperate dictionaries, each represented with 'Name' & 'Age' keys #
def namefetch():
    profiles = [
        {
            'Name': 'Jordan',
            'Age': 27
        },
        {
            'Name': 'Haylie',
            'Age': 27
        },
        {
            'Name': 'Tater',
            'Age': 10
        },
        {
            'Name': 'Tootie',
            'Age': 1
        },
    ]
    # A function that prompts user input, converts the input to lowercase after stripping leading/trailing whitespace, and stores inside 'user_input' variable. #

    # Loop that iterates through the 'profiles' list. For each profile dictionary, checks if lowercase 'user_input' matches lowercase 'Name' key. #
    while True: #Add an infinite loop
        user_input = input('Enter Profile: ').strip().lower()
        profile_found = False #Flag to check if a profile is found
        for profile in profiles:
            if user_input == profile['Name'].lower():
                print('Loading User Profile...')
                time.sleep(3)
                print(f"Name: {profile['Name']}\nAge: {profile['Age']}")
                profile_found = True
                break
        if not profile_found:
                print('Profile not found.')
            
        another_search = input("Do you want to search another profile? (y/n): ").strip().lower()

        if another_search != 'y':
            print('Terminating Session...')
            time.sleep(3)
            break #Exit the loop if the user doesn't want to search again.

namefetch()