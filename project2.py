print ("")
print ("")
print ("")
Red_points = 0
Orange_points = 0 
Yellow_points = 0 
Green_points = 0 
Blue_points = 0 
Purple_points = 0 
Pink_points = 0
print("")
print ("1. Which candy do you like the best? Answer with the following letters A though G: ")
print("")
print ("A) Cherry lolly pops")
print ("B) Peach rings")
print ("C) Pineapple hi-chews")
print ("D) Green apple hard rock candy")
print ("E) Blue Jolly Ranchers")
print ("F) Grape flavored Nerds")
print ("G) Pink Starbursts")
print("")
Answer = input ("Type in your answer here: ")
if Answer == "A":
    Red_points += 1 
    print("")
    print("->> You chose Cherry lolly pops!")
    print ("")
elif Answer == "B":
    Orange_points += 1
    print("")
    print("->> You picked Peach rings!")
    print ("")
elif Answer == "C":
    Yellow_points += 1 
    print ("")
    print ("->> You selected Pineapple hi-chews!")
    print ("")
elif Answer == "D":
    Green_points += 1
    print ("")
    print ("You chose Green apple hard rock candy!")
    print ("")
elif Answer == "E":
    Blue_points += 1
    print ("")
    print ("->> You Picked Blue Jolly Ranchers!")
    print ("")
elif Answer == "F":
    Purple_points += 1
    print ("")
    print ("->> You selected Grape flavored Nerds!")
    print ("")
elif Answer == "G":
    Pink_points += 1
    print ("")
    print ("->> You chose Pink Starbursts!")
    print ("")
else:
    print (" You can answer with only A,B,C,D,E,D,E,F,or G!")

print("2. Which personality traits best describes you?")
print("")
print("1) confident and goal oriented") 
print("2) Energetic, optimistic, and likes to have fun")
print("3) Creative and enthusiastic")
print("4) Empathetic and enjoys helping others")
print("5) cool, logical, and precise")
print("6) smart, supportive, and caring") 
print ("7) sweet, generous, kind, and has a positive outlook ")
print("")
Answer = input ("Type in your answer here: ")
if Answer == "1":
    Red_points += 1 
    print("")
    print ("->> You chose option number one. You like to describe yourself as confident and goal oriented!")
    print("")
elif Answer == "2":
    Orange_points += 1
    print("")
    print("->> You picked two. You like to describe yourself as Energetic, optimistic, and likes to have fun!")
    print("")
elif Answer == "3":
    Yellow_points += 1
    print("")
    print("->> You selected three. You like to describe yourself as Creative and enthusiastic!")
    print("")
elif Answer == "4":
    Green_points += 1
    print("")
    print("->> You picked four. You like to describe yourself as Empathetic and enjoys helping others!")
    print("")
elif Answer == "5":
    Blue_points += 1
    print("")
    print("->> You selected five. You like to describe yourself as cool, logical, and precise!")
    print("")
elif Answer == "6":
    Purple_points += 1
    print("")
    print("->> You chose option six. You like to describe yourself as smart, supportive, and caring!")
    print("")
elif Answer == "7":
    Purple_points += 1
    print("")
    print("->> You chose option seven. You like to describe yourself as sweet, generous, kind, and has a positive outlook!")
else:
    print (" You can only answer with numbers 1-7!")
print("")
print("3. Do you prefer warmer or colder weather, or both?")
print("")
Answer = input ("Type in your answer here: ")

if Answer == "Warmer weather" or Answer == "warmer":
    Red_points += 1
    Yellow_points += 1
    print("")
    print("->> You prefer a more warmer environment!")
    print("") 
elif Answer == "both" or Answer == "Both":
    Pink_points += 1
    Purple_points += 1
    Orange_points += 1
    print("")
    print("->> Why have one when you can have both!? ")
    print("")
elif Answer == "colder weather":
    Green_points += 1
    print("")
    print("->> You favor colder weather!")
    print("")
elif Answer == "colder weather":
    Blue_points += 1
    print("")
    print("->> You favor colder weather!")
    print("")
print("4. How do you want to spend your weekend? Would you like to:")
print("")
print ("A) Play video games")
print ("B) Participate in a competitive sport")
print ("C) Hang out with friends")
print ("D) Walk outside and spend time in nature")
print ("E) Read a book")
print ("F) Work on an art project")
print ("G) Practice self care")
print("")
Answer = input ("Type in your answer here: ")
if Answer == "A":
    Red_points += 1
    print("")
    print("->> You chose to play video games!")
    print("") 
elif Answer == "B":
    Orange_points += 1
    print("")
    print("->> You would like to participate in a competitive sport! ")
    print("")
elif Answer == "C":
    Yellow_points += 1
    print("")
    print("->> it's fun to spend time with friends once in a while! ")
    print("")
elif Answer == "D":
    Green_points += 1
    print("")
    print("->> Good on you for touching grass! ")
    print("")
elif Answer == "E":
    Blue_points += 1
    print("")
    print("->> You chose to read a book! ")
    print("")
elif Answer == "F":
    Purple_points += 1
    print("")
    print("->> You chose to work on an art project. How creative! ")
    print("")
