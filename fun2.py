


import turtle
turtle.goto(0,0)

UP = 0
DOWN= 1
LEFT= 2
RIGHT= 3
SPACE= 4
direction = None
pen_is_up = False


def up():
    global direction
    direction= UP
    print("You pressed the up key.")
    on_move(10, 20)
    
def down():
    global direction
    direction= DOWN
    print("You pressed the down key.")
    on_move(10, 20)
def left():
    global direction
    direction= LEFT
    print("You pressed the left key.")
    on_move(10, 20)
def right():
    global direction
    direction= RIGHT
    print("You pressed the right key.")
    on_move(10, 20)
def space():
    global direction
    direction= SPACE
    print("You pressed the space key.")
    on_move(10, 20)


    
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(space, "space") 
turtle.listen()

def on_move(x, y):
    global pen_is_up
    turtlepos =turtle.position()
    turtlexpos = turtlepos[0]
    turtleypos = turtlepos[1]
    if direction==UP:
         turtle.goto(turtlexpos, turtleypos+y)
         
    if direction==DOWN:
        turtle.goto(turtlexpos, turtleypos-y)

    if direction==LEFT:
        turtle.goto(turtlexpos-x, turtleypos)

    if direction==RIGHT:
        turtle.goto(turtlexpos+x, turtleypos)
    if direction==SPACE:
        if pen_is_up:
            turtle.pendown()
            pen_is_up= False
        else:
            turtle.penup()
            pen_is_up= True
















turtle.mainloop()
