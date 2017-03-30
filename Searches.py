import sys
def BFS(initialState, Actions, GoalTest):
    f = [initialState]
    ans = []
    while(f != []):
        currentNode = f[0]
        del f[0]
        if(GoalTest(currentNode)):
            ans.append(currentNode)
        f += Actions(currentNode)
    print('F is empty!', sys.stderr)
    return ans





