def deposit():
    while True:
        amount = input('what yould you like to deposit? $ ')
        if amount.isdiget():
            int(amount)
            if amount>0:
                bre\