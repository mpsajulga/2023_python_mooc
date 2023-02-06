""""
attempts = 0
master_code_pin = 4321
input_code_pin = ""

while True:
    input_code_pin = input("PIN: ")
    attempts += 1
    
    if input_code_pin != "4321":
        print("Wrong")
    #elif input_code_pin == master_code_pin and attempts == 1:
       # break
        #print("Corect! It took you one single attempt!")
    elif input_code_pin == master_code_pin:
        break
        print(f"Corect! It took you {attempts} attempts")
""""
"""
pins = ""
attempts = 0
master_pin = 4321

while True:
    pin = input("PIN: ")
    attempts += 1
    pins += pin + ", "
    
    if pin == "4321":
        success = True
        break
    if pin != 4321:
        print("Wrong")

if success:
    if attempts == 1:
        print(f"Correct! It only took you one single attempt!")
        print(f"{pins}")
    else:
        print(f"Correct! It took you {attempts} attempts")
        print(f"{pins}")
"""