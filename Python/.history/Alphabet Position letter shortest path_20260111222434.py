letter = input("Enter a letter: ").lower()
print(position(letter))




        
def position(letter):
    Letter = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i in Letter:
        if i == letter:
            return f'Position of Letter: {count + 1}'
        count += 1
    return 'Invalid letter'
