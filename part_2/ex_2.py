input_word = str(input("Please type in a word: "))
length_of_input_word = (len(input_word))

if length_of_input_word < 2:
    print("Thank you")
    
if length_of_input_word > 2:
    print(f"There are {length_of_input_word} in the word {input_word}")
    print("Thank you")