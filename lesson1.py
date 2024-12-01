import random

def get_choices():

    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper, scissors) : ")
    computer_choice = random.choice(options)

    choices = { "player": player_choice, "computer": computer_choice }
    
    return choices

def check_win(player, computer):
    print(f"You chose \"{player}\" and computer chose \"{computer}\".")
    # Tie Case
    if player == computer:
        return "It's a tie"
    # Case 1: Player choses "rock"
    elif player == "rock":
        if computer == "scissors": 
            return "rock smashes scissors. You win!"
        else:
            return "paper covers rock. You loose :("
    # Case 2: Player choses "scissors"
    elif player == "scissors":
        if computer == "rock":
            return "rock smashes scissors. You loose :("
        else:
            return "scissors cut paper. You win!"
    # Case 3:  Player choses "paper"
    elif player == "paper":
        if computer == "rock":
            return "paper covers rock. You win!"
        else: 
            return "scissors cut paper. You loose :("
    # Undefined Case: Error
    else:
        return "You must choose between rock, paper and scissors. Check the speeling"
    
    
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)