from email.errors import MessageError
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.delete(0, "end")
    pass_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def pass_save():

    website = web_entry.get()
    username = username_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }

    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:        
        try:
            with open(r".\day29-password_manager\data.json", mode="r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open(r".\day29-password_manager\data.json", mode="w") as f:
                 json.dump(data, f, indent= 4)
            web_entry.delete(0, "end")
            pass_entry.delete(0, "end")


            

# ---------------------------- Search Function ------------------------------- #

def find_password():

    website = web_entry.get()

    try:
        with open(r".\day29-password_manager\data.json", mode="r") as f:
                    data = json.load(f)
    except:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
        else:
            messagebox.showerror(title="Error", message="No details for the website exists.")
            
        messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config( padx=20, pady=20)

#image canvas
canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file=r".\day29-password_manager\logo.png")
canvas.create_image(100,100, image=my_img)
canvas.grid(column=1, row=0)

#------------------labels------------------#

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)



#------------------entrys------------------#


web_entry = Entry(width=27)
web_entry.grid(column=1, row=1, columnspan=2, sticky='w')
web_entry.focus()

username_entry = Entry(width=27)
username_entry.grid(column=1, row=2, columnspan=2, sticky='w')
username_entry.insert(0, "omer2313@gmail.com")


pass_entry = Entry(width=24)
pass_entry.grid(column=1, row=3, sticky='w')

#------------------buttons------------------#

search_button = Button(text="Search", command=find_password, width=12)
search_button.grid(column=1, row=1, sticky='e', columnspan=2)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=1, row=3, sticky='e', columnspan=2)

add_button = Button(text="Add", width=36, command=pass_save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()