
# Testing data
ZOO = {
    'question' : 'Does it live on land?',
    'yes' : {
        'question' : 'Does it live on a farm?',
        'no' : 'LION',
        'yes' : 'COW'
    },
    'no' : 'FISH'    
}

def add_new_animal(parent_node,ans_to_change,new_animal,new_question,ans_for_new_animal):
    # TODO: your code here
    pass

print(ZOO)

node = ZOO # Does it live on land?
add_new_animal(node,'no','OCTOPUS','Does it have 8 arms?','yes')

print(ZOO)

node = ZOO['yes'] # Would you find it on a farm?
add_new_animal(node,'yes','CHICKEN','Do you milk it?','no')

print(ZOO)
