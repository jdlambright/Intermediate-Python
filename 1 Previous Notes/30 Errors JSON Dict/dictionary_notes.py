else:
if website in data:
    email = data[website]["email"]
    password = data[website]["password"]
    messagebox.showinfo(title=website, message=f"Email: {email} \n password{password}")

'''

refer to day 29 password_main.py lines 74-80
note before we could read a dictionary we had to open the file it is in on line 70
the dictionary called website is in the data.json file
line 2 data is the file name
line 3 go to data look for the key website the value email which is also a key and return the value associated with it
line 4 go to data look for the key website the value password which is also a key and return the value associated with it

'''