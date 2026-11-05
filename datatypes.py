
agent = input("What is your real name, agent?: ")
fav_gadget = input("What is your favorite gadget?: ")

while True:
    try:
        secret_agent_id = int(input("What is your secret agent id?: "))
        speed_rate = int(input("What is your speed rate?: "))
        missions_count = int(input("What is your missions count?: "))
        height_m = round(float(input("What is your height (m)?: ")), 2)
        is_active = True
        break
    except ValueError:
        print("Sorry, you must enter a number!")
        continue