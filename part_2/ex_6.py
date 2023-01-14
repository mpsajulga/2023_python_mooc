in_fahrenheit = float(input("Please type in a temperature (F): "))

celsius = ((in_fahrenheit - 32)*(5/9))


if celsius < 0:
    print(f"{in_fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")

else:
    print(f"{in_fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")