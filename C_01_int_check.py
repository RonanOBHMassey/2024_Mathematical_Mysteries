# checks users enter an int / float that is
# more than a minimum (default minimum is zero)
# Allows an 'exit' code
def num_check(question, num_type=int, low=0, exit_code="xxx"):
    error = f"Please enter an integer that is more than {low}"

    while True:
        # ask user question and return response if
        # exit code is entered
        response = input(question)
        if response == exit_code:
            return response

        # Check response is more than the minimum
        try:
            response = num_type(response)

            if response > low:
                return response
            else:
                print(error)

            # Show error if response is invalid
        except ValueError:
            print(error)


num_check("how many questions? ")

num_check("enter a random number ")
