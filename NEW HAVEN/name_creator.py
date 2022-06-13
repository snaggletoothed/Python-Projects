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