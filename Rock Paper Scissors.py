import random
yourCount = 0
computerCount = 0
while True:
    userin = input("Rock, paper or scissors? ").upper()
    randNum = random.randint(0,2)   #to generate computer's play
    myList = ["ROCK", "PAPER", "SCISSORS"]
    if userin == "ROCK":
        uservalue = 0
    elif userin == "PAPER":
        uservalue = 1
    elif userin == "SCISSORS":
        uservalue = 2
    else:
        print("Please enter a valid input.")
        continue

    if (uservalue - randNum) == 1 or (uservalue - randNum) == -2:
        print("Computer played " + myList[randNum] + ", YOU WIN!")
        yourCount += 1
    if (uservalue - randNum) == -1 or (uservalue - randNum) == 2:
        print("Computer played " + myList[randNum] + ", YOU LOSE!")
        computerCount += 1
    if uservalue == randNum:
        print("Computer played " + myList[randNum] + ", it's a draw.")
    print("Your score: " + str(yourCount) + " Computer's score: " + str(computerCount))






