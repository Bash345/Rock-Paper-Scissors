from random import randint

t = ["Rock", "Paper", "Scissors"]
comp = t[randint(0,2)]
player = False

while player == False:
    
    player = input("Rock, Paper, Scissors?")
    if player == comp:
        print("Tie!, go again")
    elif player == "Rock":
        if comp == "Paper":
            print("You lose", comp, "wraps", player)
        else:
            print("You win!", player, "smashes", comp)
    elif player == "Paper":
        if comp == "Scissors":
            print("You Lose", comp, "cuts", player)
        else:
            print("You Win", player, "wraps", comp)
    elif player == "Scissors":
        if comp == "Paper":
            print("You Win", player, "cuts", comp)
        else:
            print("You Lose", comp, "smashes", player)
    else:
        print("Are you stupid fam, do you know how to play the game")

