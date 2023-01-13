"""
Please write a program which asks the user for two numbers. The program will then print out the sum and the product of the two numbers.

The program should function as follows:

Number 1: 3
Number 2: 7
The sum of the numbers: 10
The product of the numbers: 21
"""

in_num_1 = int(input("Number 1: "))
in_num_2 = int(input("Number 2: "))

sum = in_num_1+in_num_2
product = in_num_1 * in_num_2

print(f"The sum of the numbers: {sum}")
print(f"The product of the numbers: {product}")