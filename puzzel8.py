import copy


class Puzzel:
    def __init__(self, firstState):
        self.initialSt = firstState
        self.cost = 0

    def initialState(self):
        return self.initialSt

    def Actions(self, state):
        list = []
        emptyLocation = [-1, -1]
        for i in range(3):
            for j in range(3):
                if(state[i][j] == 0):
                    emptyLocation = [i, j]
                    break
        if(emptyLocation[0] != 0):
            list.append('D')
        if(emptyLocation[0] != 2):
            list.append('U')
        if(emptyLocation[1] != 0):
            list.append('R')
        if(emptyLocation[1] != 2):
            list.append('L')
        return list

    def Result(self, state, action):
        stateans = copy.deepcopy(state)
        emptyLocation = [-1, -1]
        for i in range(3):
            for j in range(3):
                if (state[i][j] == 0):
                    emptyLocation = [i, j]
                    break
        if(action == 'L'):
            stateans[emptyLocation[0]][emptyLocation[1]], stateans[emptyLocation[0]][emptyLocation[1]+1] =\
                stateans[emptyLocation[0]][emptyLocation[1]+1], stateans[emptyLocation[0]][emptyLocation[1]]
        elif(action == 'R'):
            stateans[emptyLocation[0]][emptyLocation[1]], stateans[emptyLocation[0]][emptyLocation[1] -1] = \
                stateans[emptyLocation[0]][emptyLocation[1] -1], stateans[emptyLocation[0]][emptyLocation[1]]
        elif(action == 'D'):
            stateans[emptyLocation[0]][emptyLocation[1]], stateans[emptyLocation[0]-1][emptyLocation[1]] = \
                stateans[emptyLocation[0]-1][emptyLocation[1]], stateans[emptyLocation[0]][emptyLocation[1]]
        elif(action == 'U'):
            stateans[emptyLocation[0]][emptyLocation[1]], stateans[emptyLocation[0] +1][emptyLocation[1]] = \
                stateans[emptyLocation[0] +1][emptyLocation[1]], stateans[emptyLocation[0]][emptyLocation[1]]
        return stateans

    def GoalTest(self, state):
        if(state == [[1, 2, 3], [4,5,6],[7,8,0]]):
            return True
        return False

    def GoalState(self):
        return [[1, 2, 3], [4,5,6],[7,8,0]]

    def stepCost(self, state, action):
        return 1
        #self.cost += 1

    def pathCost(self):
        return self.cost

    def H(self, state):
        goal = [[1,2,3],[4,5,6],[7,8,0]]
        ans = 0
        for i in range(3):
            for j in range(3):
                if(goal[i][j] != state[i][j]):
                    ans += 1
        return ans

