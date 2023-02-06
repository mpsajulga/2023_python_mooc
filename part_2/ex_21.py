compiled_words = ""
previous_word = None

while True:
    input_word = str(input("Please type in a word: "))
    
    if input_word == "end" or input_word == previous_word:
        break
    
    previous_word = input_word
    
    compiled_words += input_word + " "
    
print(compiled_words)