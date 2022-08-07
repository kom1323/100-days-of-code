
def caesar(text, shift, direction):

    text_lst = list(text)

    if direction == "decode":
        shift = -shift

    for index in range(len(text_lst)):
        if text_lst[index] in alphabet:
           new_char_index = (alphabet.index(text_lst[index]) + shift) % alphabet_len
           text_lst[index] = alphabet[new_char_index]

    text = "".join(text_lst)
    
    print (f"The {direction}d code is: {text}")


from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_len = len(alphabet)
program_state = "yes"

while program_state == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")  
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    program_state = input("Type 'yes' if you want to go again. Type 'no' if you want to exit the program.\n")
    if program_state == "no":
        print("Goodbye")



