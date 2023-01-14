no_soup = "Jerry"
in_name = input("Please tell me your name: ")

if in_name == no_soup:
    print("Next please!")
else:
    in_portions = float(input("How many portions of soup? "))
    total_cost = in_portions * 5.90
    print(f"The total cost is {total_cost}")
    print("Next please!")