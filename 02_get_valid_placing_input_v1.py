# checks for invalid placing and asks user to try again if invalid
def get_valid_placing_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input

        except ValueError:
            print("Value must be an number. Please try again.")


test_placing = get_valid_placing_input("Please enter rider's placing: ")
print(test_placing)
