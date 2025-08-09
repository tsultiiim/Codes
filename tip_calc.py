print("Welcome to the tip calculator!")
bill = float(input("What was the Total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n "))
pay= (((tip/100)*bill)+bill)/people
print(f"Each person should pay : ${pay}")
