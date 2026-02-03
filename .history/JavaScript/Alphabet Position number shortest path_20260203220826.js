// python versions

def position(number):
    Letter = 'abcdefghijklmnopqrstuvwxyz'
    count = 1
    for i in Letter:
        if str(count) == number:
            return f'Letter at position {number}: {i}'
        count += 1
    return 'Invalid number'


number = input("Enter a number (1-26): ")
print(position(number))
