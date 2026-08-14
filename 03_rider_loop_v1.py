# set riders amount for a team
NUMBER_OF_TEAM_RIDERS = 6

TEAM_RIDERS = []
# loop for rider names
rider_total = 0
while rider_total < NUMBER_OF_TEAM_RIDERS:
    rider_name = input(f"Enter rider #{rider_total + 1} name: ")
    rider_total += 1
    TEAM_RIDERS.append(rider_name)

print("Your teams riders are: ")
for i in range(NUMBER_OF_TEAM_RIDERS):
    print("Rider {}: {}".format(i + 1, TEAM_RIDERS[i]))


