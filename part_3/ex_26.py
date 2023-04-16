'''
Please write a program which asks the user to type in an integer number.
If the user types in a number equal to or below 0, the execution ends.
Otherwise the program prints out the factorial of the number.

The factorial of a number involves multiplying the number by all the positive integers smaller than itself.
In other words, it is the product of all positive integers less than or equal to the number.
For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.
'''



while True:
    number = int(input("Please type in a number: "))
    factorial = 1    
    if number < 0:    
       print("Thanks and bye!")
       break
    elif number == 0:    
       print("Thanks and bye!")
       break
    else:    
       for i in range(1,number + 1):    
           factorial = factorial*i    
       print(f"The factorial of the number {number} is {factorial}")
       