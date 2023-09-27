#Initialize character & enemy placeholders
import random

#Gameplay loop start
while True:
    
    #Initialize character & enemy placeholders
    player_character = {
    'Name': 'Hero', 
    'Level': 5, 
    'HP': 15
    }
    enemy_creature = {
    'Name': 'Bandit', 
    'Level': 3, 
    'HP': 10
    }
    
    #Introductory message to inform player they are about to fight
    print('\nYou encountered a wild bandit!\n')

    #Define user's available moves and their damage amounts
    available_moves = {
        '1': 2,
        '2': 0,
        '3': 4,
        '4': 5
    }
    
    #Initialize enemy HP
    enemy_hp = 10
    
    #Initialize player HP
    player_hp = 15
    
    #Displays available moves/damage to the user
    print('Available Moves:')
    for move, damage in available_moves.items():
        print(f'{move} - Damage: {damage}')
    
    while True:
        #Takes player input for choices
        player_choice = input('\nPlease choose a move... (1/2/3/4)\n')
        
        #Check if user's input is valid (from available_moves)
        if player_choice in available_moves:
            
            #Calculates damage value from player choice
            damage_dealt = available_moves[player_choice]
            print(f'You used {player_choice} and dealt {damage_dealt} damage!\n')
            
            #Apply damage to enemy
            enemy_hp -= damage_dealt
            
            #Display the enemy's remaining HP
            print(f'Enemy health remaining: {enemy_hp} \n')
            if enemy_hp <= 0: #Check if enemy is defeated (HP <=0)
                print('Congrats! You defeated the Bandit!\n')
                break #Exit game loop as the player wins
        else:
            print ('Invalid move. Please select a valid move.\n')

        #Implement the enemy's attack (bandit's turn)
        enemy_move = random.choice(list(available_moves.keys()))
        enemy_damage = available_moves[enemy_move]

        #Apply damage to the player's creature.
        player_hp -= enemy_damage

        #Display bandit's move and damage dealt
        print(f'The wild creature used {enemy_move} and dealt {enemy_damage}')

        #Check if player is defeated (HP <= 0)
        if player_hp <= 0:
            print('Game over!')
            break

    #Asks player if they would like to play again, and breaks loop if no is selected
    play_again = input('Do you want to play again? (y/n)')
    if play_again.lower() != 'y':
        break