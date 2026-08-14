# Checker for blank inputs
def get_non_blank_input(prompt):
    while True:
        user_input = input(prompt)

        # strip to remove any white space characters from start or end
        if user_input.strip():
            return user_input

        print("Value cannot be blank. Please try again.")