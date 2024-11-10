PLAYER_LIMIT = 30
PALYER_NAMES = int(input('Enter player names  the limit is 30 palyers'))

Commands = ''

if Commands.lower() ==  'help':
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
    
elif Commands.lower() == 'start':
    print('game started')
