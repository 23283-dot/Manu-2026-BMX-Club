import pandas as pd

# FUNCTIONS

# checks for blank input and ask user to try again if it is blank
def get_non_blank_input(prompt):
    while True:
        user_input = input(prompt)

        # strip to remove any white space characters from start or end
        if user_input.strip() == '':
            print("Value cannot be blank. Please try again.")
        else:
            return user_input

# checks for invalid placing and asks user to try again if invalid
def get_valid_placing_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input

        except ValueError:
            print("Value must be an number. Please try again.")

# get rider names and return the rider names
def get_rider_names(number_of_riders):
    rider_names = []

    for rider_index in range(number_of_riders):
        rider_name = get_non_blank_input(f"Enter rider #{rider_index + 1} name: ")
        rider_names.append(rider_name)

    return rider_names

# gets riders placings and returns their placing and points
def get_riders_placings(rider_names, number_of_races):
    riders_placings = {} # dictionary of the riders and their race placings

    for rider_name in rider_names:
        rider_placings = [] # used to store the rider's placings
        rider_total_points = 0 # used to keep track of the total points for rider

        for race_index in range(number_of_races):
            placing = get_valid_placing_input(f"Enter placing for rider {rider_name} in race #{race_index + 1}: ")

            if placing == 1:
                rider_total_points += 5 # 5 points for first place
            elif placing == 2:
                rider_total_points += 3 # 3 points for second place
            elif placing == 3:
                rider_total_points += 1 # 1 point for third place

            rider_placings.append(placing)

        rider_placings.append(rider_total_points)

        riders_placings[rider_name] = rider_placings

    return riders_placings


# CONSTANTS
NUMBER_OF_TEAM_RIDERS = 6
NUMBER_OF_RACES = 4


# MAIN ROUTINE

# get team name
print("---------- Team Name ----------")
team_name = get_non_blank_input("Enter your team name: ")
print()
print (f"Your team name is: {team_name}")
print()

# get rider names
print("---------- Team Rider Names ----------")
team_rider_names = get_rider_names(NUMBER_OF_TEAM_RIDERS)
print()
print("Your team riders are: ")
for team_rider_index in range(NUMBER_OF_TEAM_RIDERS):
    print(f"Rider #{team_rider_index + 1}: {team_rider_names[team_rider_index]}")
print()

# get rider placings and points
print("---------- Rider Race Placings ----------")
team_riders_placings = get_riders_placings(team_rider_names, NUMBER_OF_RACES)
print()

# create dataframe with riders placings
df = pd.DataFrame(team_riders_placings)

# create column for race and point labels
race_labels = []
for i in range(NUMBER_OF_RACES):
    race_labels.append(f"Race #{i + 1} placing")
race_labels.append("Total points")
df.insert(0, team_name, race_labels) # add label column to start of dataframe

# print out results
print(df.to_string(index=False))
print()



