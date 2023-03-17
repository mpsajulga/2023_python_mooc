'''Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. 
If the strings are of equal length, the program should print out "The strings are equally long".

Some examples of expected behaviour:

Sample output
Please type in string 1: hey
Please type in string 2: hiya
hiya is longer'''

input_first_string = input("Please type in string 1: ")
input_second_string = input("Please type in string 2: ")

first_string = len(input_first_string)
second_string = len(input_second_string)

if first_string < second_string:
    print(f"{input_second_string} is longer")
elif first_string > second_string:
    print(f"{input_first_string} is longer")
else:
    print("The strings are equally long")