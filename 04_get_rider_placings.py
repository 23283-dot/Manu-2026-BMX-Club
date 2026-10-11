# gets placing ensuring that it's a number, is in the valid range, and isn't blank
def get_valid_placing_input(prompt):
    while True:
        try:
            placing = int(input(prompt))

            if placing > 50:
                print("Rider placing in race cannot be greater than 50.")
            elif placing < 0:
                print("Rider placing in race cannot be less than 0.")
            else:
                return placing
        except ValueError:
            # if it fails, print an error and the loop repeats
            print("That is not a valid number. Try again.")

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


test_riders_placings = get_riders_placings(['Manu', 'Stephen', 'Mieke'], 4)
print(test_riders_placings)