import random
yourCount, computerCount = 0, 0
print("ROCK PAPER SCISSORS!")
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
    elif userin == "END":
        print("GAME OVER.")
        break
    else:
        print("Please enter a valid input. END to stop the game.")
        continue
    #3 cases exist given that input is valid:
    if (uservalue - randNum) == 1 or (uservalue - randNum) == -2:
        print("Computer played " + myList[randNum] + ", YOU WIN!")
        yourCount += 1
    if (uservalue - randNum) == -1 or (uservalue - randNum) == 2:
        print("Computer played " + myList[randNum] + ", YOU LOSE!")
        computerCount += 1
    if uservalue == randNum:
        print("Computer played " + myList[randNum] + ", it's a draw.")
    print("Your score: " + str(yourCount) + " Computer's score: " + str(computerCount))







