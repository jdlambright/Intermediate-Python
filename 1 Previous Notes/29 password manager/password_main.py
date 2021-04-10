from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

#fail safe for twilio eEmKoSDr9SsUb5RPMJKUvXMyKvDMA-Bfsr8ULWaE

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #list of letters numbers and symbols
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #list comprehension to randomly choose list symbols and numbers
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    #combines all list into one and mixes selected numbers up
    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password= "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    #get data from what is typed
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    #set up JSON data
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    #message box
    if len(website) == 0  or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="you did not fill out all the required fields")

    else:
        #test to make sure that a data.json exist
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
                # updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w")as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


#-----------------------------Search Setup----------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="NOT FOUND", message="There are no saved password for this website")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n password{password}")
        else:
            messagebox.showinfo(title="NOT FOUND", message="There are no saved password for this website")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,)

canvas= Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo_img)
canvas.grid(column=1, row=0)

#labels
website_label= Label(text="Website: ")
website_label.grid(column=0, row=1)

username_label= Label(text="Email/Username: ")
username_label.grid(column=0, row=2)

password_label= Label(text="Password: ")
password_label.grid(column=0, row=3)


#entries
website_entry= Entry(width= 33)
website_entry.grid(column=1, row= 1)
website_entry.focus()

username_entry= Entry(width= 52)
username_entry.grid(column=1, row= 2, columnspan=2)
username_entry.insert(0, "josh.lambright@gmail.com")

password_entry= Entry(width= 33)
password_entry.grid(column=1, row= 3)


#buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)






window.mainloop()