
# Checker for blank inputs
def get_non_blank_input(prompt):
    while True:
        user_input = input(prompt)

        # strip to remove any white space characters from start or end
        if user_input.strip():
            return user_input

        print("Value cannot be blank. Please try again.")

NUMBER_OF_TEAM_RIDERS = 6

team_riders = []

team_name = get_non_blank_input("Enter your team name: ")
print (f'Your team name is: {team_name}')

for i in range(NUMBER_OF_TEAM_RIDERS):
    rider_name = get_non_blank_input(f'Enter name for Rider {i + 1}: ')
    team_riders.append(rider_name)

print ("Your team riders are:")
for i in range(NUMBER_OF_TEAM_RIDERS):
    print(f'Rider {i + 1}: {team_riders[i]}')