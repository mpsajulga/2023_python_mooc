password = str(input("Password: "))

while True:
    password_verification = str(input("Repeat password: "))

    if password_verification != password:
        print("They do not match!")
    elif password_verification == password:
        break
print("User account created!")