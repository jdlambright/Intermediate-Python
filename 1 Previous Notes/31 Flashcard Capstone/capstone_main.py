from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# read data
#the try and except are there to first see if there are existing words to learn if not it pulls from original list
try:
    quote = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFound:
    original_data = pandas.read_csv(".data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = quote.to_dict(orient="records")


# Functions
def next_card():
    #the reason we have windows.after_cancel is because the timer needs to reset with each card
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)


# ui setup
window = Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#this shows the french card and after 3 sec it will switch to english if not guessed
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=700, height=375, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(350, 200, image=card_front_img)
card_title = canvas.create_text(350, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(350, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()

