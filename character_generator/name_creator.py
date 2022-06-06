import pandas as pd, random
#import csv and converts it to dataframe
df = pd.read_csv('/names.csv')
#create lists to serepate csv columns
list_male = df['MALE'].tolist() 
list_female = df['FEMALE'].tolist()
surname_list = df['SURNAMES'].tolist()

#func to assign male names
def male_name():
    x = random.randint(1,6288)
    name = list_male[x]
    x = random.randint(1,10443)
    surname = surname_list[x]
    male_name = name + ' ' + surname
    return male_name
#func to assisgn female names
def female_name():
    x = random.randint(1,4391)
    name = list_female[x]
    x = random.randint(1,10443)
    surname = surname_list[x]
    female_name = name + ' ' + surname
    return female_name  
