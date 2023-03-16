'''
Please change the program from the previous exercise so that the user gets to input also the base which is multiplied (in the previous program the base was always 2).
'''

upper_limit = int(input("Upper limit: "))

numbers = 1
base = int(input("Base: "))

while numbers <= upper_limit:
    print(numbers)
    numbers *= base  