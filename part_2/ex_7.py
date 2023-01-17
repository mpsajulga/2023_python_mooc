input_first_word = str(input("Please type in the 1st word: "))
input_second_word = str(input("Please type in the 2nd word: "))

if input_first_word < input_second_word:
    print(f"{input_second_word} comes alphabetically last.")
elif input_first_word > input_second_word:
    print(f"{input_first_word} comes alphabetically last.")
else:
    print("You gave the same word twice.")