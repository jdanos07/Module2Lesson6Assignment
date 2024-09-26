# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator Write a script that asks for 
# and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

user_first_name = input('Please provide your complete First name : ')
user_last_name = input('Please provide your complete Last name : ')
first_name = []
first_name.append(user_first_name.capitalize())
last_name = []
last_name.append(user_last_name.capitalize())

def name_len_validation():
    for f_name in first_name:
        if len(f_name) >= 2:
            for l_name in last_name:
                if len(l_name)>= 2:
                    print(f'Hello {f_name} {l_name}. It\'s a pleasure to see you')

        else:
            print(
                'Provided name dooes not meet criteria.' 
                '\nName must have a minimum of two charactes.'
                '\nPlease refresh to re-enter.'
                )
       
name_len_validation()
