def deposit():
    while True:
        amount = input('what yould you like to deposit? $ ')
        if amount.isdiget():
            int(amount)
            if amount>0:
                break
            else:
                print('amaunt must be greater than 0.')
            else:
                print('please enter your number.')
                return amount