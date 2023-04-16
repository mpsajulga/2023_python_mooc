input_string = input("Please type in a word: ")
input_character = input("Please type in a character: ")
index = input_string.find(input_character)

while index != -1:
    if len(input_string[index:]) >= 3: # check if substring from index+3 has at least 3 characters
        print(input_string[index:index+3])
    index += 1 # increment index by 1 to check the next possible substring
    index = input_string.find(input_character, index) # find the next occurrence of the input character starting from the updated index
    
'''
This program prints out all the substrings which are at least three characters long,
which begins with the character specified by the user.
It is assumed that the input string is at least three characters long.'''