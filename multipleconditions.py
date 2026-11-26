
print("******** SCHOOL PLANNER ********")
weather = input("Enter weather: ").lower()

if weather == "sunny" and not weather == "rainy":
    print("It is sunny")
    homework_done = input("Did you do your homework?: ").lower()
    if homework_done == "yes" and homework_done != "no":
        print("Good job! You did your homework!")
    elif homework_done == "no" and homework_done != "yes":
        print("Oops! You forgot to do your homework!")
elif weather == "rainy" and not weather == "sunny":
    print("It is rainy")
    print("You should not go to school today!")
else:
    print("Invalid input!")