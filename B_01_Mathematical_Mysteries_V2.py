import random


# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if response is a word in the list
            if item == user_response:
                return item

            # check if user response iss the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if something is invalid
        print(error)
        print()


# instructions
def instructions():
    print('''
**** INSTRUCTIONS ****

You will pick between
---------------------------
        Easy mode
            &
        HARD MODE
---------------------------
Easy mode contains very simple math
(subtraction (-), addition (+))

Hard mode contains more complicated math equations
(multiplication)

Good Luck!!!
    ''')


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


# Main routine starts here

# Start with a Header
print('''
███╗   ███╗ █████╗ ████████╗██╗  ██╗███████╗███╗   ███╗ █████╗ ████████╗██╗ ██████╗ █████╗ ██╗     
████╗ ████║██╔══██╗╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔══██╗╚══██╔══╝██║██╔════╝██╔══██╗██║     
██╔████╔██║███████║   ██║   ███████║█████╗  ██╔████╔██║███████║   ██║   ██║██║     ███████║██║     
██║╚██╔╝██║██╔══██║   ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══██║   ██║   ██║██║     ██╔══██║██║     
██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║███████╗██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╗██║  ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝

███╗   ███╗██╗   ██╗███████╗████████╗███████╗██████╗ ██╗███████╗███████╗                           
████╗ ████║╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║██╔════╝██╔════╝                           
██╔████╔██║ ╚████╔╝ ███████╗   ██║   █████╗  ██████╔╝██║█████╗  ███████╗                           
██║╚██╔╝██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗██║██╔══╝  ╚════██║                           
██║ ╚═╝ ██║   ██║   ███████║   ██║   ███████╗██║  ██║██║███████╗███████║                           
╚═╝     ╚═╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝                           
------------------------------------------------------------------------------------------------------------------------                       
By Ronan O'Brien-Hall
''')

# yes_no and other lists
yes_no = ["yes", "no"]
difficulty_list = ["easy", "hard"]
easy_equation = ["+", "-"]

quiz_history = []

# initialise variables
mode = "regular"
questions_answered = 0
end_game = "no"
low_num = 0
high_num = 100
correct_answers = 0
incorrect_answers = 0

# instructions prompt
want_instructions = string_checker("Do you want to see the instructions? ", yes_no)

# Checks users enter yes (y) and no (n)
if want_instructions == "yes" or want_instructions == "y":
    instructions()

user_choice = string_checker("Choose Your Difficulty: ", difficulty_list)

# Ask user for number of rounds
num_questions = num_check("How many rounds would you like? Press <enter> to play Infinite Mode: ", low=1, exit_code="")

# ask user if ready to start
start_quiz = string_checker(f"Are you ready? ", yes_no)

if num_questions == "":
    mode = "infinite"
    num_questions = 5

# quiz loop starts here
if start_quiz == "yes":

    while num_questions > questions_answered:

        if end_game == "yes":
            break

        # Rounds Headings
        if mode == "infinite":
            question_heading = f"\n➕➖ Question {questions_answered + 1} (INFINITE MODE)✖️➗"
        else:
            question_heading = f"\n➕➖ Question {questions_answered + 1} of {num_questions} ✖️➗"

        print(question_heading)

        if user_choice == "easy":
            # create a randomised equation
            first_num = random.randint(low_num, high_num)
            second_num = random.randint(low_num, high_num)
            random_equation = random.choice(easy_equation)
            if random_equation == "+":
                answer = first_num + second_num

            else:
                answer = first_num - second_num
            user_answer = num_check(f"What is {first_num} {random_equation} {second_num}? ", low=-100,
                                    exit_code="xxx")

        else:
            # create a randomised equation
            first_num = random.randint(low_num, high_num)
            second_num = random.randint(low_num, high_num)
            answer = first_num * second_num
            user_answer = num_check(f"What is {first_num} X {second_num}? ", low=-1, exit_code="xxx")

        # check for correct answer
        if user_answer == answer:
            print("✔️ Correct!")
            correct_answers += 1

        # check that they don't want to quit
        elif user_answer == "xxx":
            # set end_game to use so that outer loop can be broken
            end_game = "yes"
            break

        else:
            print(f"✖️ Incorrect! the correct answer was {answer}")
            incorrect_answers += 1

        questions_answered += 1

        question_result = f"correct answer {answer} - user's answer {user_answer}"
        quiz_history.append(question_result)

        # if users are in infinite mode, increase number of rounds
        if mode == "infinite":
            num_questions += 1

if start_quiz == "no":
    print("You got stressed and ran out of the classroom! 😭")

# ask for permission to show stats
if questions_answered > 0:

    # display game history on request.
    see_stats = string_checker("Do you want to see your statistics? ")
    if see_stats == "yes":
        # output the statistics
        print("\n📈📊📉 Statistics 📈📊📉")
        print(
            f"Correct Answers: {correct_answers} | Incorrect answers: {incorrect_answers}")
        print()

    see_history = string_checker("Do you want to see the answer sheet? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

else:
    print("No results as you quit the quiz 🤦‍♂️")
