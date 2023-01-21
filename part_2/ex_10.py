input_year = int(input("Please type in a year: "))

if input_year % 100 == 0:
    if input_year % 400 == 0:
        print("That year is a leap year.")
    else:
        print("That is not a leap year.")        
elif input_year % 4 == 0:
    print("That year is a leap year.")

else:
    print("That year is not a leap year.")