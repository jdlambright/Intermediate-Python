from tkinter import *
from quiz_brain import QuizBrain

#by importing QuizBrain that lets us know that allows us to
# specify the data type as a QuizBrain class in line 11

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain #this is what allows us to call functions from quiz_brain

        #window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        #labels
        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg= "white", font=("Ariel", 20, "bold"))
        self.score_label.grid(row=0, column= 1)

        #canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text="",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"You are finished! You got {self.quiz.score}/10 right!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        #line 53, 56-57 have the same outcome just typed 2 different ways
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
        #71 allow it to pause 1 sec and then calls the next question


# my mistakes when i converted to self.  I did not need self in front of true and false img. line 30 and 34
# also i forgot to add self to self.canvas in line 20
# both mistakes gave a not defined error

#canvas.config(pady=20) gave a not defined error as well i actually needed to put it in canvas.grid line 27

# window = Tk()
# window.title("Quizzler")
# window.config(padx=50, pady=50, bg=THEME_COLOR)
#
#
# #labels
# score_label = Label(text=f"Score: {0}", bg=THEME_COLOR, font=("Ariel", 20, "bold"))
# score_label.grid(row=0, column= 1)
#
# #canvas
# canvas = Canvas(width=250, height=250)
# question = canvas.create_text(100,100, text="question", font=("Ariel", 20, "bold"))
# canvas.grid(row=1, column=0, columnspan=2)
#
#
# # buttons
# true_img = PhotoImage(file="./images/true.png")
# true_button = Button(image=true_img)
# true_button.grid(row=2, column=1)
#
#
# false_image = PhotoImage(file="./images/false.png")
# false_button = Button(image=false_image)
# false_button.grid(row=2, column=0)
#
#
#
# window.mainloop()
#
