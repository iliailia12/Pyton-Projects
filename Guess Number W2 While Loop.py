secret_number = 9
Guess_count = 0
Guess_limit = 3
while Guess_count < Guess_limit:
    guess = int(input('Guess : '))
    Guess_count += 1
    if guess == secret_number:
        print('you won')
        break
else:
    print('sorry you faild!!!')