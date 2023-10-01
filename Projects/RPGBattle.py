import random
import time
import os
player_character = {
        'Name': 'Tater',
        'Level': 5,
        'HP': 15
    }
enemy_creature = {
    'Name': 'Bandit',
    'Level': 3,
    'HP': 10
}
riposte_used = False
# Introductory message to inform the player they are about to fight
print('\n\033[95mYou encountered a wild bandit!\n\033[0m')

# Define user's available moves and their damage amounts
available_moves = {
    'Sword Slash': 2,
    'Riposte': 0,
    'Fireball': 10,
    'Block': 5
}
enemy_movelist = {
    'Stab': 2,
    'Shakedown': 4,
}
# Gameplay loop start
while True:
    # Initialize character & enemy placeholders
    # Initialize enemy HP
    enemy_hp = 10

    # Initialize player HP
    player_hp = 15
    while True:
        # Start of inner loop. Displays available moves/damage to the user before they make a selection.
        print('\033[94mAvailable Moves:\033[0m' + '\nHP: ' + (f'\033[92m{player_hp}\033[0m') + (f'\nEnemy: \033[91m{enemy_hp}\033[0m'))
        for i, move_name in enumerate(available_moves.keys(), start=1):
            print(f'{i}: {move_name} - Damage: {available_moves[move_name]}')
        try:
            # Takes player input for choices
            player_choice = int(input("\n\033[93mSelect a move by typing the corresponding number...\033[0m\n"))
            if player_choice in range(1, 5) or str(player_choice) == 'Riposte':
                # Check if user's input is valid (from available_moves)
                selected_move_name = list(available_moves.keys())[player_choice - 1]
                damage_dealt = available_moves[selected_move_name]
                print(f'\nYou used {selected_move_name} and dealt \033[91m{damage_dealt}\033[0m damage!')
                time.sleep(1.5)

                # Apply damage to the enemy
                enemy_hp -= damage_dealt

                # Check if enemy is defeated (HP <= 0)
                if enemy_hp <= 0:
                    print('Congrats! You defeated the Bandit!\n')
                    break  # Exit the inner loop

                # Implement the enemy's attack (bandit's turn)
                enemy_move = random.choice(list(enemy_movelist.keys()))
                enemy_damage = enemy_movelist[enemy_move]

                # Apply damage to the player's creature.
                if player_choice == 2:
                    enemy_hp -= enemy_damage
                    print(f'The Bandit was parried & took \033[92m{enemy_damage}\033[0m Riposte damage!\n')
                    time.sleep(1.5)
                else:
                    player_hp -= enemy_damage
                    print(f'The bandit used {enemy_move} and dealt {enemy_damage}\n')
                    time.sleep(1.5)
                # Display bandit's move and damage dealt
                # Check if the player is defeated (HP <= 0)
                if player_hp <= 0:
                    print('Game Over!')
                    break  # Exit the inner loop
            else:
                print('Invalid input. Please enter a valid move (1-4).\n')
        except ValueError:
            print('Invalid input. Please enter a valid number.\n')

    # Ask the player if they want to play again
    play_again = input('\033[93mDo you want to play again? (y/n)\033[0m\n')
    if play_again.lower() != 'y':
        os.system('clear' if os.name == 'posix' else 'cls')
        break  # Exit the outer loop