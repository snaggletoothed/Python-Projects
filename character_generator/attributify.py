

####Main attributes
#• Strength
#• Agility
#• Knowledge 

#Secondary
# Strength
#• Attack
#• Health
# Agility 
#• Initiative
#• Defence
#• Dodge
#• Critical
# Knowledge 
#• Mana
#• Awareness

def assign_attributes():
    import random
#generate frame of attributes
    attributes = {
    'strenght' : {'core': 0, 'attack' : 0, "health" : 0},
    'agility' : {'core': 0, 'initiative' : 0, 'defence' : 0, 'dodge' : 0,'critical' : 0},
    'knowledge' : {'core' : 0, 'mana' : 0, 'awareness' : 0}
    }  
#assign random values to attributes     
    x = random.randint(1,10)
    attributes['strenght']['attack'] = x
    x = random.randint(5,25)
    attributes['strenght']['health'] = x
    x = random.randint(0,10)
    attributes['agility']['initiative'] = x
    x = random.randint(0,10)
    attributes['agility']['defence'] = x
    x = random.randint(0,10)
    attributes['agility']['dodge'] = x
    x = random.randint(0,2)
    attributes['agility']['critical'] = x
    x = random.randint(5,15)
    attributes['knowledge']['mana'] = x
    x = random.randint(0,10)
    attributes['knowledge']['awareness'] = x
    return attributes
    
     
      
def aptitude_test():
    
    def question_1():        
        choice = input("""
        Thou art traveling from a bawbling farm down a dirt road
        on a cabbage cart and noticeth a goblin raiding party. 
        Doth thee:
            
        (1) behold f'r aught yond can beest madeth into a weapon
        and attacketh. 
        (2) useth an ancient curse to transf'rm the cabbages
        into bloodlusting carniv'rious
        v'rsions of themselves yond art und'r thy commandeth. 
        (3) sneaketh backeth to the farm to f'rm an ambush party and
        striketh at which hour least did expect.  
         
        chooseth eith'r (1), (2), 'r (3)""")
        choice = int(choice)
        
        if choice == 1:
            aptitude_result = {
            'strenght' : {'core' : 3},
            'agility' : {'core': 2 },
            'knowledge' : {'core' : 1}
            }
            return aptitude_result
        if choice == 2:
            aptitude_result = {
            'strenght' : {'core' : 1},
            'agility' : {'core': 3 },
            'knowledge' : {'core' : 2}
            }
            return aptitude_result
        if choice == 3:
            aptitude_result = {
            'strenght' : {'core' : 2},
            'agility' : {'core': 1 },
            'knowledge' : {'core' : 3}
            }
            return aptitude_result
        else:
            print('incorrect input')
            question_1()
    def question_2():
        choice = input("""
         Thou art in the city market taking in the smells,
        sights, and sounds of market day at which hour thee notice
        a cut-purse taking off with someone's coin purse!
        doth thee:
        (1) taketh off after the cut-purse and tryeth and chase those folk down. 
         (2) grab a murderious cabbage from one of the stalls
        and throweth directly at the cut-purse. 
         (3) inform the local constabulary about the theft and
        giveth to holp with any information to holp unfold the coystrill        
        """)
        choice = int(choice)
        
        if choice == 1:
            aptitude_result = {
            'strenght' : {'core' : 3},
            'agility' : {'core': 2 },
            'knowledge' : {'core' : 1}
            }
            return aptitude_result
        if choice == 2:
            aptitude_result = {
            'strenght' : {'core' : 1},
            'agility' : {'core': 3 },
            'knowledge' : {'core' : 2}
            }
            return aptitude_result
        if choice == 3:
            aptitude_result = {
            'strenght' : {'core' : 2},
            'agility' : {'core': 1 },
            'knowledge' : {'core' : 3}
            }
            return aptitude_result
        else:
            print('incorrect input')
            question_2()
    r1 = question_1()    
    r2 = question_2()    
    strenght = r1['strenght']['core']  + r2['strenght']['core']
    agility = r1['agility']['core']  + r2['agility']['core']
    knowledge = r1['knowledge']['core']  + r2['knowledge']['core'] 
    aptitude = {
    'strenght' : {'core' : strenght},
    'agility' : {'core' : agility},
    'knowledge' : {'core':knowledge}
    
    
    }
    return aptitude
