import random

user_wins = 0
computer_wins = 0
options = ['Rock','Paper','Scissors']
            #  0        1     2
while True:
    user_input = input('type rock paper or q to quit. ').lower()
    if user_input == 'q':
        # break
        if user_input not in options:
            continue
        
        random_number = random.radint(0, 2)
        # rock 0 paper 1 scissors 2
        computer_pick = options[random_number]
        print(f'computer picked{computer_pick} + '".")
        
        if user_input == 'Rock'
print('good bye!!!')