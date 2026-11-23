
try:
    temperature = int(input("Enter today's temperature in Celsius: "))

    if temperature < 20:
        outfit = "jacket"
        print("It is cold today")
        print(f"Wear a {outfit} today")
    else:
        outfit = "t-shirt"
        print("It is sunny today")
        print(f"Wear a {outfit} today")

    is_raining = input("Is it raining? (y/n): ").lower()

    if is_raining == "y":
        print("Bring an umbrella today!")

    has_puddles = input("Are there puddles on the ground? (y/n): ").lower()

    if has_puddles == "y":
        shoes = "boots"
        print("The ground is wet!")
        print(f"Wear {shoes} today")
    else:
        shoes = "sneakers"
        print("The ground is dry!")
        print(f"Wear {shoes} today")

    wind_speed = int(input("Enter wind speed in km/h: "))

    if wind_speed > 30:
        needs_windbreaker = True
        print("It is windy today!")
        print(f"Wear a windbreaker over your {outfit} today")
    else:
        needs_windbreaker = False
        print("It is not windy today!")
        print(f"It is calm today, no need to wear a windbreaker over your {outfit} today")

    print()
    print("Weather Check Complete!")

    print("==== WEATHER OUTFIT CHECKER ====")
    print(f"Temperature: {temperature}")
    print(f"Outfit chosen: {outfit}")
    print(f"Raining: {is_raining}")
    print(f"Needs windbreaker: {needs_windbreaker}")
    print(f"Shoes: {shoes}")
    print("================================")
except ValueError:
    print("Please enter a valid temperature")

