from tkinter import *
#if you are only using one piece of functionality its good to just type import tkinter
#however its better to use from tkinter import * if you are using a lot of different functions
#this prevents you from having to type tkinter.label() tkinter.Button() etc

window = Tk()
window.title("GUI")
window.minsize(width=500, height = 300)


#label- create it and say how it will be laid out


my_label = Label(text="label", font=("Arial", 22, "bold"))
#without pack the label will not appear
my_label.pack(side="top")

my_label.config(text="new text")

#button
def button_clicked():
    #to capture what is typed lines 23-24
    new_text= entry.get()
    my_label.config(text= new_text)
    print("i got clicked")

button = Button(text="click me", command=button_clicked) #when calling a function as method you do not need ()
button.pack()


#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="placeholder")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="yes", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="no", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()














window.mainloop()