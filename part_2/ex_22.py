print("Please type in integer numbers. Type in 0 to finish.")
numbers_typed = 0
sum_of_input_integer_number = 0
mean_of_the_numbers = 0
negative_numbers = 0
positive_numbers = 0

while True:
    input_integer_number = int(input("Number: "))
    if input_integer_number == 0:
        break
    
    numbers_typed += 1
    sum_of_input_integer_number += input_integer_number
    mean_of_the_numbers = sum_of_input_integer_number/numbers_typed
    
    if input_integer_number > 0:
        positive_numbers += 1
    if input_integer_number < 0:
        negative_numbers += 1
       
print(f"Numbers typed in {numbers_typed}")
print(f"The sum of the numbers is {sum_of_input_integer_number}")
print(f"The mean of the numbers is {mean_of_the_numbers}")
print(f"Positive numbers {positive_numbers}")
print(f"Negative numbers {negative_numbers}")
