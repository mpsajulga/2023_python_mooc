'''Please write a program which asks the user to type in a sentence.
The program then prints out the first letter of each word in the sentence, each letter on a separate line.'''

sentence = input("Please type in a sentence: ")
words = sentence.split() # Split the string into words

for word in words:
    print(word[0])