import sys
def BFSTree(initialState, Actions, GoalTest, Result, stepCost, pathCost):
    f = [initialState()]
    while(f != []):
        stepCost()
        currentNode = f[0]
        del f[0]
        if(GoalTest(currentNode)):
            return currentNode, pathCost()
        actions = Actions(currentNode)
        for a in actions:
            f += Result(currentNode, a)
    print('F is empty!', sys.stderr)


def DLS(initialState, Actions, GoalTest, Result, stepCost, pathCost):
    return DLSRecursive(initialState(), Actions, GoalTest, Result, stepCost, pathCost)

def DLSRecursive(state, Actions, GoalTest, Result, stepCost, pathCost, limit):
    if(GoalTest(state)):
        return state, pathCost()
    elif(limit == 0):
        return 'cutoff', pathCost()

    cutoff = False
    for a in Actions(state):
        child = Result(state, a)
        stepCost()
        res = DLSRecursive(state, Actions, GoalTest, Result, stepCost, pathCost, limit-1)
        if(res == 'cutoff'):
            cutoff = True
        elif(res != 'failure'):
            return res, pathCost()
    if(cutoff):
        return 'cutoff', pathCost()
    else:
        return 'failure', pathCost()


