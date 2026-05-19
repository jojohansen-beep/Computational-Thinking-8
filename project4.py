from utils import *
x1= 25
y1= -80
x2 = -200
y2 = 90
# Section 1 - setup
# TODO - set a background using set_background()
set_background("PusheenLivingRoom.gif")
m1 = create_sprite("lilpusheen.gif",x1,y1)
m2 = create_sprite ("lilfoodbowl2.gif",x2,x2 )


# TODO - create at least two variables and set their starting value. ex: cookies = 0
food = 0 
Hunger = 100
Health = 100
Happiness = 100


# OPTIONAL: use this invisible alien to say a message
m3 = create_sprite("alien", -100,200)
m3.hideturtle()
m4 = create_sprite("alien", -200,200)
m4.hideturtle()
m5 = create_sprite("alien", 50,200)
m5.hideturtle()
m6 = create_sprite("alien", 25,-90)
m6.hideturtle()
m7 = create_sprite("alien", 29,-70)


# Section 2 - controls
# TODO - define an action. ex: def my_control()
def create_food ():
    global food,Hunger
    food += 1 
    Hunger += 1
    x = -200
    y = - 200
    m3 = create_sprite("food.gif",x,y)
    time.sleep(0.9)
    m3.hideturtle ()
window.onkeypress (create_food, "space")



# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
   # m1.clear()
    #m1.write (f)
     # sittingpusheen3.gif.goto(x1,y1)
    
    # TODO - put any automatic actions here
    if food == 0: 
        if i % 40 == 0:
            Hunger -= 1
            if Hunger == 90:
                Health -= 2 

    
    # OPTIONAL - use the message sprite to say a message
    m3.clear()
    m3.write(f"Hunger = {Hunger}")
    m4.clear()
    m4.write(f"food = {food}")
    m5.clear()
    m5.write(f"Health = {Health}")

    for i in range(5):
                m6.clear()
                m6.write(f"Can I have some food?")
                time.sleep(0.5)
                m6.hideturtle()
                
                m7.clear()
                m7.write(f"meow :3")
                time.sleep(0.5)
                m7.hideturtle()
    
    time.sleep(0.01)
    window.update()