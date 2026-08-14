# Functions

# Checker for blank inputs
def get_non_blank_input(prompt):
    while True:
        user_input = input(prompt)

        # strip to remove any white space characters from start or end
        if user_input.strip():
            return user_input

        print("Value cannot be blank. Please try again.")

# Set number of riders per team
NUMBER_OF_TEAM_RIDERS = 6
rider_total = 0

# Lists
TEAM_RIDERS = []

# Main routine

team_name = get_non_blank_input("Enter your team name: ")
print ('Your team name is: {}'.format(team_name))

# loop for rider names

while rider_total < NUMBER_OF_TEAM_RIDERS:
    rider_name = input(f"Enter rider #{rider_total + 1} name: ")
    rider_total += 1
    TEAM_RIDERS.append(rider_name)

print("Your teams riders are: ")
for i in range(NUMBER_OF_TEAM_RIDERS):
    print("Rider {}: {}".format(i + 1, TEAM_RIDERS[i]))
