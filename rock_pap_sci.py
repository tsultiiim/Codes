import random
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("WELCOME TO THE GAME OF ROCK,PAPER AND SCISSORS")
choice=int(input("Enter 0 for rock,Enter 1 for paper,Enter 2 for scissors\n"))
signs=[rock,paper,scissors]
lol=random.randint(0,2)
comp_choice=signs[lol]
if choice==0:
    print("You chose rock\n")
    print(rock)
    if lol==1:
        print("Computer chose paper\n")
        print(paper)
        print("You loose!\n")
    elif lol==2:
        print("Computer chose scissors\n")
        print(scissors)
        print("You win!\n")
    elif lol==choice:
        print("Computer also chose rock")
        print("Draw!")
    else:
        print("Invalid\n")
if choice==1:
    print("You chose paper\n")
    print(paper)
    if lol==0:
        print("Computer chose rock\n")
        print(rock)
        print("You win!\n")
    elif lol==2:
        print("Computer chose scissors\n")
        print(scissors)
        print("You loose!\n")
    elif lol==choice:
        print("Computer also chose paper")
        print("Draw!")
    else:
        print("Invalid\n")
if choice==2:
    print("You chose scissors\n")
    print(scissors)
    if lol==0:
        print("Computer chose rock\n")
        print(rock)
        print("You loose!\n")
    elif lol==1:
        print("Computer chose paper\n")
        print(paper)
        print("You win!\n")
    elif lol==choice:
        print("Computer also chose scissors")
        print("Draw")
    else:
        print("Invalid\n")
