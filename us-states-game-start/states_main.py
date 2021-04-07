import turtle
import pandas

#screen setup
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#read csv add states data to list
quote = pandas.read_csv("50_states.csv")
all_states = quote.state.to_list()
guessed_states = []


#create a continuous prompt until all states are guessed or exit code is typed
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 correct", prompt="Name a State: ").title()

    #checks for exit code. if its typed then it adds all missing states to new file
    if answer_state  == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("missing_states.csv")
        break

    #checks to see if an answer is in list of states and if it is prints the name of that state on the map
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = quote[quote.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




screen.exitonclick()