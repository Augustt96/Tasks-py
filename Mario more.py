from cs50 import get_int 

# ask for height
while True:
    height = get_int("Height: ")
    if height >= 1 and height <= 8:
        break

# print spaces and # according to the height    
for i in range(height):
    print(" " * (height - i - 1) + "#" * (i+1) + "  " + "#" * (i+1))