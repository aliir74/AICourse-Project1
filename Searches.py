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


