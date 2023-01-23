from math import sqrt

while True:
    input_number = int(input("Please type in a number: "))

    if input_number < 0:
        print("Invalid number")
    elif input_number > 0:
        print(sqrt(input_number))
    elif input_number == 0:
        break
print("Exiting...")