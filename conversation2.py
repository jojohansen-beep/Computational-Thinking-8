# Section 1 - Your code
from utils import *
player_name = input("What is your name?    ")

set_background("summer")

s1 = create_sprite("kitten", -200, 0)
s2 = create_sprite("puppy", 200, 0)
s3= create_sprite("shark2", 0, -100)

s1.color("white")
s2.color("pink")
s3.color("darkblue")
time.sleep(5)


s1.write("Where are we?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
window.update()
time.sleep(1)

s2.write("in Hawaii!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s3.write("fish are friends not food!",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s2.clear()
window.update()
time.sleep(1)

s1.write(f"I'm looking for {player_name}",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

s1.clear()
s1.write("Have you seen them?",font = ("Arial", 20, "normal"))
window.update()
time.sleep(1)

######################################################################
# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()