import pandas as pd, name_creator as create,random


#import worksheet
new_haven = ('NEW_HAVEN.xlsx')

#dataframe for inventory sheet
dfinventory = pd.read_excel(new_haven,sheet_name='Inventory')

#data frame for drug price sheet
dfdrug_pricing = pd.read_excel(new_haven,sheet_name='Drug_Pricing')

#data frame for city state information and distance map
dfcityStateDistances = pd.read_excel(new_haven,sheet_name='City_State_Distances')#.to_string(index=False)
dfcity_States = pd.read_excel(new_haven,sheet_name='City_States')

#data frame for characters
dfCharacters = pd.read_excel(new_haven,sheet_name='Character')

###keep for possible save game function
#creating the player character from the database
#player_character = dfCharacters.loc[dfCharacters['CHARACTER']=='PC']
#player = {
#    'Name'  : player_character['NAME'].to_string(index=False),#random values
#    'Age'   : player_character['AGE'].to_string(index=False),#random values
#    'Gender': player_character['GENDER'].to_string(index=False),#gender is in binary for later sorting
#    'Credits': player_character['CREDITS'].to_string(index=False)#values added later
#    }

#function to generate a name for thhhhhe player character
def citizenryifier():
        #function to be used in text to generate possitve affirmations***pointless function really
    def positive_affirmations():
        affirmationsList = ['Excellent ', 'Glorious ', "You'd make your{INSERT PARENTAL/GUARDIAN} proud with this ","Great "]
        x = random.randint(0,3)
        if x == 0:
            affirmation = affirmationsList[x]
        elif x == 1 :
            affirmation = affirmationsList[x]
        elif x == 2 :
            affirmation = affirmationsList[x]
        elif x == 3 :
            affirmation = affirmationsList[x]
        return affirmation

    choice = input("""

                                                                                               
 ███╗   ██╗███████╗██╗    ██╗    ██╗  ██╗ █████╗ ██╗   ██╗███████╗███╗   ██╗                     
████╗  ██║██╔════╝██║    ██║    ██║  ██║██╔══██╗██║   ██║██╔════╝████╗  ██║                     
██╔██╗ ██║█████╗  ██║ █╗ ██║    ███████║███████║██║   ██║█████╗  ██╔██╗ ██║                     
██║╚██╗██║██╔══╝  ██║███╗██║    ██╔══██║██╔══██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║                     
██║ ╚████║███████╗╚███╔███╔╝    ██║  ██║██║  ██║ ╚████╔╝ ███████╗██║ ╚████║                     
╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝     ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝     

                
 ██████╗██╗████████╗██╗███████╗███████╗███╗   ██╗██████╗ ██╗   ██╗██╗███████╗██╗███████╗██████╗ 
██╔════╝██║╚══██╔══╝██║╚══███╔╝██╔════╝████╗  ██║██╔══██╗╚██╗ ██╔╝██║██╔════╝██║██╔════╝██╔══██╗
██║     ██║   ██║   ██║  ███╔╝ █████╗  ██╔██╗ ██║██████╔╝ ╚████╔╝ ██║█████╗  ██║█████╗  ██████╔╝
██║     ██║   ██║   ██║ ███╔╝  ██╔══╝  ██║╚██╗██║██╔══██╗  ╚██╔╝  ██║██╔══╝  ██║██╔══╝  ██╔══██╗
╚██████╗██║   ██║   ██║███████╗███████╗██║ ╚████║██║  ██║   ██║   ██║██║     ██║███████╗██║  ██║
 ╚═════╝╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
-BROUGHT TO YOU BY 
            THE NEW HAVEN
                AMALGAMATED
                    CITY WATHCMEN                                                                                                                 

G'day, I believe a happy birthday is in order as you are now old enough for a name!
Also you get to recieve a Citizenship to one of the 5 City States!
All you need is a [NAME] and to pass a simple test
GOOD LUCK YOU, YOU!*



Now, then
Would you like a name generated or would you like to choose your own?




INFORMATION FOOTNOTE:
Due to technical constraints
you only get the [1] chance 
OR ELSE
this session must be terminated

>>>>>>>>>please use the correct character below : [G]enerate|||[C]hoose>>>>>>\n""")
    if choice in ['G','g']:
        def name_maker():    
            choice = input("""
    Now, would it be [M]ale or [F]emale?
                        
>>>>>>>><<<<<please choose the correct input below  : [M]ale|||[F]emale>>>>>>>>>\n""")
            if choice in ['M','m']:
                name = create.male_name()
                print(positive_affirmations()+"this choicely name of: "+name)
                print("""
Do you like this name? If not it's the "or else" option...
>>>>>>>>>>>>>>>>>>>>>>>>nothing to see here<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""")
                return name
            elif choice in ['F','f']:
                name = create.female_name()
                print(positive_affirmations()+"this choicely name of: "+name)
                print("""
Do you like this name? If not it's the "or else" option...
>>>>>>>>>>>>>>>>>>>>>>>>nothing to see here<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""")                
                return name
            else:
                print("INCORRECT INPUT. TERMINATING")
    else:
            print("INCORRECT INPUT. TERMINATING")
    name = name_maker()
    return name

