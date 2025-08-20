# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input('Please input a letter: ')
    vowelsArray = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if letter in vowelsArray:
        return print(f'The letter {letter} is a vowel')
    elif letter.isalpha():
        return print(f'The letter {letter} is a consonant')
    else:
        print('Invalid character. Please input a letter.')

# Call the function
check_letter()

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age = int(input('Please enter your age: '))
    legalAge = 18
    try:
        if age>=legalAge:
            print('You are eligible to vote! Yippie')
        else:
            print('Too baby to vote :(')
    except ValueError:
        print('Invalid input')
# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog = int(input("Input a dog's age: "))
    if dog > 2:
        dogYears = (dog - 2)*7 + 20
        print(f"Age in dog years: {dogYears}")
    elif dog > 0:
        dogYears = dog*10
        print(f"Age in dog years: {dogYears}")
    else:
        print('Invalid age')


# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold = input("Is it cold? (Yes/No/Y/N): ").upper()
    rain = input("Is it raining? (Yes/No/Y/N): ").upper()
    if (cold in ["YES", "Y"] and rain in ["YES", "Y"]):
        print("Wear a waterproof coat.")
    elif (cold in ["YES", "Y"] and rain in ["NO", "N"]):
        print("Wear a warm coat.")
    elif (cold in ["NO", "N"] and rain in ["YES", "Y"]):
        print("Carry an umbrella.")
    elif (cold in ["NO", "N"] and rain in ["NO", "N"]):
        print("Wear light clothing")
    else:
        print("Invalid input")
# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

def determine_season():
    # Your control flow logic goes here
    month_input = str(input("Enter the month of the year as three characters (Jan - Dec): ").upper())
    day_input = input("Enter the day of the month (as a number): ")
    if month_input not in MONTHS:
        print("Invalid month")
    day = int(day_input)
    if day < 1 or day > 31:
        print("Invalid day, please enter a number between 1 and 31")
    if not day_input.isdigit():
        print("Invalid input, please input a number between 1 and 31")
    month = MONTHS.index(month_input) + 1
    if (month in [1, 2]) or (month == 12 and day > 20) or (month == 3 and day < 20):
        print(f"{month_input} {day_input} Season is Winter")
    elif (month in [4, 5] or (month == 3 and day > 19) or (month == 6 and day < 21)):
        print(f"{month_input} {day_input} Season is Spring")
    elif (month in [7, 8] or (month == 6 and day > 20) or (month == 9 and day < 22)):
        print(f"{month_input} {day_input} Season is Suummer")
    elif (month in [10, 11] or (month == 9 and day > 21) or (month == 12 and day < 21)):
        print(f"{month_input} {day_input} Season is Fall")
    

# Call the function
determine_season()

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    # Your control flow logic goes here
    winning_number = 67
    for i in range(5):
        while True:
            try:
                guess = int(input("Guess a number between 1 and 100: "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    return
                else:
                    break
            except ValueError:
                    print("That's not a valid number. Try again.")
        if guess == winning_number:
            print("Yippiee you win")
            return
        elif guess < winning_number:
            if i < 3:
                print("Guess too low, please try again")
            elif i == 3:
                print("Guess too low. Last chance!")
            elif i == 4:
                return print("You lose")
        elif guess > winning_number:
            if i < 3:
                print("Guess too high, please try again")
            elif i == 3:
                print("Guess too high. Last chance!")
            elif i == 4:
                return print("You lose")

# Call the function
guess_number()