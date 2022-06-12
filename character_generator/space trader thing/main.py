import pandas as pd
#import worksheet
new_haven = ('NEW_HAVEN.ods')

#dataframe for inventory sheet
dfinventory = pd.read_excel(new_haven,sheet_name='Inventory')

#data frame for drug price sheet
dfdrug_pricing = pd.read_excel(new_haven,sheet_name='Drug Pricing')

#data frame for city state information and distance map
dfcityStateDistances = pd.read_excel(new_haven,sheet_name='City State Distances')#.to_string(index=False)
dfcity_States = pd.read_excel(new_haven,sheet_name='City States')

#data frame for characters
dfCharacters = pd.read_excel(new_haven,sheet_name='Character')

#creating the player character from the database
player_character = dfCharacters.loc[dfCharacters['Character']=='pc']
player = {
    'Name'  : player_character['Name'].to_string(index=False),#random values
    'Age'   : player_character['Age'].to_string(index=False),#random values
    'Gender': player_character['Gender'].to_string(index=False),#gender is in binary for later sorting
    'Credits': player_character['Credits'].to_string(index=False)#values added later
    }

#function to show distances from between different city states
def city_Distances_UI():
    #switching dataframe values to dictionary
    new_harbour_distance = dfcityStateDistances['New Harbour'].to_dict()
    new_tokyo_distance = dfcityStateDistances['New Tokyo'].to_dict()
    chicago_2_distance = dfcityStateDistances['Chicago-2'].to_dict()
    hanover_distance = dfcityStateDistances['Hanover'].to_dict()
    euphoria_distance = dfcityStateDistances['Euphoria'].to_dict()
    
    
    
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

    1 NEW HARBOUR > NEW TOKYO   5 NEW TOKYO > NEW HARBOUR   9  CHICAGO-2 > HANOVER        
    2 NEW HARBOUR > CHICAGO-2   6 NEW TOKYO > CHICAGO-2     10 CHICAGO-2 > EUPHORIA
    3 NEW HARBOUR > HANOVER     7 NEW TOKYO > HANOVER       11 CHICAGO-2 > NEW HARBOUR
    4 NEW HARBOUR > EUPHORIA    8 NEW TOKYO > EUPHORIA      12 CHICAGO-2 > NEW TOKYO 
                    
            13  HANOVER > EUPHORIA             17   EUPHORIA > NEW HARBOUR
            14  HANOVER > NEW HARBOUR          18   EUPHORIA > NEW TOKYO         
            15  HONOVER > NEW TOKYO            19   EUPHORIA > CHICAGO-2
            16  HANOVER > CHICAGO-2            20   EUPHORIA > HANOVER             

    >>>>>>>>>>>>>>>>>>>>>>please input number for information below>>>>>>>>>>>>>>>>>>>>>>>>>>>
    """)
    choice = int(choice)
    if choice == 1:
        print("NEW HARBOUR > NEW TOKYO: "+ str(new_harbour_distance[1])+"KM")
    elif choice == 2:
        print("NEW HARBOUR > CHICAGO-2: "+str(new_harbour_distance[2])+"KM")
    elif choice == 3:
        print("NEW HARBOUR > HANOVER: "+str(new_harbour_distance[3])+"KM")
    elif choice == 4:
        print("NEW HARBOUR > EUPHORIA: "+str(new_harbour_distance[4])+"KM")
    elif choice == 5:
        print("NEW TOKYO > NEW HARBOUR:"+str(new_tokyo_distance[0])+"KM")
    elif choice == 6:
        print("NEW TOKYO > CHICAGO-2: "+str(new_tokyo_distance[2])+"KM")
    elif choice == 7:
        print("NEW TOKYO > HANOVER: "+ str(new_tokyo_distance[3])+"KM")
    elif choice == 8:
        print("NEW TOKYO > EUPHORIA: "+str(new_tokyo_distance[4])+"KM")
    elif choice == 9:
        print("CHICAGO-2 > HANOVER: "+str(chicago_2_distance[0])+"KM")
    elif choice == 10:
        print("CHICAGO-2 > EUPHORIA: "+str(chicago_2_distance[1])+"KM")
    elif choice == 11:
        print("CHICAGO-2 > NEW HARBOUR: "+str(chicago_2_distance[3])+"KM")
    elif choice == 12:
        print("CHICAGO-2 > NEW TOKYO: "+str(chicago_2_distance[4])+"KM")
    elif choice == 13:
        print("HANOVER > EUPHORIA: "+str(hanover_distance[0])+"KM")
    elif choice == 14:
        print("HANOVER > NEW HARBOUR: "+str(hanover_distance[1])+"KM")
    elif choice == 15:
        print("HANOVER > NEW TOKYO: "+str(hanover_distance[2])+"KM")
    elif choice == 16:
        print("HANOVER > CHICAGO-2: "+str(hanover_distance[4])+"KM")
    elif choice == 17:
        print("EUPHORIA > NEW HARBOUR:"+str(euphoria_distance[0])+"KM")
    elif choice == 18:
        print("EUPHORIA > NEW HARBOUR: "+str(euphoria_distance[1]+"KM"))
    elif choice == 19:
        print("EUPHORIA > NEW HARBOUR: "+str(euphoria_distance[2])+"KM")
    elif choice == 20:
        print("EUPHORIA > NEW HARBOUR: "+str(euphoria_distance[3])+"KM")
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
    if "NEW HARBOUR" in current_location:#to simplify travel 
        choice = input("""
WELCOME TO THE NEW HARBOUR JUNCTION
SO TO WHERE SHALL IT BE?: 

1 NEW HARBOUR > NEW TOKYO       2 NEW HARBOUR > CHICAGO-2   
3 NEW HARBOUR > HANOVER         4 NEW HARBOUR > EUPHORIA

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>please choose the correct number below>>>>>>>>>>>>>>>>>>>>>>>
""")
    elif "NEW TOKYO" in current_location:#to simplify travel
        choice = input("""
WELCOME TO THE NEW TOKYO STATION
SO TO WHERE SHALL IT BE?: 

1 NEW TOKYO > NEW HARBOUR       2 NEW TOKYO > CHICAGO-2   
3 NEW TOKYO > HANOVER           4 NEW TOKYO > EUPHORIA

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>please choose the correct number below>>>>>>>>>>>>>>>>>>>>>>>
""")


#print(dfcityStateDistances.to_string(index=False))