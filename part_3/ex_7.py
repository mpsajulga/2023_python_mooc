'''Please write a new version of the program in the previous exercise. 
In addition to the result it should also print out the calculation performed:
for ex. 
Limit: 18
The consecutive sum: 1 + 2 + 3 + 4 + 5 + 6 = 21
'''

limit = int(input("Limit: "))
number = 1
result = 1
verdict = "1" + " "

while limit > result :
    number += 1
    verdict += (f"+ {number} ")
    result += number
    
print(f"The consecutive sum: {verdict} = {result}")