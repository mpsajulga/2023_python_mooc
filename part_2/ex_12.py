input_int_number = int(input("Number: "))

divisible_by_three = "Fizz"
divisible_by_five = "Buzz"
divisible_by_both_three_and_five = "FizzBuzz"

if input_int_number % 3 == 0 and input_int_number % 5 == 0:
    print(divisible_by_both_three_and_five)
elif input_int_number % 3 == 0:
    print(divisible_by_three)
else:
    print(divisible_by_five)