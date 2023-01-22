input_str_letter_1 = str(input("1st letter: "))
input_str_letter_2 = str(input("2nd letter: "))
input_str_letter_3 = str(input("3rd letter: "))


if input_str_letter_1 >= input_str_letter_2 and input_str_letter_1 <= input_str_letter_3 or input_str_letter_1 >= input_str_letter_3 and input_str_letter_1 <= input_str_letter_2:
    print(f"The letter in the middle is {input_str_letter_1}")
elif input_str_letter_2 >= input_str_letter_1 and input_str_letter_2 <= input_str_letter_3 or input_str_letter_2 >= input_str_letter_3 and input_str_letter_2 <= input_str_letter_1:
    print(f"The letter in the middle is {input_str_letter_2}")
else:
    print(f"The letter in the middle is {input_str_letter_3}")