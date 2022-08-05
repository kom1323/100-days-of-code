import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

chars = []

if nr_letters > 0:
    chars.append(letters)
if nr_symbols > 0:
    chars.append(symbols)
if nr_numbers > 0:
    chars.append(numbers)



pass_size = nr_letters + nr_numbers + nr_symbols
output_pass = ""

for n in range(0, pass_size):
    curr_char_type_amount = 0
    if nr_letters > 0:
        curr_char_type_amount += 1
    if nr_numbers > 0:
        curr_char_type_amount += 1
    if nr_symbols > 0:
        curr_char_type_amount += 1

    curr_char_type = random.randint(0, curr_char_type_amount - 1)

    if curr_char_type == 0:
        output_pass += random.choice(chars[0])
        nr_letters -= 1
        if nr_letters == 0:
            chars.remove(letters)
    elif curr_char_type == 1:
        output_pass += random.choice(chars[1])
        nr_symbols -= 1
        if nr_symbols == 0:
            chars.remove(symbols)
    else:
        output_pass += random.choice(chars[2])
        nr_numbers -= 1
        if nr_numbers == 0: 
            chars.remove(numbers)


print("Here is your password: " + output_pass)