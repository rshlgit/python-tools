'''
Haltstates is a program that takes in user responses to HALT questions
as input and prints the number of affirmative responses as output.

A HALT question is of the form:

    "Are you Hungry?"
    "Are you Angry?"
    "Are you Lonely?"
    "Are you Tired?"

These questions are asked in the same order as they are presented.

After each question, the program waits for a response from the user.
If the response is valid, the program asks the next question.
If the response is invalid, the program does NOT proceed and keeps 
prompting the user to input a valid response.

After four valid responses have been entered, the program prints a
count of affirmative responses and terminates.
'''

# create a list of HALT states as strings
states = ['Hungry', 'Angry', 'Lonely', 'Tired']


# create a list of questions using the previous list
questions = [f'Are you {state}? ' for state in states]


# create a function that returns 
#  1 if the input is valid and affirmative 
#  0 if the input is valid and not affirmative
# -1 if the input is invalid

def categoryOf(user_input):
    
    # make user_input case-insensitive
    user_input = user_input.lower()


    # define a list of affirmative and non affirmative responses
    affirmatives = ['t', '1', 'true', 'y', 'yes', 'yeah', 'i am']
    negatives    = ['f', '0', 'false', 'n', 'no', 'nope', 'i am not']

    # Note: These lists can accomodate many more valid responses
    # by importing large CSV or JSON type files and clever pattern matching


    # return either 1, 0, or -1 based on the category of the input
    if (user_input in affirmatives):
        return 1
    elif (user_input in negatives):
        return 0
    else:
        return -1


# this is the core logic of the program, read carefully 
# first define and set halt_count to 0 and index to 0
halt_count = 0
index = 0

# while index has not reached 4
while index < 4:

    # prompt the user with the question corresponding to current index
    # and store user response in user_input
    user_input = input(questions[index])

    # call categoryOf() function on user_input and store in input_category
    input_category = categoryOf(user_input)
    
    # add 1 to halt_count only if input_category is also 1  
    halt_count += (input_category == 1)

    # if input_category is invalid, print the invalid input message 
    # and decrement index by 1 
    if input_category == -1:
        print("Input not recognised, please enter valid input.")
        index -= 1
    
    # at the end of each iteration increase index by 1
    index += 1

# fancy output with borders
print("-" * 22)
print("Your HALT count is: ", halt_count)
print("-" * 22)
