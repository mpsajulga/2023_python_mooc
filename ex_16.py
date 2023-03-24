input_string = input("Word: ")
centered_input_string = input_string.center(28)
filler_char = "*"
required_char_count = 30
thirty_char = filler_char*required_char_count

print(thirty_char)
print(f"{filler_char}{centered_input_string}{filler_char}")
print(thirty_char)