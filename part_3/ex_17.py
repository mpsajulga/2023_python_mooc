'''Please write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, from the shortest to the longest. 
'''

string = input("Please enter a string: ")

for i in range(1, len(string) + 1):
    substring = string[0:i]
    print(substring)