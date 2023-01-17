input_age = int(input("What is your age? "))

if input_age >= 5:
    print(f"Ok, you're {input_age} years old")
if input_age > 0 and input_age <= 4:
    print("I suspect you can't write quite yet...")
if input_age <= 0:
    print("That must be a mistake")