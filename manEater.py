import math


class manEater:
    def __init__(self, initialState):
        self.initialState = initialState
        self.cost = 0

    def initialState(self):
        return self.initialState

    def Actions(self, state):
        list = []
        leftEater = state[1][0][0]
        leftReligious = state[1][0][1]
        rightEater = state[1][0][1]
        rightReligious = state[1][1][1]
        boatPlace = state[0]

        if(boatPlace == 'left'):
            list.append('right-1-1')
            if(rightReligious > rightEater):
                list.append('right-1-0')
            if(leftReligious > leftEater):
                list.append('right-0-1')
        if(boatPlace == 'right'):
            list.append('left-1-1')
            if (leftReligious > leftEater):
                list.append('left-1-0')
            if (rightReligious > rightEater):
                list.append('left-0-1')
        return list

    def Result(self, state, action):
        direction, eaterCount, religiousCount = action.split('-')
        if(direction == 'right'):
            state[1][1][0] += int(eaterCount)
            state[1][1][1] += int(religiousCount)
        else:
            state[1][0][0] += int(eaterCount)
            state[1][0][1] += int(religiousCount)

        if(state[0] == 'right'):
            state[0] = 'left'
        else:
            state[1] = 'right'

        return state

    def GoalTest(self, state):
        if(state == ['right', [ [0,0], [3,3] ] ]):
            return True
        return False

    def stepCost(self, state, action):
        self.cost += 1

    def pathCost(self):
        return self.cost

    def H(self, state):
        leftEater = state[1][0][0]
        leftReligious = state[1][0][1]
        boatPlace = state[0]
        if(boatPlace == 'left'):
            return math.ceil((leftEater+leftReligious)/2)
        elif(boatPlace == 'right'):
            return math.ceil((leftEater + leftReligious+1) / 2)