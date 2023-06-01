# prolog
# Author: Darling
# 
'''
Purpose:
    This program focuses on state machines.
    Utilizing the process of traffic lights for design implementation.
    The traffic light flashes will have several iterations for further practice with state machines.

    UPDATE:
    For this iteration there will be three seperate turtles given G,Y,R colors which will be..
    visible or invisible to the user depending on the handler function
'''

import turtle # Tess becomes a traffic light.

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()

draw_housing()

tess.hideturtle()
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# ------ print(tess.pos())
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")


#create a second turtle for the yellow light
alex_Y = turtle.Turtle(shape="circle")
alex_Y.hideturtle()
#alex_Y.hideturtle()
alex_Y.shapesize(3)
alex_Y.penup()
alex_Y.fillcolor("orange")
alex_Y.goto(40.00,120.00)


#create a third turtle for the red light
alex_R = turtle.Turtle(shape="circle")
alex_R.hideturtle()
#alex_Y.hideturtle()
alex_R.shapesize(3)
alex_R.penup()
alex_R.fillcolor("red")
alex_R.goto(40.00,190.00)

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change the turtle visiblitiy
#...given the 3 different turtle colors

# This variable holds the current state of the machine
state_num = 0

# LIGHT LOCATIONS using .pos() method
'''
Yellow(40.00,120.00)
Red(40.00,190.00)
Green (40.00,50.00)
'''

counter = 0
def advance_state_machine():
    global state_num
    global counter
    if counter < 3: #loop traffic program for 3 iterations
        if state_num == 0: # Transition from state 0 to state 1 while one light remains visible on a timer
            tess.showturtle()
            alex_Y.hideturtle()
            alex_R.hideturtle()
            state_num = 1
            wn.ontimer(advance_state_machine,600)
        elif state_num == 1: # Transition from state 1 to state 2 while one light remains visible on a timer
            alex_Y.showturtle()
            alex_R.hideturtle()
            tess.hideturtle()
            state_num = 2
            wn.ontimer(advance_state_machine,600)
        else: # Transition from state 2 to state 0 while one light remains visible on a timer
            alex_R.showturtle()
            alex_Y.hideturtle()
            tess.hideturtle()
            state_num = 0
            wn.ontimer(advance_state_machine,600)
            counter += 1 #change global counter variable by adding +1
    else:
        wn.bye() #Shut the graphics window down
    
# Bind the event handler to the space key
#wn.onkey(advance_state_machine,"space")

#call the function
advance_state_machine()

wn.listen() # Listen for events
wn.mainloop()
