# author:
# date:
# purpose: Winners

# This program contains errors
# find and fix them

# NOTE: all the errors are in one line
# If you change more than one line of code,
# you will lose 1 point per every other line changed or added
# (Adding your name to author and date doesn't count as code changes)


# input
name = input("Please enter first name: ")

is_OK_age = False

while is_OK_age == False:
    try:
        age = input("Please enter your age: ")
        age=int(age)
        is_OK_age = True
    except ValueError:
        print("Please enter age as a whole number")

# calculations
is_winner = name.lower() == "sally" or "Sam" and age > 21


# output
print(name, "age", age,  "is a winner:", is_winner)
