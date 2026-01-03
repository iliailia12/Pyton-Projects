def deposit():
    while True:
        amount = input('What would you like to deposit? $ ')
        
        if amount.isdigit():  # Corrected the typo here
            amount = int(amount)   amount
            if amount > 0:
                print(f'You have successfully deposited ${amount}.')
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a valid number.')

deposit()
