import random,os
from time import sleep
date = os.system('date')
def text_float():
    os.system("clear")
    print("--------------------------------")
    print("Welcome To Rock Paper Scissors")
    print("author   :   gareth pretorius")
    print("--------------------------------")
    os.system('date')
    print("--------------------------------")
text_float()
def Start():
    player_Name = input("\bHello,\nWhat is your Name: \n")
    os.system("clear")
    highscore = {}
    text_float()
    rounds = int(input("\nHello, "+player_Name+"\nHow Many Rounds?:\n⮕ ⮕ ⮕ "))
    os.system("clear")
    win=0
    lose=0
    draw=0
    matches = 0
    x=3
    while x!=0:
        text_float()
        print("Starting in : "+str(x)+"...")
        x-=1
        sleep(1) 
        os.system("clear")
    while rounds != 0:
        choices={
            1:"ROCK",
            2:"PAPER",
            3:"SCISSOR"
        }
        text_float()
        player_choice = input("ROCK,PAPER,SCISSOR!\n⮕ ⮕ ⮕ ")
        opponent_choice = choices[random.randint(1,3)]

        if player_choice in ['ROCK','Rock','rock','r','R']:
            player_choice = choices[1]
                
        if player_choice in ['PAPER','Paper','paper','p','P']:
            player_choice = choices[2]


        if player_choice in ['SCISSOR','Scissor','scissor','s','S']:
            player_choice = choices[3]

        if player_choice == opponent_choice:
            print(player_choice+" : "+opponent_choice+ " = TIE")
            draw +=1
            
        elif player_choice == "ROCK" and opponent_choice == "PAPER" or player_choice == "PAPER" and opponent_choice == "SCISSOR" or player_choice == "SCISSOR" and opponent_choice == "ROCK":
            print(player_choice+" : "+opponent_choice+ " = LOST")
            lose+=1

        elif player_choice == "PAPER" and opponent_choice == "ROCK" or player_choice == "SCISSOR" and opponent_choice == "PAPER" or player_choice == "ROCK" and opponent_choice == "SCISSOR":
            print(player_choice+" : "+opponent_choice+ " = WIN")
            win+=1
        else:
            print("Wrong Input, Program Quitting")
            quit()
        results ={
            'Wins':win,
            'Losses':lose,
            'Draws':draw

        }
        rounds-=1
        matches +=1
        print("Rounds Left: "+str(rounds)+"\n"+str(results).replace("{'","").replace("'","").replace("}",""))
        sleep(1)
        os.system("clear")
        highscore ={
            'Date' : date,
            'Name' : player_Name,
            'Wins' : win,
            'Losses': lose,
            'Draws': draw,
            'Rounds': matches
        }
        print("HIGHSCORE: "+str(highscore).replace("{'","").replace("'","").replace("}",""))
    choice=input("Try Again?:\n")
    
    
    if choice in ["yes","Yes","YES","y","Y"]:
        sleep(1)
        os.system("clear")
        Start()
    elif choice in ["NO","no","No","n","N","Q","q","Quit","quit","QUIT"]:
        os.system("clear")
        print("Shutting Down")
        sleep(1)
        quit()

Start()
            
