in_num_1 = int(input("Number 1: "))
in_num_2 = int(input("Number 2: "))

add = in_num_1 + in_num_2
multiply = in_num_1 * in_num_2
subtract = in_num_1 - in_num_2

operation = input("Operation: ")

if operation == "add":
    print(f"{in_num_1} + {in_num_2} = {add}")
if operation == "multiply":
    print(f"{in_num_1} * {in_num_2} = {multiply}")
if operation == "subtract":
    print(f"{in_num_1} - {in_num_2} = {subtract}")