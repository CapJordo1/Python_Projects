#your_move = print('\nSelect one of the following attacks...\n\nCharge\nSlash\nFireball\n')
#their_move = print('The enemy launches an attack at you!')


#Gameplay loop start
while True:
    #Initialize character & enemy placeholders
    player_character = {
    "Name": "Hero", 
    "Level": 5, 
    "HP": 15
}
    enemy_creature = {
    "Name": "Bandit", 
    "Level": 3, 
    "HP": 10
}
    #Introductory message to inform player they are about to fight
    print("\nYou encountered a wild bandit!\n")

    #Define user's available moves and their damage amounts
    available_moves = {
        "Leg Sweep": 2,
        "Parry": 0,
        "Sword Slash": 4,
        "Magic Missile": 5
    }
    #Displays available moves/damage to the user
    print('Available Moves:')
    for move, damage in available_moves.items():
        print(f'{move} - Damage: {damage}')
    #Whitespace for readability of moves
    print('\n')







    #Asks player if they would like to play again, and breaks loop if no is selected
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() != "y":
        break