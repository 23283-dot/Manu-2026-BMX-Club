# checks for invalid placing and asks user to try again if invalid
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


test_placing = get_valid_placing_input("Please enter rider's placing: ")
print(test_placing)
