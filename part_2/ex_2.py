in_number = int(input("Please type in a number: "))

if in_number < 0:
    absolute_value_of_number = in_number * -1
    print(f"The absolute value of this number is {absolute_value_of_number}")
else:
    print(f"The absolute value of this number is {in_number}")