from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

'''
in data we got 10 questions from the quiz api and saved it to "question_data" then data was imported here
that allowed us to make a list of the questions called question_bank using a for loop
(within the loop we referenced the Question class that we made in question model)
we put the quiz_bank into the QuizBrain class saved that to variable called quiz
then we put that into the Quizinterface class saved it to a variable called quiz_ui.
That allows to pull from all of that data in the user interface

'''

#while quiz.still_has_questions():   moved to quiz brain
    #quiz.next_question()

#print("You've completed the quiz")
#print(f"Your final score was: {quiz.score}/{quiz.question_number}")