elif Answer == "F":
    Pink_points += 1
    print("")
    print("->> it's always good to practice self care! ")
    print("")
else:
    print (" You can answer with only A,B,C,D,E,D,E,F,or G!")
print("")
print(" 5. Which best describes you when working on a group project? You are normally the one who...") 
print("")
print ("1) Becomes the leader and takes charge")
print ("2) Motivates others and mentions new ideas") 
print ("3) Does a lot of the research and comes up with the facts")
print ("4) Making sure everyone feels included")
print ("5) brings a  artistic aspect to the project")
print ("6) combines creative ideas with organization")
print ("")
Answer = input ("Type in your answer here: ")
if Answer == "1":
    Red_points += 1 
    print("")
    print ("->> You are the natural leader of the group!")
    print("")
elif Answer == "1":
    Orange_points += 1
    print("")
    print("->> You are the natural leader of the group!")
    print("")
elif Answer == "2":
    Yellow_points += 1
    print("")
    print("->> You add an element of fun to the project and help keep others motivated!")
    print("")
elif Answer == "3":
    Green_points += 1
    print("")
    print("->> You bring a lot of work/detail into the project and are good at planning and organizing data!")
    print("")
elif Answer == "4":
    Blue_points += 1
    print("")
    print("->> You like to create a space where everyone is comfortable and included!")
    print("")
elif Answer == "5":
    Purple_points += 1
    print("")
    print("->> You are the artist of the group!")
    print("")
elif Answer == "6":
    Purple_points += 1
    print("")
    print("->> You like to think outside the box while bringing structure and organization to the project!")
    print("")
else:
    print (" You can only answer with numbers 1-7!")
print("")
# End seven different types of points
if Red_points > Orange_points and Red_points > Yellow_points and Red_points > Green_points and Red_points > Blue_points and Red_points > Purple_points and Red_points and Red_points > Pink_points:              
    print ("Final Results:")  
    print ("")
    print("Your personality reflects the color red!")  
    print ("")              
    print ("You are outgoing, ambitious, a natural born leader and can also be very competitive.")
elif Orange_points > Red_points and Orange_points > Yellow_points and Orange_points > Green_points and Orange_points > Blue_points and Orange_points > Purple_points and Orange_points > Pink_points:                
    print("Final results:")
    print ("")
    print("Your personality indicates the color orange!")
    print ("")
    print("You are energetic, optimistic, extroverted, and enjoy taking risks and going on fun adventures. But while people with orange personalities are optimistic and fun-loving,they also can be impatient and impulsive at times")
    print ("")
elif Yellow_points > Orange_points and Yellow_points > Red_points and Yellow_points > Green_points and Yellow_points > Blue_points and Yellow_points > Purple_points and Yellow_points > Pink_points: 
    print("Final results:")
    print ("")
    print (" Your personality indicates the color yellow!")
    print ("")
    print (" People with yellow personalities often radiate extreme optimism, high energy, enthusiasm, and cheerfulness just like the warm, positive rays of the sun! These individuals are extroverted social butterflies that thrive in social situations with a very creative and innovative nature.")
elif Green_points > Yellow_points and Green_points > Orange_points and Green_points > Red_points and Green_points > Blue_points and Green_points > Purple_points and Green_points > Pink_points: 
    print("Final results:")
    print ("")
    print ("Your personality reflects the color green!")
    print ("")
    print("Individuals who have a green personality type are generally very analytical, logical, and visionary. People with green personalities are also independent and prefer to work alone and possibly are disinterested when doing group work or in working with others. They also can be described as being perfectionists and value efficiency also tending to hold themselves up to high standards.")
elif Blue_points > Green_points  and Blue_points > Yellow_points and Blue_points > Orange_points and Blue_points > Red_points and Blue_points > Purple_points and Blue_points > Pink_points:
    print("Final results:")
    print ("")
    print ("Your personality indicates the color blue!")
    print ("")
    print ("People with blue personalities are caring, empathic, analytical, loyal, and sincere. They are also structured, team oriented, and like to strive for high standards. But due to their strong empathy and emotional nature they can be sensitive and take things personally. ") 
elif Purple_points > Red_points and Purple_points > Orange_points and Purple_points > Yellow_points and Purple_points > Green_points and Purple_points > Blue_points and Purple_points > Pink_points:
    print("Final results:")
    print ("")
    print ("Your personality reflects the color purple!")
    print ("")
    print (" people with purple personality traits are highly creative and imaginative often artists or dreamers. These individuals are described as compassionate, sensitive, unique, charismatic, and wise. Who value individuality and like to stand out from the crowd.")
elif Pink_points > Red_points and Pink_points > Orange_points and Pink_points > Yellow_points and Pink_points > Green_points and Pink_points > Blue_points and Pink_points > Purple_points:
    print("Final results:")
    print ("")
    print ("Your personality reflects the color pink!")
    print ("")
    print ("People who have pink personality traits are creative, sweet, generous and optimistic seeing things from rose tinted glasses perspective. Individuals who favor pink often have an gentle, empathetic nature, and calming energy while also representing vulnerability, confidence and youthful innocence.")