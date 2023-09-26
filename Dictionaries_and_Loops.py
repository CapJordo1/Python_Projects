#Python Exercise - Dictionaries & Loops#

# A list containing three seperate dictionaries, each represented with 'Name' & 'Age' keys #
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
def namefetch():
    user_input = input("Enter Profile: ").strip().lower()
# Loop that iterates through the 'profiles' list. For each profile dictionary, checks if lowercase 'user_input' matches lowercase 'Name' key. #
    for profile in profiles:
        if user_input == profile['Name'].lower():
            print(f"Name: {profile['Name']}\nAge: {profile['Age']}")
            break
    else:
        print('Profile not found.')

namefetch()