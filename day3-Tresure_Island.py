print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


choice = input("You are on the beach. In front of you is a jungle. Do you want to enter the jungle or walk on the beach? (jungle/beach)")
if choice == "beach":
    print("suddenly sharks with legs come out of the water and eat you.")
    print("Game over.")
else:
    choice = input("You are in the jungle."
     "you see a road on your right but hear a river to your left."
     "Do you go to the road or the river? (road/river)")
    if choice == "road":
        print("You get ambushed by the locals, they make you their king and then eat you by their tradition.")
        print("Game over.")
    else:
        choice = ("You find the river. do you go up the river, across or down? (up/across/down)")
        if choice == "up":
            print("A dinosaur comes out of the jungle and eats you.")
            print("Game over.")
        elif choice == "down":
            print("You fall into the river and get swept away")
            print("Game over")
        else:
            print("You find the Tresure")
            print("YOU WIN!!!")
            
