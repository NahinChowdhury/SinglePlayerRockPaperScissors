# Single Player Rock,Paper, Scissor

import random

def introduction():
    
    print("Welcome to the game of Rock,Paper and Scissors.")
    print("Rules:")
    print("You can only choose Rock, Paper or Scissors.")  
    
def playerInputValidity(number):
    playerChoice = ''
    
    while playerChoice not in ["rock", "paper","scissors"]:
        playerChoice = input("Player "+ str(number) +" chooses: ").lower().strip()
    
    return playerChoice

def botChoice():
    randomChoice = random.randint(0,2)
    choiceList = ["rock", "paper","scissors"]
    
    return choiceList[randomChoice]

def botChoiceOutput(botChoices):
    print("Computer Robot chooses: "+ botChoices)

def winner(playerOneChoice,botChoice):
    # if player one 
    precedence = ["rock", "paper","scissors"]
    
    # if player1 == pred[smth] and player2 == pred[smth - 1]
    # player 1 wins
    # if player1 ==pred[smth] and player 2 == pred[smth - 2]
    # player 2 wins
    
    playerOnePos = precedence.index(playerOneChoice)
    # if player1 chooses smth and player2 chooses something weaker than him
    if playerOneChoice == precedence[playerOnePos] and botChoice == precedence[playerOnePos]:
        return 0
    
    elif playerOneChoice == precedence[playerOnePos] and botChoice == precedence[playerOnePos - 1]:
        return 1
    
    else:
        return 2    
    
def scores(playerOneWins,botWins):
    
    print("")
    print("Scores so far:")
    print("You: "+ str(playerOneWins))
    print("Computer Robot: "+ str(botWins))
    print("")
        
def winnerAnnouncement(playerOneWins):
    
    if playerOneWins >= 3:
        print("Player One Wins!")
    else:
        print("Computer Robot Wins!")    

def gameEndingLines():
    
    print("Game Over! Thank you for playing.")    

def main():
    
    introduction()
    
    turns = int(input("Please enter best of how many rounds you'll like to play: ").lower().strip())
    
    playerOneWins = 0
    botWins = 0
    
    while(playerOneWins < turns and botWins < turns):
        playerOneChoice = playerInputValidity(1)
        botChoices = botChoice()
        botChoiceOutput(botChoices)
        
        result = winner(playerOneChoice,botChoices)
    
        if result == 0:
            pass
        elif result == 1:
            playerOneWins += 1
        else:
            botWins += 1 
        
        scores(playerOneWins,botWins)

    winnerAnnouncement(playerOneWins)

    gameEndingLines()

main()