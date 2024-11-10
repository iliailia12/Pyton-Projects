import random

PLAYER_LIMIT = 30
game_started = False

player_list = []
current_index = 0
goose_index = None


def help_message():
    print('''
=== Duck Duck Goose – Help Menu ===

Available commands:

help     - Show this help menu
start    - Start the game
next     - Say Duck / Goose
players  - Show the list of players
add      - Add a new player
remove   - Remove a player
status   - Show current game status
exit     - Exit the game

Notes:
- Commands are case-insensitive
- Maximum number of players: 30
- Minimum players to start: 2
''')


while True:
    command = input('Enter command: ').lower()

    if command == 'help':
        help_message()

    elif command == 'add':
        if game_started:
            print('You cannot add players after the game has started.')
            continue

        if len(player_list) >= PLAYER_LIMIT:
            print('Player limit reached (30).')
            continue

        name = input('Enter player name: ').strip()

        if not name:
            print('Player name cannot be empty.')
        elif name in player_list:
            print('This player already exists.')
        else:
            player_list.append(name)
            print(f'{name} added successfully.')

    elif command == 'remove':
        if game_started:
            print('You cannot remove players after the game has started.')
            continue

        name = input('Enter player name to remove: ').strip()

        if name in player_list:
            player_list.remove(name)
            print(f'{name} removed.')
        else:
            print('Player not found.')

    elif command == 'players':
        if not player_list:
            print('No players yet.')
        else:
            for i, p in enumerate(player_list, 1):
                print(f'{i}. {p}')

    elif command == 'status':
        print('Game status:', 'STARTED' if game_started else 'NOT STARTED')
        print('Players:', len(player_list))

    elif command == 'start':
        if game_started:
            print('Game already started.')
        elif len(player_list) < 2:
            print('Not enough players.')
        else:
            game_started = True
            current_index = 0
            goose_index = random.randint(0, len(player_list) - 1)
            print('🎉 Game started! 🎉')
            print('Use "next" to play Duck Duck Goose.')

    elif command == 'next':
        if not game_started:
            print('Start the game first.')
            continue

        current_player = player_list[current_index]

        if current_index == goose_index:
            print(f'🦢 GOOSE! 👉 {current_player}')
            print('🏁 Round finished!')
            game_started = False
        else:
            print(f'🦆 Duck → {current_player}')

        current_index = (current_index + 1) % len(player_list)

    elif command == 'exit':
        print('Exiting game...')
        break

    else:
        print('Invalid command. Type "help" to see available commands.')


# enumerate() არის Python-ის ჩაშენებული (built-in) ფუნქცია, რომელიც გამოიყენება იტერირებადი ობიექტის (მაგ. სიის, ტუპლის, სტრინგის) ელემენტებზე ინდექსთან ერთად გასავლელად.
# ის აბრუნებს წყვილებს (ინდექსი, ელემენტი).