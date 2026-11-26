
print("******* The Pool *******")
age = input("Enter your age group(0-5, 6-12, 13-17, 18-29, 30+): ")

if age == "0-5":
    print("Reminder: Wear floats")
    print("Use 'section 1' of the pool!")
    section = int(input("Enter your section number: "))
    match section:
        case 1:
            print("Perfect!")
        case 2:
            print("Please use 'section 1'!")
        case 3:
            print("Please use 'section 1'!")
        case 4:
            print("Please use 'section 1'!")
        case _:
            print("Invalid section! Try again!")
elif age == "6-12":
    print("Reminder: Wear floats")
    print("Use 'section 2' of the pool!")
    section = int(input("Enter your section number: "))
    match section:
        case 1:
            print("Please use 'section 2'!")
        case 2:
            print("Perfect!")
        case 3:
            print("Please use 'section 2'!")
        case 4:
            print("Please use 'section 2'!")
        case _:
            print("Invalid section! Try again!")
elif age == "13-17":
    print("Reminder: Wear floats (Optional)")
    print("Use 'section 3' of the pool!")
    section = int(input("Enter your section number: "))
    match section:
        case 1:
            print("Please use 'section 3'!")
        case 2:
            print("Please use 'section 3'!")
        case 3:
            print("Perfect!")
        case 4:
            print("Please use 'section 3'!")
        case _:
            print("Invalid section! Try again!")
elif age == "18-29":
    print("Use 'section 4' of the pool!")
    section = int(input("Enter your section number: "))
    match section:
        case 1:
            print("Please use 'section 3'!")
        case 2:
            print("Please use 'section 3'!")
        case 3:
            print("Please use 'section 3'!")
        case 4:
            print("Perfect!")
        case _:
            print("Invalid section! Try again!")
elif age == "30+":
    print("Sorry! You are too old for this pool!")
else:
    print("Invalid input! Try again!")