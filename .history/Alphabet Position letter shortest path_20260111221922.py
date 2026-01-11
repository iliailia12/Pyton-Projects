def position(letter):
    Letter = 'abcdefghijklmnopqrstuvwxyz'
    count = 0 
    for i in Letter:
        if Letter[count]==letter:
            return f'Position of Letter: {count +1}'
        else:
            count+=1