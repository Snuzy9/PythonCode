
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
    except:
        print('Something went wrong, try again!')
        continue

print(f"Agent: {agent} -> Type: {type(agent)}")
print(f'Favourite gadget: {fav_gadget} -> Type: {type(fav_gadget)}')
print(f'Secret agent id: {secret_agent_id} -> Type: {type(secret_agent_id)}')
print(f'Speed rate: {speed_rate} -> Type: {type(speed_rate)}')
print(f'Mission count: {missions_count} -> Type: {type(missions_count)}')
print(f'Height: {height_m} -> Type: {type(height_m)}')
print(f'Active: {is_active} -> Type: {type(is_active)}')

secret_agent_id_text = str(secret_agent_id)
speed_rate_text = str(speed_rate)
missions_count_text = str(missions_count)
height_m_text = str(height_m)
is_active_text = str(is_active)

print(f'Agent ID in text: {secret_agent_id_text} -> Type: {type(secret_agent_id_text)}')
print(f'Speed rate in text: {speed_rate_text} -> Type: {type(speed_rate_text)}')
print(f'Missions count in text: {missions_count_text} -> Type: {type(missions_count_text)}')
print(f'Height in text: {height_m_text} -> Type: {type(height_m_text)}')
print(f'Activity in text: {is_active_text} -> Type: {type(is_active_text)}')

first_three = agent[:3]
last_letter = agent[-1]
code_name = first_three + last_letter

print(f'First three letters of agent: {first_three}')
print(f'Last letter of agent: {last_letter}')
print(f'Secret code name: {code_name}')

reversed_gadget = fav_gadget[::-1]
print(f'Reversed gadget name: {reversed_gadget}')

badge_line1 = 'AGENT ' + code_name.upper()
badge_line2 = 'ID: ' + secret_agent_id_text.upper() + ' | MISSIONS ' + missions_count_text.upper()
badge_line3 = 'SPEED: ' + speed_rate_text.upper() + ' | ACTIVITY ' + is_active_text.upper()
badge_line4 = 'SECRET GADGET CODE: ' + reversed_gadget.upper()

print('')
print('===== SECRET AGENT BADGE =====')
print(badge_line1)
print(badge_line2)
print(badge_line3)
print(badge_line4)
print('==============================')