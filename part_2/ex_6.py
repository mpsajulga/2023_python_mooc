print("Person 1:")
input_name_1 = input("Name: ")
input_age_1 = int(input("Age: "))

print("Person 2: ")
input_name_2 = input("Name: ")
input_age_2 = int(input("Age: "))

if input_age_1 > input_age_2:
    print(f"The elder is {input_name_1}")
if input_age_1 < input_age_2:
    print(f"The elder is {input_name_2}")
if input_age_1 == input_age_2:
    print(f"{input_name_1} and {input_name_2} are the same age")