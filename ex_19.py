"""

Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

The program should function as follows:

Number 1: 2
Number 2: 1
Number 3: 6
Number 4: 7
The sum of the numbers is 16 and the mean is 4.0

"""

in_num_1 = int(input("Number 1: "))
in_num_2 = int(input("Number 2: "))
in_num_3 = int(input("Number 3: "))
in_num_4 = int(input("Number 4: "))

sum = in_num_1+in_num_2+in_num_3+in_num_4
mean = sum/4

print(f"The sum of the numbers is {sum} and the mean is {mean}")