input_string = input("Please type in a string: ")
substring_a = "a"
substring_e = "e"
substring_o = "o"
true_condition = "found"
false_condition = "not found"

if substring_a in input_string:
    print(f"a {true_condition}")
else:
    print(f"a {false_condition}")

if substring_e in input_string:
    print(f"e {true_condition}")
else:
    print(f"e {false_condition}")

if substring_o in input_string:
    print(f"o {true_condition}")
else:
    print(f"o {false_condition}")