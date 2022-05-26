import random,os,time
def logo():
    os.system("clear")

    print("""=--------------------------------------------=      
=   Welcome to a  Basic Password Generator   =
=       author - gareth pretorius            =
=--------------------------------------------=      
      """)
    time.sleep(1)    
logo()
alphabet = {
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',
    7:'E',
    8:'F',
    9:'H',
    10:'I',
    11:'J',
    12:'K',
    13:'L',
    14:'M',
    15:'N',
    16:'O',
    17:'P',
    18:'Q',
    19:'R',
    20:'S',
    21:'T',
    22:'U',
    23:'V',
    24:'W',
    25:'X',
    26:'Y',
    27:'Z'   
}
symbols={
    0:'!',
    1:'@',
    2:'#',
    3:'$',
    4:'%',
    5:'^',
    6:'&',
    7:'*',
    8:'(',
    9:')',
}
words={
    1:'ocelot',
    2:'teseract',
    3:'orange',
    4:'horse',
    5:'panda',
    6:'fox',
    7:'helicopter',
    8:'battery',
    9:'howitzer'
    
}
def generator():

    x = random.randint(1,5)

    password=""
    while x != 0:
        y = random.randint(1,2)
        alpha_hi =str(alphabet[random.randint(1,27)])
        alpha_low = str.lower(alphabet[random.randint(1,27)])
        symbol=symbols[random.randint(1,9)]
        word = str.title(words[random.randint(1,9)])
        if y == 1 :
            password +=str.swapcase(symbol+alpha_hi+word+alpha_low+symbol+str(random.randint(0,9)))
            x -=1
        elif y == 2 :
            password +=str(symbol+alpha_hi+word+alpha_low+symbol+str(random.randint(0,9)))
            x -=1
    return password

amount = int(input("How Many Password Do You Want To Generate?: "))
logo()

x = 0
password_list={}
while amount != 0:
    password_list[x]=generator()
    x+=1
    amount-=1
for i in password_list:
    print(str(i)+" : "+password_list[i])
