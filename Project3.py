from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 200
x2 = -300
y2 = 50
x3 = - 300
y3 = -63
x4 = -300
y4 = -200
x5 = -200
y5 = -200



# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("MarioKartRainbowRoad.gif")
t1 = create_sprite("Pusheenraman.gif.gif",x1,y1)
t2 = create_sprite("DinoPusheen.gif",x2,y2)
t3 = create_sprite("Pusheenicorn3.gif",x3,y3)
t4 = create_sprite("MermaidPusheen2.gif",x4,y4)
t5 = create_sprite("Carpusheen.gif",x5,y5)


# Section 3 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# TODO - explain here which sprites are faster or slower

# Ramen pusheen is the fastest because it has the highest number which is eight therefore making Ramen pusheen having the hightest amount of speed. 
for i in range(30):
    x1 += 8 
    x2 += 4
    x3 += random.randint(1,7)
    x4 += 5

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.5)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("Pusheenraman.gif.gif",199,200)
s5.hideturtle()
window.update()
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    s5.color("white")
    s5.write("Ramen Pusheen wins!")


elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write("Dino Pusheen wins!")

elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    s5.write(" wins!")


turtle.exitonclick()