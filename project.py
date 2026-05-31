import turtle

from cartooncharacters import *
from animals import *
from objects import *

choice = input("""
Choose a drawing:

Characters:
doraemon
pikachu
shinchan
nobita
hellokitty
mickey
minion
spongebob
totoro
smiley

Animals:
panda
cat
dog
bear
rabbit

Objects:
house
star
heart
flower
tree
rocket
robot
car
boat
icecream

Enter name:
""").lower()

if choice == "doraemon":
    draw_doraemon()

elif choice == "pikachu":
    draw_pikachu()

elif choice == "shinchan":
    draw_shinchan()

elif choice == "nobita":
    draw_nobita()

elif choice == "hellokitty":
    draw_hello_kitty()

elif choice == "mickey":
    draw_mickey()

elif choice == "minion":
    draw_minion()

elif choice == "spongebob":
    draw_spongebob()

elif choice == "totoro":
    draw_totoro()

elif choice == "smiley":
    draw_smiley()

elif choice == "panda":
    draw_panda()

elif choice == "cat":
    draw_cat()

elif choice == "dog":
    draw_dog()

elif choice == "bear":
    draw_bear()

elif choice == "rabbit":
    draw_rabbit()

elif choice == "house":
    draw_house()

elif choice == "star":
    draw_star()

elif choice == "heart":
    draw_heart()

elif choice == "flower":
    draw_flower()

elif choice == "tree":
    draw_tree()

elif choice == "rocket":
    draw_rocket()

elif choice == "robot":
    draw_robot()

elif choice == "car":
    draw_car()

elif choice == "boat":
    draw_boat()

elif choice == "icecream":
    draw_icecream()

else:
    print("Drawing not found.")

turtle.done()