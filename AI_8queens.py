import random 

def isBetterState(currentState, nextState):
    F_nextState = pairs_attacking(nextState)
    F_currentState = pairs_attacking(currentState)

    delta_E = F_nextState - F_currentState
    if(delta_E <= 0):
        return 1
    else:
        return -1

def successors(queens): #successor function
    generated = 1
    expanded = 0
    currentState = queens.copy()
    
    if(isGoal(currentState) == True):
        return generated, expanded, currentState

    while 1:
        nextState = currentState.copy()
        nextState[random.randint(0,7)] = random.randint(0,7)
        generated += 1
        print('Successor: ', nextState)
            
        if(isBetterState(currentState, nextState) == 1):
            expanded += 1
            print('Better')
            if(isGoal(nextState)):
                return generated, expanded, nextState
            currentState = nextState.copy()
    return generated, expanded, []

def pairs_attacking(queens): #objective function
    attacks = 0
    for i in range(8):
        for j in range(i+1, 8):
            if(queens[i] == queens[j]):
                attacks += 1
            if(abs(i-j) == abs(queens[i] - queens[j])):
                attacks += 1
    return attacks

def isGoal(state):   
    return pairs_attacking(state) == 0

def initialState():
    return list(random.randint(0, 7) for i in range(8))

def printState(state):
    for i in range(8):
        for j in range(8):
            if state[j] == i:
                print('Q', end = ' ')
            else:
                print('_', end = ' ')
        print()

queens = initialState()
generated, expanded, goalState = successors(queens)
print('\nInitial State: ', queens)
print('No. of nodes generated:', generated)
print('No. of nodes expanded:', expanded)
print('Goal State: ', goalState)
printState(goalState)