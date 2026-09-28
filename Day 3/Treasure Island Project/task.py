print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You're at a cross road which way do you want to go ?")
side = input("Do you wanna go left or right ?")
side = side.lower()
if side == "right":
    print("You fell in a hole! Game over")
elif side == "left":
    print("You reached a lake!")
    waiting = input ("do you want to wait for a boat or swim through the lake?")
    waiting = waiting.lower()
    if waiting == "wait":
        print("You made it through the lake safely")
        print("There are now three doors in front of you Red , Yellow and Blue ")
        door = input("Which door will you choose?")
        door = door.lower()
        if door == "red":
            print("Sorry you walked into the fire ! Game over")
        elif door == "yellow":
            print("Nice!! You found the treasure")
        elif door == "blue":
            print("Sorry you walked into the sky ! Game over")
    else:
        print("You tried to swim and drowned! Game over ")