def character_builder():
    pass

#function to show distances from between different city states
def city_Distances_UI():
    #switching dataframe values to dictionary
    reykjavik_distance = dfcityStateDistances['REYKJAVÍK'].to_dict()
    new_shinjuku_distance = dfcityStateDistances['NEW SHINJUKU'].to_dict()
    chicago_2_distance = dfcityStateDistances['CHICAGO-2'].to_dict()
    hanoi_distance = dfcityStateDistances['HANOI'].to_dict()
    euphoria_distance = dfcityStateDistances['EUPHORIA'].to_dict()
    
    
    
    choice = input("""
##    ## ######## ##      ##    ##     ##    ###    ##     ## ######## ##    ##        
###   ## ##       ##  ##  ##    ##     ##   ## ##   ##     ## ##       ###   ##        
####  ## ##       ##  ##  ##    ##     ##  ##   ##  ##     ## ##       ####  ##        
## ## ## ######   ##  ##  ##    ######### ##     ## ##     ## ######   ## ## ##        
##  #### ##       ##  ##  ##    ##     ## #########  ##   ##  ##       ##  ####        
##   ### ##       ##  ##  ##    ##     ## ##     ##   ## ##   ##       ##   ###        
##    ## ########  ###  ###     ##     ## ##     ##    ###    ######## ##    ##      

 
 
 ######  #### ######## ##    ##     ######  ########    ###    ######## ########       
##    ##  ##     ##     ##  ##     ##    ##    ##      ## ##      ##    ##             
##        ##     ##      ####      ##          ##     ##   ##     ##    ##             
##        ##     ##       ##        ######     ##    ##     ##    ##    ######         
##        ##     ##       ##             ##    ##    #########    ##    ##             
##    ##  ##     ##       ##       ##    ##    ##    ##     ##    ##    ##             
 ######  ####    ##       ##        ######     ##    ##     ##    ##    ########       
 
 
 
########  ####  ######  ########    ###    ##    ##  ######  ########  ######          
##     ##  ##  ##    ##    ##      ## ##   ###   ## ##    ## ##       ##    ##         
##     ##  ##  ##          ##     ##   ##  ####  ## ##       ##       ##               
##     ##  ##   ######     ##    ##     ## ## ## ## ##       ######    ######          
##     ##  ##        ##    ##    ######### ##  #### ##       ##             ##         
##     ##  ##  ##    ##    ##    ##     ## ##   ### ##    ## ##       ##    ##         
########  ####  ######     ##    ##     ## ##    ##  ######  ########  ######       
-BROUGHT TO YOU BY 
            THE BROTHERHOOD FOR UNITED MEASUREMENTS
    
    DISTANCE FROM AND TO:

    1 REYKJAVÍK > NEW SHINJUKU   5 NEW SHINJUKU > REYKJAVÍK   9  CHICAGO-2 > HANOI        
    2 REYKJAVÍK > CHICAGO-2   6 NEW SHINJUKU > CHICAGO-2     10 CHICAGO-2 > EUPHORIA
    3 REYKJAVÍK > HANOI     7 NEW SHINJUKU > HANOI       11 CHICAGO-2 > REYKJAVÍK
    4 REYKJAVÍK > EUPHORIA    8 NEW SHINJUKU > EUPHORIA      12 CHICAGO-2 > NEW SHINJUKU 
                    
            13  HANOI > EUPHORIA             17   EUPHORIA > REYKJAVÍK
            14  HANOI > REYKJAVÍK          18   EUPHORIA > NEW SHINJUKU         
            15  HONOVER > NEW SHINJUKU            19   EUPHORIA > CHICAGO-2
            16  HANOI > CHICAGO-2            20   EUPHORIA > HANOI             

    >>>>>>>>>>>>>>>>>>>>>>please input number for information below>>>>>>>>>>>>>>>>>>>>>>>>>>>
    """)
    choice = int(choice)
    if choice == 1:
        print("REYKJAVÍK > NEW SHINJUKU: "+ str(reykjavik_distance[1])+"KM")
    elif choice == 2:
        print("REYKJAVÍK > CHICAGO-2: "+str(reykjavik_distance[2])+"KM")
    elif choice == 3:
        print("REYKJAVÍK > HANOI: "+str(reykjavik_distance[3])+"KM")
    elif choice == 4:
        print("REYKJAVÍK > EUPHORIA: "+str(reykjavik_distance[4])+"KM")
    elif choice == 5:
        print("NEW SHINJUKU > REYKJAVÍK:"+str(new_shinjuku_distance[0])+"KM")
    elif choice == 6:
        print("NEW SHINJUKU > CHICAGO-2: "+str(new_shinjuku_distance[2])+"KM")
    elif choice == 7:
        print("NEW SHINJUKU > HANOI: "+ str(new_shinjuku_distance[3])+"KM")
    elif choice == 8:
        print("NEW SHINJUKU > EUPHORIA: "+str(new_shinjuku_distance[4])+"KM")
    elif choice == 9:
        print("CHICAGO-2 > HANOI: "+str(chicago_2_distance[0])+"KM")
    elif choice == 10:
        print("CHICAGO-2 > EUPHORIA: "+str(chicago_2_distance[1])+"KM")
    elif choice == 11:
        print("CHICAGO-2 > REYKJAVÍK: "+str(chicago_2_distance[3])+"KM")
    elif choice == 12:
        print("CHICAGO-2 > NEW SHINJUKU: "+str(chicago_2_distance[4])+"KM")
    elif choice == 13:
        print("HANOI > EUPHORIA: "+str(hanoi_distance [0])+"KM")
    elif choice == 14:
        print("HANOI > REYKJAVÍK: "+str(hanoi_distance [1])+"KM")
    elif choice == 15:
        print("HANOI > NEW SHINJUKU: "+str(hanoi_distance [2])+"KM")
    elif choice == 16:
        print("HANOI > CHICAGO-2: "+str(hanoi_distance [4])+"KM")
    elif choice == 17:
        print("EUPHORIA > REYKJAVÍK:"+str(euphoria_distance[0])+"KM")
    elif choice == 18:
        print("EUPHORIA > REYKJAVÍK: "+str(euphoria_distance[1]+"KM"))
    elif choice == 19:
        print("EUPHORIA > REYKJAVÍK: "+str(euphoria_distance[2])+"KM")
    elif choice == 20:
        print("EUPHORIA > REYKJAVÍK: "+str(euphoria_distance[3])+"KM")
    else:
        print("incorrect choice made, resetting...")
        city_Distances_UI()
