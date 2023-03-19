'''Please modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.'''

width_input_string = int(input("Width: "))
height_input_string = int(input("Height: "))
hash = "#"
printed_hash_width = hash*width_input_string
base_line = 0

while height_input_string != base_line:
    print(printed_hash_width)
    height_input_string -= 1