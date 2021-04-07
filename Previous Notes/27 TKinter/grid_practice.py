from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height = 300)
window.config(padx=20, pady=20)

#button
def button_clicked():
    #to capture what is typed lines 23-24
    new_text= entry.get()
    my_label.config(text= new_text)
    print("i got clicked")

#label- create it and say how it will be laid out
my_label = Label(text="label", font=("Arial", 22, "bold"))
my_label.config(text="new text")
my_label.grid(column=0, row=0)
my_label.config(padx=15, pady=15)

#button
button1 = Button(text="button 1", command=button_clicked)
button1.grid(column=1, row=1)


button2 = Button(text="button 2", command=button_clicked)
button2.grid(column=2, row=0)


#Entries
input = Entry(text="type something", width=30)
print(input.get())
input.grid(column=3, row=2)


#pack() is going to put widgets on the screen in a logical manner but hard to customize
#place() uses x and y starting top left corner as 0,0  (100, 0) would move widget over 100 px and keep at top
#the downside of place() is you have to work and play with every single widget to get it where you want
#grid() system puts everything into columns and rows. it is relative to other widgets
# you cannot put grid() and pack() in the same program











window.mainloop()