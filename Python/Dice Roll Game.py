import random

while True:
    coice = input('Roll The dice ?(y/n): ').lower()
    if coice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'({dice1}, {dice2})')
    elif coice == 'n':
        print('thanks for playing play more necxt time!')
        break
    else:
        print('Invalid choce')