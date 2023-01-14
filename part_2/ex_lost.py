input_number = int(input("Please type in a number: "))
if input_number>100:
    print("The number was greater than one hundred")
    input_number=input_number - 100
    print("Now its value has decreased by one hundred")
    print(f"Its value is now {input_number}")
else: 
    print(f"{input_number} must be my lucky number!")
    
print("Have a nice day!")