#function to travel between different transport depots   
def public_Transport(current_location):
    current_location = current_location 
    print("""
##::: ##:'########:'##:::::'##::::'##::::'##::::'###::::'##::::'##:'########:'##::: ##::::::::         
###:: ##: ##.....:: ##:'##: ##:::: ##:::: ##:::'## ##::: ##:::: ##: ##.....:: ###:: ##::::::::         
####: ##: ##::::::: ##: ##: ##:::: ##:::: ##::'##:. ##:: ##:::: ##: ##::::::: ####: ##::::::::         
## ## ##: ######::: ##: ##: ##:::: #########:'##:::. ##: ##:::: ##: ######::: ## ## ##::::::::         
##. ####: ##...:::: ##: ##: ##:::: ##.... ##: #########:. ##:: ##:: ##...:::: ##. ####::::::::         
##:. ###: ##::::::: ##: ##: ##:::: ##:::: ##: ##.... ##::. ## ##::: ##::::::: ##:. ###::::::::         
##::. ##: ########:. ###. ###::::: ##:::: ##: ##:::: ##:::. ###:::: ########: ##::. ##::::::::         
.::::..::........:::...::...::::::..:::::..::..:::::..:::::...:::::........::..::::..:::::::::         
########::'##::::'##:'########::'##:::::::'####::'######::::::::::::::::::::::::::::::::::::::                                     
##.... ##: ##:::: ##: ##.... ##: ##:::::::. ##::'##... ##:::::::::::::::::::::::::::::::::::::                                     
##:::: ##: ##:::: ##: ##:::: ##: ##:::::::: ##:: ##:::..::::::::::::::::::::::::::::::::::::::                                     
########:: ##:::: ##: ########:: ##:::::::: ##:: ##:::::::::::::::::::::::::::::::::::::::::::                                     
##.....::: ##:::: ##: ##.... ##: ##:::::::: ##:: ##:::::::::::::::::::::::::::::::::::::::::::                                     
##:::::::: ##:::: ##: ##:::: ##: ##:::::::: ##:: ##::: ##:::::::::::::::::::::::::::::::::::::                                     
##::::::::. #######:: ########:: ########:'####:. ######::::::::::::::::::::::::::::::::::::::                                     
.::::::::::.......:::........:::........::....:::......:::::::::::::::::::::::::::::::::::::::                                     
########:'########:::::'###::::'##::: ##::'######::'########:::'#######::'########::'########: 
.. ##..:: ##.... ##:::'## ##::: ###:: ##:'##... ##: ##.... ##:'##.... ##: ##.... ##:... ##..:: 
:: ##:::: ##:::: ##::'##:. ##:: ####: ##: ##:::..:: ##:::: ##: ##:::: ##: ##:::: ##:::: ##:::: 
:: ##:::: ########::'##:::. ##: ## ## ##:. ######:: ########:: ##:::: ##: ########::::: ##:::: 
:: ##:::: ##.. ##::: #########: ##. ####::..... ##: ##.....::: ##:::: ##: ##.. ##:::::: ##:::: 
:: ##:::: ##::. ##:: ##.... ##: ##:. ###:'##::: ##: ##:::::::: ##:::: ##: ##::. ##::::: ##:::: 
:: ##:::: ##:::. ##: ##:::: ##: ##::. ##:. ######:: ##::::::::. #######:: ##:::. ##:::: ##:::: 
::..:::::..:::::..::..:::::..::..::::..:::......:::..::::::::::.......:::..:::::..:::::..::::: 
::::::::::::::::::::::::::::::::::::::::::::::'##::::'##:'##::: ##:'####::'#######::'##::: ##:
:::::::::::::::::::::::::::::::::::::::::::::: ##:::: ##: ###:: ##:. ##::'##.... ##: ###:: ##:
:::::::::::::::::::::::::::::::::::::::::::::: ##:::: ##: ####: ##:: ##:: ##:::: ##: ####: ##:
:::::::::::::::::::::::::::::::::::::::::::::: ##:::: ##: ## ## ##:: ##:: ##:::: ##: ## ## ##:
:::::::::::::::::::::::::::::::::::::::::::::: ##:::: ##: ##. ####:: ##:: ##:::: ##: ##. ####:
:::::::::::::::::::::::::::::::::::::::::::::: ##:::: ##: ##:. ###:: ##:: ##:::: ##: ##:. ###:
::::::::::::::::::::::::::::::::::::::::::::::. #######:: ##::. ##:'####:. #######:: ##::. ##:
:::::::::::::::::::::::::::::::::::::::::::::::.......:::..::::..::....:::.......:::..::::..::                       
-BROUGHT TO YOU BY 
                THE NEW HAVEN 
                PUBLIC TRANSPORT
                    UNION                       

WELCOME TRAVELER!
OURS IS A PRIVATE NON ALIGNED TRANSPORTATION SERVICE RUNNING DAILY TO AND FROM THE MAJOR CITY STATES!!!
THERE'S NO BETTER FARE THAN HERE!""")
    if "REYKJAVÍK" in current_location:#to simplify travel 
        choice = input("""
WELCOME TO THE REYKJAVÍK JUNCTION
SO TO WHERE SHALL IT BE?: 

1 REYKJAVÍK > NEW SHINJUKU       2 REYKJAVÍK > CHICAGO-2   
3 REYKJAVÍK > HANOI         4 REYKJAVÍK > EUPHORIA

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>please choose the correct number below>>>>>>>>>>>>>>>>>>>>>>>
""")
    elif "NEW SHINJUKU" in current_location:#to simplify travel
        choice = input("""
WELCOME TO THE NEW SHINJUKU STATION
SO TO WHERE SHALL IT BE?: 

1 NEW SHINJUKU > REYKJAVÍK       2 NEW SHINJUKU > CHICAGO-2   
3 NEW SHINJUKU > HANOI           4 NEW SHINJUKU > EUPHORIA

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>please choose the correct number below>>>>>>>>>>>>>>>>>>>>>>>
""")


