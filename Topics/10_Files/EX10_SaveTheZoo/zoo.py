import json

INIT_DATA = {
    'question' : 'Does it live on land?',
    'yes' : {
        'question' : 'Does it live on a farm?',
        'no' : 'lion',
        'yes' : 'cow'
    },
    'no' : 'fish'    
}

def load_zoo():
    try:
        with open('zoo.json') as f:
            data = f.read()
            zoo = json.loads(data)
    except:
        print('Brand new zoo!')
        zoo = INIT_DATA
        
    return zoo

def save_zoo(zoo):
    with open('zoo.json','w') as f:
        data = json.dumps(zoo)
        f.write(data)    

def ask_yes_no():
    while True:
        ans = input('yes/no : ')
        ans = ans.strip()
        ans = ans.upper()
        if len(ans)>0:
            if ans[0] == 'Y':
                return 'yes'
            elif ans[0] == 'N':
                return 'no'
        else:
            print('???')
    return ans

def add_new_node(parent_node,ans_to_change,new_animal,new_question,ans_for_new_animal):
    
    node = {'question' : new_question}
    
    old_animal = parent_node[ans_to_change]
    
    if ans_for_new_animal == 'yes':
        node['yes'] = new_animal
        node['no'] = old_animal
    else:
        node['yes'] = old_animal
        node['no'] = new_animal
        
    parent_node[ans_to_change] = node

ZOO = load_zoo()

cur_node = ZOO
while True:
    print(cur_node['question'])
    ans = ask_yes_no()
    
    next_node = cur_node[ans]
    if isinstance(next_node,dict):
        cur_node = next_node
    else:
        print('My guess is:',next_node)
        print('Did I guess it?')
        g = ask_yes_no()
        if g=='no':
            # Gather the info for the new node       
            new_animal = input('What were you thinking of? ')
            new_question = input('Give me a question to separate '+next_node+' from '+new_animal+': ')
            print('And what would the answer be for',new_animal)
            ans_for_new_animal = ask_yes_no()
            # Add the new node
            add_new_node(cur_node,ans,new_animal,new_question,ans_for_new_animal)
            save_zoo(ZOO)
            
        print('Let\'s play again!')
        cur_node = ZOO
