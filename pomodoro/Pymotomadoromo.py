#pomodoro
import os,time,random

#main funcion
def pomodoro():
    print("""   

🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅
🍅 This is A Simple Python Pomodoro 🍅
🍅     called  Pymotomadoromo       🍅
🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅
    author  :   gareth pretorius
""")
    
    #Function to name Task or activity
    def task_name():
        task_name = input("     Set Pomodoro|Timer For: ")
        return task_name
    taskname=task_name()

    #function for user choice so that they can customize the minutes or seconds 
    def user_values():
        minute = int(input("        Amount of Minutes: "))
        second = int(input("        Amount of Seconds: "))
        if second == 0:
            second = 60
        while minute != 0:
            second -= 1
            os.system("clear")
            os.system("date")
            # loop to keep seconds double digits
            if second < 10:
                print("🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅")
                print("🍅Task: "+ taskname)
                print("\nTime Remaining: "+str(minute)+":"+'0'+ str(second)+"🍅")
                time.sleep(1)
            #main loop
            elif second > 10:
                print("🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅")
                print("🍅Task: "+ taskname)
                print("🍅\n🍅Time Remaining: "+str(minute)+":"+ str(second)+"            🍅")
                print("🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅")
                time.sleep(1)    
            #loop to reset the second counter    
            if second == 0:
                minute-=1
                print("🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅")
                print("\n"+taskname+"\nTime Remaining: "+str(minute)+":"+ str(second))
                second = 60
                pomodoro()
    
    #to get user input
    choice = input("        (s)tart|||(c)hange values\n")
    
    #user choice pomodoro
    if choice in ["c","C","Change","CHANGE","change"]:
        user_values()

    #default values pomodoro main func
    elif choice in["s","S","start","Start","START"]:
        minute = 45
        second = 60
        while minute != 0:
            second -= 1
            os.system("clear")
            os.system("date")
            if second < 10:
                print("🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅")
                print("🍅Task: "+ taskname)
                print("\nTime Remaining: "+str(minute)+":"+'0'+ str(second)+"🍅")
                time.sleep(1)
            elif second > 10:
                print("🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅")
                print("🍅Task: "+ taskname)
                print("🍅\n🍅Time Remaining: "+str(minute)+":"+ str(second)+"            🍅")
                print("🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅")
                time.sleep(1)    
            if second == 0:
                minute-=1
                print("🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅")
                print("\n"+taskname+"\nTime Remaining: "+str(minute)+":"+ str(second))
                second = 60
                pomodoro()
pomodoro()