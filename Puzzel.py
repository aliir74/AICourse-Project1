class Puzzel:
    def __init__(self, initialState):
        self.initialState = initialState

    def initialState(self):
        return self.initialState

    def Actions(self, state):
        list = []
        emptyLocation = [-1, -1]
        for i in range(3):
            for j in range(3):
                if(state[i][j] == 0):
                    emptyLocation = [i, j]
                    break
        if(emptyLocation[0] != 0):
            list.append('U')
        if(emptyLocation[0] != 2):
            list.append('D')
        if(emptyLocation[1] != 0):
            list.append('L')
        if(emptyLocation[1] != 2):
            list.append('R')
        return list

    def Result(self, state, action):
        emptyLocation = [-1, -1]
        for i in range(3):
            for j in range(3):
                if (state[i][j] == 0):
                    emptyLocation = [i, j]
                    break
        if(action == 'R'):
            state[emptyLocation[0]][emptyLocation[1]], state[emptyLocation[0]][emptyLocation[1]+1] =\
                state[emptyLocation[0]][emptyLocation[1]+1], state[emptyLocation[0]][emptyLocation[1]]
        elif(action == 'L'):
            state[emptyLocation[0]][emptyLocation[1]], state[emptyLocation[0]][emptyLocation[1] -1] = \
                state[emptyLocation[0]][emptyLocation[1] -1], state[emptyLocation[0]][emptyLocation[1]]
        elif(action == 'U'):
            state[emptyLocation[0]][emptyLocation[1]], state[emptyLocation[0]-1][emptyLocation[1]] = \
                state[emptyLocation[0]-1][emptyLocation[1]], state[emptyLocation[0]][emptyLocation[1]]
        elif(action == 'D'):
            state[emptyLocation[0]][emptyLocation[1]], state[emptyLocation[0] +1][emptyLocation[1]] = \
                state[emptyLocation[0] +1][emptyLocation[1]], state[emptyLocation[0]][emptyLocation[1]]
        return state

    def GoalTest(self, state):
        if(state == [[1, 2, 3], [4,5,6],[7,8,0]]):
            return True
        return False

    def stepCost(self, state, action):
        self.cost += 1

    def pathCost(self):
        return self.cost

