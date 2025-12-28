# ძირითადი კალკულატორი
# შეიქმნას პროგრამა, რომელიც ითვლის გადახედვა, გამრავლება, გამოტანა და დივიზია.
# შესანიშნავი გზა არის ოპერაციები ისე, რომ გამოიყენოთ if-else statements.



def calculator():
    print("შეარჩიე ოპერაცია: +, -, *, /")
    operation = input("ოპერაცია: ")

    num1 = float(input("შეიყვანე პირველი რიცხვი: "))

    num2 = float(input("შეიყვანე მეორე რიცხვი: "))

    # ოპერაციის მიხედვით გამოთვლა
    if operation == "+":
        result = num1 + num2
        print("რეზულტატი:", result)
    elif operation == "-":
        result = num1 - num2
        print("რეზულტატი:", result)
    elif operation == "*":
        result = num1 * num2
        print("რეზულტატი:", result)
    elif operation == "/":
        # აქ ვამოწმებთ, რომ არ იყოს 0-ს გაყოფა
        if num2 == 0:
            print("არ შეიძლება 0-ზე დაყოფა!")
        else:
            result = num1 / num2
            print("რეზულტატი:", result)
    else:
        print("არასწორი ოპერაცია! სცადეთ კვლავ.")

calculator()
