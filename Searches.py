import copy
import queue
import sys
def BFSTree(problem):
    f = [[problem.initialState()]]
    seenNode = 1
    expandedNode = 0
    memory = 0
    while(f != []):

        currentNode = f[0]
        del f[0]
        expandedNode += 1
        actions = problem.Actions(currentNode[-1])
        for a in actions:
            child = problem.Result(currentNode[-1], a)
            tmp = copy.deepcopy(currentNode)
            tmp.append(child)
            f += tmp
            seenNode += 1
            memory = sys.getsizeof(f)
            problem.stepCost(currentNode[-1], a)
            if(problem.GoalTest(child)):
                return tmp, len(tmp)-1, expandedNode, seenNode, memory
    print('There isnt any solution to destination state ( BFS Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory

def BFSGraph(problem):
    f = [[problem.initialState()]]
    e = []
    seenNode = 1
    expandedNode = 0
    memory = 0
    while(f != []):

        currentNode = f[0]
        del f[0]
        e.append(currentNode[-1])
        expandedNode += 1
        actions = problem.Actions(currentNode[-1])
        for a in actions:
            child = problem.Result(currentNode[-1], a)
            if(not((child not in e)and(child not in f))):
                continue
            tmp = copy.deepcopy(currentNode)
            tmp.append(child)
            f += tmp
            seenNode += 1
            memory = sys.getsizeof(f)
            problem.stepCost(currentNode[-1], a)
            if(problem.GoalTest(child)):
                return tmp, len(tmp)-1, expandedNode, seenNode, memory
    print('There isnt any solution to destination state ( BFS Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory

def bidrectional(problem):
    pass



def UCSTree(problem):
    f = queue.PriorityQueue(0)
    f.put((0, [problem.initialState()]))
    seenNode = 1
    expandedNode = 0
    memory = 0
    while (not f.empty()):
        currentNode = f.get()
        expandedNode += 1
        actions = problem.Actions(currentNode[1][-1])
        for a in actions:
            child = problem.Result(currentNode[1][-1], a)
            tmp = copy.deepcopy(currentNode[1])
            tmp.append(child)
            seenNode += 1
            f.put(currentNode[0] + problem.stepCost(currentNode[1][-1], a), tmp)
            memory = sys.getsizeof(f)
            if (problem.GoalTest(child)):
                return tmp, currentNode[0] + problem.stepCost(currentNode[1][-1], a), expandedNode, seenNode, memory

    print('There isnt any solution to destination state ( USC Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory

def UCSGraph(problem):
    f = queue.PriorityQueue(0)
    f.put((0, [problem.initialState()]))
    f2 = [problem.initialState()]
    e = []
    seenNode = 1
    expandedNode = 0
    memory = 0
    while (not f.empty()):
        currentNode = f.get()
        e.append(currentNode[1][-1])
        expandedNode += 1
        actions = problem.Actions(currentNode[1][-1])
        for a in actions:
            child = problem.Result(currentNode[1][-1], a)
            if (not ((child not in e) and (child not in f2))):
                continue
            f2.append(child)
            tmp = copy.deepcopy(currentNode[1])
            tmp.append(child)
            seenNode += 1
            f.put(currentNode[0] + problem.stepCost(currentNode[1][-1], a), tmp)
            memory = sys.getsizeof(f)
            if (problem.GoalTest(child)):
                return tmp, currentNode[0] + problem.stepCost(currentNode[1][-1], a), expandedNode, seenNode, memory

    print('There isnt any solution to destination state ( USC Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory

def Astar(problem):
    f = queue.PriorityQueue(0)
    f.put((0+problem.H(problem.initialState()), [0, [problem.initialState()]]))
    seenNode = 1
    expandedNode = 0
    memory = 0
    while (not f.empty()):
        currentNode = f.get()
        expandedNode += 1
        actions = problem.Actions(currentNode[1][1][-1])
        for a in actions:
            child = problem.Result(currentNode[1][1][-1], a)
            tmp = copy.deepcopy(currentNode[1])
            tmp[1].append(child)
            tmp[0] += problem.stepCost(currentNode[1][1][-1], a)
            seenNode += 1
            f.put(problem.H(child) + currentNode[0] + problem.stepCost(currentNode[1][-1], a), tmp)
            memory = sys.getsizeof(f)
            if (problem.GoalTest(child)):
                return tmp[1], tmp[0], expandedNode, seenNode, memory

    print('There isnt any solution to destination state ( Astar Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory

def AstarGraph(problem):
    f = queue.PriorityQueue(0)
    f.put((0+problem.H(problem.initialState()), [0, [problem.initialState()]]))
    e = []
    f2 = [problem.initialState()]
    seenNode = 1
    expandedNode = 0
    memory = 0
    while (not f.empty()):
        currentNode = f.get()
        expandedNode += 1
        e.append(currentNode[1][1][-1])
        actions = problem.Actions(currentNode[1][1][-1])
        for a in actions:
            child = problem.Result(currentNode[1][1][-1], a)
            if (not ((child not in e) and (child not in f2))):
                continue
            f2.append(child)
            tmp = copy.deepcopy(currentNode[1])
            tmp[1].append(child)
            tmp[0] += problem.stepCost(currentNode[1][1][-1], a)
            seenNode += 1
            f.put(problem.H(child) + currentNode[0] + problem.stepCost(currentNode[1][-1], a), tmp)
            memory = sys.getsizeof(f)
            if (problem.GoalTest(child)):
                return tmp[1], tmp[0], expandedNode, seenNode, memory

    print('There isnt any solution to destination state ( Astar Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory


def DFSTree(problem):
    f = [[problem.initialState()]]
    seenNode = 1
    expandedNode = 0
    memory = 0
    while(f != []):

        currentNode = f[-1]
        del f[-1]
        expandedNode += 1
        actions = problem.Actions(currentNode[-1])
        for a in actions:
            child = problem.Result(currentNode[-1], a)
            tmp = copy.deepcopy(currentNode)
            tmp.append(child)
            f += tmp
            seenNode += 1
            memory = sys.getsizeof(f)
            problem.stepCost(currentNode[-1], a)
            if(problem.GoalTest(child)):
                return tmp, len(tmp)-1, expandedNode, seenNode, memory
    print('There isnt any solution to destination state ( BFS Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory

def DFSGraph(problem):
    f = [[problem.initialState()]]
    e = []
    seenNode = 1
    expandedNode = 0
    memory = 0
    while(f != []):

        currentNode = f[-1]
        del f[-1]
        e.append(currentNode[-1])
        expandedNode += 1
        actions = problem.Actions(currentNode[-1])
        for a in actions:
            child = problem.Result(currentNode[-1], a)
            if (not ((child not in e) and (child not in f))):
                continue
            tmp = copy.deepcopy(currentNode)
            tmp.append(child)
            f += tmp
            seenNode += 1
            memory = sys.getsizeof(f)
            problem.stepCost(currentNode[-1], a)
            if(problem.GoalTest(child)):
                return tmp, len(tmp)-1, expandedNode, seenNode, memory
    print('There isnt any solution to destination state ( BFS Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory

'''

def DFS(problem):
    return DFSRecursive(problem.initialState(), problem)
def DFSRecursive(state, problem):
    if(state == problem.GoalTest()):
        return state, problem.pathCost()

    for a in problem.Actions(state):
        child = problem.Result(state, a)
        problem.stepCost(state, a)
        res = DFSRecursive(child, problem)
        if(res[0] != 'failure'):
            return res
    return 'failure', problem.pathCost()
'''

def DLSTree(problem, limit):
    f = [[problem.initialState()]]
    seenNode = 1
    expandedNode = 0
    memory = 0
    while(f != []):
        currentNode = f[-1]
        del f[-1]
        if(len(currentNode) > limit):
            continue
        expandedNode += 1
        actions = problem.Actions(currentNode[-1])
        for a in actions:
            child = problem.Result(currentNode[-1], a)
            tmp = copy.deepcopy(currentNode)
            tmp.append(child)
            f += tmp
            seenNode += 1
            memory = sys.getsizeof(f)
            problem.stepCost(currentNode[-1], a)
            if(problem.GoalTest(child)):
                return tmp, len(tmp)-1, expandedNode, seenNode, memory
    print('There isnt any solution to destination state ( DLS Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory

def DLSGraph(problem, limit):
    f = [[problem.initialState()]]
    e = []
    seenNode = 1
    expandedNode = 0
    memory = 0
    while(f != []):
        currentNode = f[-1]
        del f[-1]
        if(len(currentNode) > limit):
            continue
        e.append(currentNode[-1])
        expandedNode += 1
        actions = problem.Actions(currentNode[-1])
        for a in actions:
            child = problem.Result(currentNode[-1], a)
            if (not ((child not in e) and (child not in f))):
                continue
            tmp = copy.deepcopy(currentNode)
            tmp.append(child)
            f += tmp
            seenNode += 1
            memory = sys.getsizeof(f)
            problem.stepCost(currentNode[-1], a)
            if(problem.GoalTest(child)):
                return tmp, len(tmp)-1, expandedNode, seenNode, memory
    print('There isnt any solution to destination state ( DLS Tree )!', sys.stderr)
    return [], 0, expandedNode, seenNode, memory


'''
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
        problem.stepCost(state, a)
        res = DLSRecursive(child, problem, limit-1)
        if(res[0] == 'cutoff'):
            cutoff = True
        elif(res[0] != 'failure'):
            return res
    if(cutoff):
        return 'cutoff', problem.pathCost()
    else:
        return 'failure', problem.pathCost()

'''

def IDS(problem):
    for depth in range(1, 1000):
        path, cost, exapndNode, seenNode, memory = DLSTree(problem, depth)
        if(path != []):
            return path, cost, exapndNode, seenNode, memory

    return path, cost, exapndNode, seenNode, memory

def IDSGraph(problem):
    for depth in range(1, 1000):
        path, cost, exapndNode, seenNode, memory = DLSGraph(problem, depth)
        if(path != []):
            return path, cost, exapndNode, seenNode, memory

    return path, cost, exapndNode, seenNode, memory