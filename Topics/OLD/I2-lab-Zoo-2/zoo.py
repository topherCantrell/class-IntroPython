# syntax cheat sheet

# math ops parens, simple 'def' function calling a function
# if/else/for/while/continue/break
# [] operator, dot operator, open/close/random/input/print
# 'with' example
# dict and list literals ... complex example

import json

def load_zoo():
    f = open('zoo.json','r')
    s = f.read()
    f.close()
    ret = json.loads(s)
    return ret

ZOO = load_zoo()

def save_zoo():
    s = json.dumps(ZOO)
    f = open('zoo.json','w')
    f.write(s)
    f.close()

def ask_yes_no():
    """This function asks
    :return: 'yes' or 'no' period
    """
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

def add_new_node(parent,guess_yes_no):
    # Get the animal we guessed (could have passed that in)
    old_animal = parent[guess_yes_no]
    # Ask the user for info
    new_animal = input('What were you thinking of : ')
    new_question = input('Give me a yes/no question to separate '+new_animal+' from '+old_animal+' : ')
    print('What would the answer be for your animal : ')
    new_ans = ask_yes_no()
    # Make the new node
    new_node = {'question' : new_question}
    if new_ans=='yes':
        new_node['yes'] = new_animal
        new_node['no'] = old_animal
    else:
        new_node['no'] = new_animal
        new_node['yes'] = old_animal
    # Replace the guessed-animal with the new node
    parent[guess_yes_no] = new_node

def handle_node(node):
    # Return 'yes' or 'no' unless it is an
    # animal ... I'll that
    print(node['question'])
    ans = ask_yes_no()
    if type(node[ans])==str:
        # This is an animal
        print('Is it a', node[ans])
        guess = ask_yes_no()
        if guess=='yes':
            print('I got it!')
        else:
            print('You stumped me!')
            add_new_node(node,ans)
            save_zoo()
        return None
    else:
        return node[ans]

load_zoo()

cur_node = ZOO
while True:
    p = handle_node(cur_node)
    if p:
        cur_node = p
    else:
        cur_node=ZOO


