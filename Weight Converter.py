weight = int(input('weight'))
uit =  input('(L)bs or (k)g: ')
if uit.upper() == "L":
    converted = weight * 0.45
    print(f'you are {converted} kilos')
else:
    converted = weight / 0.45
    print(f"you are {converted} pounds")