in_num = int(input("Please type in a number: "))

if in_num < 1000:
    print("This number is smaller than 1000")
    if in_num < 100:
        print("This number is smaller than 100")
        if in_num < 10:
            print("This number is smaller than 10")
    print("Thank you!")
else:
    print("Thank you!")