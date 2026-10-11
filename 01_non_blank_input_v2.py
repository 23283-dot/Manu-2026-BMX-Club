# checks for blank input and ask user to try again if it is blank
def get_non_blank_input(prompt):
    while True:
        user_input = input(prompt)

        # strip to remove any white space characters from start or end
        if user_input.strip() == '':
            print("Value cannot be blank. Please try again.")
        elif not user_input.replace(" ", "").isalnum():
            print("Value must contain only letters, numbers and spaces. Please try again.")
        else:
            return user_input

test_name = get_non_blank_input("Please enter your name: ")
print(test_name)