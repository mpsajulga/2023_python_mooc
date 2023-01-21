input_points = int(input("How many input_points [0-100]: "))

if input_points >= 0 and input_points <= 49:
    print("Grade: fail")
elif input_points >= 50 and input_points <= 59:
    print("Grade: 1")
elif input_points >= 60 and input_points <= 69:
    print("Grade: 2")
elif input_points >= 70 and input_points <= 79:
    print("Grade: 3")
elif input_points >= 80 and input_points <=89:
    print("Grade: 4")
elif input_points >= 90 and input_points <= 100:
    print("Grade: 5")
else:
    print("impossible!")