
node_farm = {
    'question': 'Does it live on a farm?',
    'yes': 'COW',
    'no': 'LION'
}

node_land = {
    'question': 'Does it live on land?',
    'yes': node_farm,
    'no': 'FISH',
}

# OR ...

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

def get_yes_no():    
    while True:
        yn = input('yes/no: ')
        if yn.upper().startswith('Y'):
            return 'yes'
        elif yn.upper().startswith('N'):
            return 'no'
        else:
            print("I don't understand.")
           
    
def add_new_animal(parent_node,ans_to_change,new_animal,new_question,ans_for_new_animal):
    # This was our best guess
    old_animal = parent_node[ans_to_change]
    # Make the new node
    new_node = {'question' : new_question}
    if ans_for_new_animal=='yes':
        new_node['yes'] = new_animal
        new_node['no'] = old_animal
    else:
        new_node['no'] = new_animal
        new_node['yes'] = old_animal
    # Change the parent to point to the new node
    parent_node[ans_to_change] = new_node


while True:
    # Ask the question and get the answer   
    print(current_node['question'])
    ans = get_yes_no()
    
    # If the answer leads to another question, then
    # change nodes to that node and continue
    next_node = current_node[ans]
    if isinstance(next_node,dict):
        current_node = next_node
        continue
    
    # print('My guess is: '+next_node)
    
    # We got to a string. Is this the right animal?
    print('Were you thinking of a '+next_node+'?')
    got_it = get_yes_no()
    
    if got_it=='no':
        # The animal we guessed (we'll use that in asking the user for a question)
        old_animal = current_node[ans]
        # Ask the user for info
        new_animal = input('What were you thinking of : ')
        new_question = input('Give me a yes/no question to separate '+new_animal+' from '+old_animal+' : ')
        print('What would the answer be for your animal : ')
        new_ans = get_yes_no()
        
        add_new_animal(current_node,ans,new_animal,new_question,new_ans)
    
    # Restart at the top of the tree
    current_node = ZOO      
    print('Let\'s play again!')    
    
