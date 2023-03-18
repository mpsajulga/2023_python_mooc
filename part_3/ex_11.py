'''Please write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character are the same or not

Please type in a string: python
The second and the second to last characters are different

Sample output
Please type in a string: pascal
The second and the second to last characters are a
'''

input_string = str(input("Please type in a string: "))
second_character = input_string[1]
second_to_last_character = input_string[-2]

if second_character == second_to_last_character:
    print(f"The second and the second to last characters are {second_character}")
else:
    print("The second and the second to last characters are different")
