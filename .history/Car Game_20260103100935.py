command = ''
while command.lower() != 'quit':
    command = input('< ').lower() 

    if command == 'start':
        print('Car started')
    elif command == 'stop':
        print('Car stopped')
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit the program
        """)
    elif command != 'quit':  
        print("Sorry, I do not understand that.")
skincare_sect home_decor_sect bathroom_sect sports_fitness_sect accessories_sect kids_items_sect toys_sect 