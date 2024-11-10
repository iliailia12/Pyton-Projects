# Python Project Idea – A countdown timer is a useful tool for keeping track of time. In this project, we will create a countdown timer using Python. We will first create a function to take   time in seconds and print it out in a formatted string. We will then use this function to create a countdown timer.

# The countdown timer will start at a given time and count down to zero. At each second, it will print out the remaining time. When the timer reaches zero, it will print out a message saying, “Time’s up!.” This project is a great way to learn about working with time in Python. It is also a useful tool that you can use in your projects.



# Python-ის პროექტის იდეა – დროის თვალყურის დევნების სასარგებლო ინსტრუმენტია უკუთვლის ტაიმერი. ამ პროექტში, Python-ის გამოყენებით შევქმნით უკუთვლის ტაიმერს. თავდაპირველად შევქმნით ფუნქციას, რომელიც დროს წამებში გამოთვლის და ფორმატირებულ სტრიქონში დაბეჭდავს. შემდეგ ამ ფუნქციას გამოვიყენებთ უკუთვლის ტაიმერის შესაქმნელად.

# უკუთვლის ტაიმერი ჩაირთვება მოცემულ დროს და ნულამდე დაითვლის. ყოველ წამს ის დაბეჭდავს დარჩენილ დროს. როდესაც ტაიმერი ნულს მიაღწევს, ის დაბეჭდავს შეტყობინებას: „დრო ამოიწურა!“. ეს პროექტი შესანიშნავი საშუალებაა Python-ში დროსთან მუშაობის შესასწავლად. ის ასევე სასარგებლო ინსტრუმენტია, რომლის გამოყენებაც შეგიძლიათ თქვენს პროექტებში.




import time

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

def countdown_timer(start_time):
    while start_time > 0:

        print(format_time(start_time), end="\r")  
        time.sleep(1)  
        start_time -= 1  

    # Once the countdown reaches 0
    print("00:00", end="\r")
    print("Time's up!")

# Get user input
try:
    user_input = int(input("Enter countdown time in seconds: "))
    countdown_timer(user_input)
except ValueError:
    print("Please enter a valid number!")
