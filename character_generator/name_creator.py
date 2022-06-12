import pandas as pd, random
#import csv and converts it to dataframe
df = pd.read_csv('names.csv')
#create lists to serepate csv columns
list_male = df['MALE'].tolist() 
list_female = df['FEMALE'].tolist()
surname_list = df['SURNAMES'].tolist()

#func to assign male names
def male_name():
    x = random.randrange(1,6288)
    name = list_male[x]
    x = random.randrange(1,len(surname_list))
    surname = surname_list[x]
    male_name = str(name) + ' ' + str(surname)
    return male_name
#func to assisgn female names
def female_name():
    x = random.randrange(1,4391)
    name = list_female[x]
    x = random.randrange(1,len(surname_list))
    surname = surname_list[x]
    female_name = str(name) + ' ' + str(surname)
    return female_name  

print("""
      ###############################
      ^  Welcome To Personify       ^
      ^  This  is basic             ^
      ^  random name generator      ^
      ^  author : gareth pretorius  ^
      ###############################""")
amount = input("How Many Names to Generate?: ")#add catch here for incorrect input
choices = input("Generate [M]ale, [F]emale, or Mi[x]ed?: ")

if  choices in ["M","m","Male","male","MALE"]:
    amount = int(amount)
    x = 1 
    while x <= amount:
        print("Number :"+str(x)+" "+male_name())
        x+=1
elif choices in ["F","f","female","Female","FEMALE"] :
    amount = int(amount)
    x = 0 
    while x <= amount:
        print("Number :"+str(x)+" "+female_name())
        x+=1
elif choices in ["X","x","mix","mixed","Mix","Mixed","MIXED","MIX"] :
    amount = int(amount)
    x = 0 
    while x <= amount:
        y = random.randint(0,1)
        if y == 1:
            print("Number :"+str(x)+" "+male_name())
            x+=1
        elif y == 0:
            print("Number :"+str(x)+" "+female_name())
            x += 1
else:
    print("Incorrect Input. Please Retry...")
quit()