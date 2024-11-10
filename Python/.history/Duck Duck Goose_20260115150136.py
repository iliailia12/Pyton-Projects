PLAYER_LIMIT = 30
try:
    player_count = int(input('Enter number of players (max 30): '))
except ValueError:
    print('This is ivalid valiu error')

player_list = []

def help_messige():
        print('''
=== Duck Duck Goose – Help Menu ===

Available commands:

help — Show this help menu

start — Start the game

players — Show the list of players

add — Add a new player

remove — Remove a player

status — Show current game status

exit — Exit the game

Notes:

Commands are case-insensitive

Maximum number of players: 30

The game is played in a circular order (Duck → Duck → Goose)
''')
        
        
while True:
    Commands = input('Enter Commands :   ').lower()
    if Commands == 'help':
        help_messige()
    elif Commands == "add":
        if len(player_list) >= PLAYER_LIMIT:
            print('Palier limit is 30 you reached limit you can not add no mere')
            continue
        player_name = input('enter player name :  ')
        if player_name in player_list:
            print('this name is already in the palyer list...')
        else:
            player_list.append(player_name)
            print('the name is added in the game')
    elif Commands == 'remove':
        player_name = input('enter player name you wnat to be removed :  ')
        if player_name in player_list:
            player_list.remove(player_name)
            print('player name is sucsefully removed')
        else 