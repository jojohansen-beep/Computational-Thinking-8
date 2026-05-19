import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("cardinal2",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y+4)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y-4)
    
def move_left():
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x-4, y)
    
def move_right(): 
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x+4, y)

# drawing controls 

def draw():
    s1.pendown ()

def stop_drawing (): 
    s1.penup ()

def erase (): 
    s1.clear

def red_pen ():
    s1.color ("red")

window.onkeypress (red_pen, "r")
window.onkeypress (erase,"e")
window.onkeypress (stop_drawing,"q")
window.onkeypress (draw,"c")
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")



# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()