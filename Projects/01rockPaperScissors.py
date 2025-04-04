import random as rand

rock = """
       ______      
_____'    ___)
        (_____)
        (_____)
         (____)
------.(_____)   
              
"""

paper = """
       _________
______'     ____)_____
                ______)
              __________)
            _________)
-------.________)  
"""

scissor = """
       _________
______'     ____)_____
                ______)
              __________)
            (___)
-------.____(___)  
"""

print("Rock, Paper, Scissor Game\n")
userChoice = int(input("Enter the choice: \n0 for Rock\n1for Paper and \n2 for Scissor\n\n"))
game_Option = [rock, paper, scissor]

if userChoice >= 0 and userChoice <= 2:
    print("Your choice\n")
    print(game_Option[userChoice] , "\n\n")

    computerChoice = int(rand.randint(0,2))
    print("Computer's choice: ")
    print(game_Option[computerChoice])

    if(userChoice == 0 and computerChoice == 2):
        print("You win")
    elif(userChoice == 2 and computerChoice == 0):
        print("You lose")
    elif(userChoice > computerChoice):
        print("You win!")
    elif(userChoice < computerChoice):
        print("You Lose")
    elif(userChoice == computerChoice):
        print("Draw Match")


