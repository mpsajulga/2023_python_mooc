input_string = input("Please type in a string: ")
length_of_string = len(input_string)
exact_length = 20
filler_character = "*"
n = 0

while length_of_string != 20:
    length_of_string += 1
    n += 1
    
print(f"{filler_character*n}{input_string}")