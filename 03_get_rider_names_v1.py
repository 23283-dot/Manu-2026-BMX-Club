# get user input and checks for blank value
def get_non_blank_input(prompt):
    while True:
        user_input = input(prompt)

        # strip to remove any white space characters from start or end
        if user_input.strip() == '':
            print("Value cannot be blank. Please try again.")
        else:
            return user_input

# get rider names and return the rider names
def get_rider_names(number_of_riders):
    rider_names = []

    for rider_index in range(number_of_riders):
        rider_name = get_non_blank_input(f"Enter rider #{rider_index + 1} name: ")
        rider_names.append(rider_name)

    return rider_names


test_rider_names = get_rider_names(4)
print(test_rider_names)
