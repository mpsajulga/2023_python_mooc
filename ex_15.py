"""
Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:

What is your name? Frances Fictitious
Which year were you born? 1990
Hi Frances Fictitious, you will be 31 years old at the end of the year 2021

"""

in_name = input("What is your name? ")
in_year = int(input("Which year were you born? "))
calc_age = 2021-in_year
print(f"Hi {in_name}, you will be {calc_age} years old at the end of the year 2021")