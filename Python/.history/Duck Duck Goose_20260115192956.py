PLAYER_LIMIT = 30
game_started = False

player_list = []


def help_message():
    print('''
=== Duck Duck Goose – Help Menu ===

Available commands:

help     - Show this help menu
start    - Start the game
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
            print('Player limit reached (30). Cannot add more.')
            continue

        player_name = input('Enter player name: ').strip()

        if player_name in player_list:
            print('This player already exists.')
        elif player_name == '':
            print('Player name cannot be empty.')
        else:
            player_list.append(player_name)
            print(f'{player_name} added successfully.')

    elif command == 'remove':
        if game_started:
            print('You cannot remove players after the game has started.')
            continue

        player_name = input('Enter player name to remove: ').strip()

        if player_name in player_list:
            player_list.remove(player_name)
            print(f'{player_name} removed successfully.')
        else:
            print('Player not found.')

    elif command == 'players':
        if not player_list:
            print('No players yet.')
        else:
            print('Players:')
            for i, player in enumerate(player_list, 1):
                print(f'{i}. {player}')

    elif command == 'status':
        if game_started:
            print('Game status: STARTED')
        else:
            print('Game status: NOT STARTED')

        print(f'Number of players: {len(player_list)}')

    elif command == 'start':
        if game_started:
            print('Game already started.')
        elif len(player_list) < 2:
            print('Not enough players to start the game.')
        else:
            game_started = True
            print('🎉 Game started! 🎉')

    elif command == 'exit':
        print('Exiting game...')
        break

    else:
        print('Invalid command. Type "help" to see available commands.')
 