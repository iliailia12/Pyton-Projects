
phone = input('Phone : ')
digits_mapping = {
    '1': 'one',
    '2': 'two',
    '3': 'tree',
    '4': 'four',
}

outfut = '' 
for ch in phone :
   outfut += digits_mapping.get(ch,'!') +  ''
print(outfut)