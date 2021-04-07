from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height = 300)
window.config(padx=20, pady=20)

def miles_to_km():
    #to capture what is typed lines 23-24
    miles= float(miles_input.get())
    km = int(miles *1.609)
    result_label.config(text= km)
    print("i got clicked")

miles_input = Entry(width=30)
print(miles_input.get())
miles_input.grid(column=1, row=0)

miles_label = Label(text="label", font=("Arial", 22, "bold"))
miles_label.config(text="miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=15, pady=15)

equal_label = Label(text="label", font=("Arial", 22, "bold"))
equal_label.config(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=15, pady=15)

result_label = Label(text="label", font=("Arial", 22, "bold"))
result_label.config(text="0")
result_label.grid(column=1, row=1)
result_label.config(padx=15, pady=15)

km_label = Label(text="label", font=("Arial", 22, "bold"))
km_label.config(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=15, pady=15)



button1 = Button(text="Calculate", command=miles_to_km)
button1.grid(column=1, row=2)













window.mainloop()