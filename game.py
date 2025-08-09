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
choice1=input("You are walking and come across two path,which one do you choose? L for left and R for right")
if choice1=="L":
    print("Yay!You found a gift,you can move ahead!")
    choice2 = input("You move forward and see a river,what do you choose?W for wait and S for swim across the river")
    if choice2=="W":
        print("Yay!,You waited for some time and a boat helped you across the river")
        choice3 = input("Finally you see a house with three doors,which one do you choose?,R for red,Y for yellow,B for blue")
        if choice3=="Y":
            print("Yay!!!You open the door and find.................\n")
            print("A UNICORN!!!!\n")
            print(r'''
                             \
                              \
                               \\
                                \\
                                 >\/7
                             _.-(6'  \
                            (=___._/` \
                                 )  \ |
                                /   / |
                               /    > /
                              j    < _\
                          _.-' :      ``.
                          \ r=._\        `.
                         <`\\_  \         .`-.
                          \ r-7  `-. ._  ' .  `\
                           \`,      `-.`7  7)   )
                            \/         \|  \'  / `-._
                                       ||    .'
cjr                                     \\  (
10mar02                                  >\  >
                                     ,.-' >.'
                                    <.'_.''
                                      < 
                  *******************************************''')

            print("You get on it and ride fly away.\n")
            print("THE END")
        elif choice3=="R":
            print("You opened the door and get burned into crisp bY fire!\n")
            print("GAME OVER!")
        elif choice3=="B":
            print("You open the door and get eaten by a beast!")
            print("GAME OVER!")
        else:
            print("YOU CHOOSE WRONG!\n")
            print("YOU ARE ATTACKED BY A SWAMP OF BEES YOU DIE!")
            print("GAME OVER")

    elif choice2=="S":
        print("You are attacked by trouts!,you are dead.\n")
        print("GAME OVER!")
    else:
        print("You dare defy the choices provided!,You are struck by lightening!\n")
        print("YOU ARE DEAD\n")
        print("GAME OVER!")
elif choice1=="R":
    print("You fell into a hole and died.\n")
    print("GAME OVER!")
else:
    print("You choose the third option........that is DEATH!")
    print("GAME OVER!")
 