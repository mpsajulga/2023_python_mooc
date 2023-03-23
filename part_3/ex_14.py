"""Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. 
The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.

Sample output
Please type in a string: Hi there!

Hi there!
---------
Please type in a string: This is a test

This is a test
--------------
Please type in a string: a

a
-
Please type in a string:
"""



while True:
    input_string = input("Please type in a string: ")
    length_of_input_string = len(input_string)
    dash = "-"
    dash_length = length_of_input_string * dash
    
    if length_of_input_string > 0:
        print(input_string)
        print(dash_length)
    else:
        break