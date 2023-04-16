'''This program finds the second occurrence of a substring.
If there is no second (or first) occurrence, the program prints out a message accordingly.

The occurrences cannot overlap.'''

input_string = input("Please type in a string: ")
input_substring = input("Please type in a substring: ")

index = input_string.find(input_substring)
occurrence_count = 0

while index != -1:
    occurrence_count += 1
    if occurrence_count == 2:
        print(f"The second occurrence of the substring is at index {index}.")
        break
    index += len(input_substring)
    index = input_string.find(input_substring, index)

if occurrence_count < 2:
    print("The substring does not occur twice in the string.")
