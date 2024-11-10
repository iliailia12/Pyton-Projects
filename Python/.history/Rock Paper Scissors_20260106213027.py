import random

user_wins = 0
computer_wins = 0

while True:
    user_input = input('type rock paper or q to quit. ').lower()
    if user_input == 'q':
        quit()
        if user_input in ['Rock','paper','scissors']:
            