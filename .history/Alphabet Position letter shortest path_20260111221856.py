def position(letter):
    Alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = 0 
    for i in Alphabet:
        if Alphabet[count]==letter:
            return f'Position of alphabet: {count +1}'
        else:
            count+=1