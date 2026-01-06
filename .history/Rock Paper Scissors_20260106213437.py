import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input('type rock paper or q to quit. ').lower()
    if user_input == 'q':
        break
        if user_input not in ['Rock','paper','scissors']:
            continue
        
        random_number = random.radint()
print('good bye!!!')