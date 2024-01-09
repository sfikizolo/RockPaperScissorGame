import random

print("You have 3 choices: Rock (r), Paper (p), or Scissors (s)"+"\n"+"LET'S PLAY!!!!!!!!!"+"\n")
userInput = input("Rock , Paper ,Scissor?"+"\n").lower()


while userInput not in ['r', 'p', 's']:
        print("Invalid choice , please enter a valid choice!")
        userInput = input("Rock , Paper ,Scissor?"+"\n").lower()

compArray= ["r","p","s"]

comp_mapping = {"r": "Rock", "p": "Paper", "s": "Scissors"}

compChoice = random.choice(compArray)

if (userInput == compChoice):
    result = "It's a draw"
elif (compChoice=="s" and userInput=="r") or (compChoice=="r" and userInput=="p") or  (compChoice=="p" and userInput=="s"):
    result = "You win!"
else :
    result = "The computer wins!"

print(f"The computer choice is {comp_mapping[compChoice]}"+"\n\n"+f"Your choice is {comp_mapping[userInput]}" +"\n\n"+result+"\n")