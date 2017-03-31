import sys
def BFSTree(problem):
    f = [problem.initialState()]
    while(f != []):
        problem.stepCost()
        currentNode = f[0]
        del f[0]
        if(problem.GoalTest(currentNode)):
            return currentNode, problem.pathCost()
        actions = problem.Actions(currentNode)
        for a in actions:
            f += problem.Result(currentNode, a)
    print('F is empty!', sys.stderr)


def DLS(problem, limit):
    return DLSRecursive(problem.initialState(), problem, limit)

def DLSRecursive(state, problem, limit):
    if(problem.GoalTest(state)):
        return state, problem.pathCost()
    elif(limit == 0):
        return 'cutoff', problem.pathCost()

    cutoff = False
    for a in problem.Actions(state):
        child = problem.Result(state, a)
        problem.stepCost()
        res = DLSRecursive(state, problem, limit-1)
        if(res == 'cutoff'):
            cutoff = True
        elif(res != 'failure'):
            return res, problem.pathCost()
    if(cutoff):
        return 'cutoff', problem.pathCost()
    else:
        return 'failure', problem.pathCost()


def IDS(problem):
    for depth in range(1000):
        res = DLS(problem, depth)
        if(res != 'cutoff'):
            return res

    return 'failure'
