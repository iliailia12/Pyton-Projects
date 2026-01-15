PLAYER_LIMIT = 30
try:
    player_count = int(input('Enter number of players (max 30): '))
except ValueError:
    print('This is ivalid valiu error')

player_list = []
Commands = input('Enter Commands')

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
    Commands == 'he'