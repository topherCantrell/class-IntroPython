
# Testing data
ZOO = {
    'question' : 'Does it live on land?',
    'yes' : {
        'question' : 'Does it live on a farm?',
        'no' : 'lion',
        'yes' : 'cow'
        },
    'no' : 'fish'
    }

def get_yes_no():
    """Ask the user for a 'yes' or 'no'.
    :returns: either a 'yes' or a 'no'.
    """
    while True:
        yn = input('yes/no: ')
        if yn.upper().startswith('Y'):
            return 'yes'
        elif yn.upper().startswith('N'):
            return 'no'
        else:
            print("I don't understand.")
            
def add_new_node(parent,guess_yes_no):
    # Get the animal we guessed (could have passed that in)
    old_animal = parent[guess_yes_no]
    # Ask the user for info
    new_animal = input('What were you thinking of : ')
    new_question = input('Give me a yes/no question to separate '+new_animal+' from '+old_animal+' : ')
    print('What would the answer be for your animal : ')
    new_ans = get_yes_no()
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
    """Handle a single node in the zoo.
    This function prints the question and gets the user's response.
    :returns: the next question to process (or None if done)
    """
    print(node['question'])
    ans = get_yes_no()
    next = node[ans]
    if type(next) is not str:
        # This next node is dictionary. That's the next node
        # to go to.
        return next
    else:
        # This is a string. We've reached our guess animal.
        print('Is it a',next,'?')
        was_right = get_yes_no()
        if was_right=='yes':
            print('I got it!')
            return None
        else:
            print('You stumped me!')
            add_new_node(node,ans)
            return None

p = ZOO
while True:
    n = handle_node(p)
    if n==None:
        # This is the end. Start over.
        print()
        print("Let's play again.")
        n = ZOO
    p = n