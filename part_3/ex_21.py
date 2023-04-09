input_string = input("Please type in a word: ")
input_character = input("Please type in a character: ")
index = input_string.find(input_character)

while True:
    if input_character in input_string:
        if len(input_string[index:]) >= 3: # check if substring from index+3 has at least 3 characters
            print(input_string[index:index+3])
        break
    else:
        break