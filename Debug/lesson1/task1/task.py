# author:
# date:
# purpose: Sales call

# This program contains errors
# find and fix them

# NOTE: all the errors are in one line
# If you change more than one line of code,
# you will lose 1 point per every other line changed or added
# (Adding your name to author and date doesn't count as code changes)


# input
name = input("Please enter your name: ")
city = input("Please enter your city: ")

age = 0

while age <= 0:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Please enter age as a whole number")


# calculations
is_sales_call = city == "portland" or "Hillsboro" and age > 21
# output
print("Call", name + ":", is_sales_call)
