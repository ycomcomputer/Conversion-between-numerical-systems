# File: CS112_A1_T2_2_20230508.py
# Purpose: There is a list of numbers from 1 to 9, and each player takes it in turn to choose a number, and this number cann't be chosen again. If a player picks numbers that add up to 15, he wins, and if no player gets numbers that add up to 15, it's a draw.
# Author: Youssef Mohamed Salah
# ID: 20230508

#the next function checks if there are 3 numbers whose sum equals 15
def check_result(player):
    for num1 in range(len(player)):
        for num2 in range(num1+1, len(player)):
             for num3 in range (num2+1,len(player)):
                  if player[num1]+player[num2]+player[num3]==15:
                       return True
    return False

#The next line welcomes the user
print("Welcome to Number scrabble Game")

#the next function explain the game
def game():
#The next The next line stores the choices in a list called number_set 
    number_set=[1,2,3,4,5,6,7,8,9]
    player_one=[]
    player_two=[]

#The next line explains that if the number of elements in the list is greater than one and do the following
    while len(number_set)>1:
#The next line print that it is the first player's turn
        print("Number One Turn")
        print("Choose a Number From: ",number_set)
        while True:
#The next line take input from player one and stores his choices in varible player1_choice
            player1_choice= int(input(f"Player One Choose a Number From: {number_set} : "))
#The following lines set a condition as to whether the player's choice is among the correct choices or not
            if  player1_choice in number_set:
#If the condition is true the next line deletes the selection from number_set to prevent it from being selected again
                number_set.remove(player1_choice)
#and then add this choice to player_one
                player_one.append(player1_choice)
                break
#if the condition is false print to the user message to enter valid choice and Then the player returns to choose again
            else:
             print("Enter Valid Value From: ",number_set)
            continue
#the next line check if the user wins or no if he wins print the message player one wins
        if check_result(player_one):
            print("Player One Wins")
            print("End the Game")
            return
    
#The next line print that it is the second player's turn
        print("Number Two Turn")
#the next line print the choices
        print("Choose a Number From: ",number_set)
        while True:
#The next line take input from player one and stores his choices in varible player2_choice
            player2_choice=int(input(f"Player One Choose a Number From: {number_set} : "))
#The following lines set a condition as to whether the player's choice is among the correct choices or not
            if player2_choice in number_set:
#If the condition is true the next line deletes the selection from number_set to prevent it from being selected again
              number_set.remove(player2_choice)
#and then add this choice to player_two
              player_two.append(player2_choice)
              break
#if the condition is false print to the user message to enter valid choice and Then the player returns to choose again
            else:
              print("Enter Valid Value From: ",number_set)
              continue
#the next line check if the user wins or no if he wins print the message player two wins
        if check_result(player_two):
            print("Player Two Wins")
            print("End the Game")
            return
#and the next line if no players win print the game is draw
    print("The Game is Draw")
    print("End the Game")
game()


    


    
