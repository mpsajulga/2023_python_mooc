'''
Please write a program which asks the user to type in a number.
The program then prints out all the positive integer values from 1 up to the number.
However, the order of the numbers is changed so that each pair or numbers is flipped.
That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.
'''

number = int(input("Please type in a number: "))

# Loop over the range of numbers and print them in the specified order
for i in range(2, number+1, 2):
    print(i)
    print(i-1)
    
# If the input number is odd, print the last odd number
if number % 2 == 1:
    print(number)