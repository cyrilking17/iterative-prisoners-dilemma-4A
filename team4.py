import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'no u' # Only 10 chars displayed.
strategy_name = 'predict and counter'

strategy_description = 'Predict next move and counter attack'

    
def move(my_history, their_history, my_score, their_score):
  Nb = 0
  Nc = 0
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    for x in ipairs(their_history):
        if x == 'b':
            Nb += 1
        else:
            Nc += 1
    if len(my_history)=<5: 
        return 'c'
    elif len(my_history)>5 and len(my_history)=<10:
        return 'b'
    elif len(my_history) > 10:
        if Nb > Nc:
            return 'b'
        elif Nc > Nb:
            return 'c'
        else:
            if random.randint(0,100) <= 50:
                return 'c'
            else:
                return 'b'