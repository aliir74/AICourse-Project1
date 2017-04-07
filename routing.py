import Searches

class RomanianRouting:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.cost = 0


    def initialState(self):
        return self.source


    def Actions(self, state):
        ans = []
        if(state == 'Oradea'):
            ans = ['Zerind', 'Sibiu']
        elif(state == 'Zerind'):
            ans = ['Oradea', 'Arad']
        elif(state == 'Arad'):
            ans = ['Zerind', 'Sibiu', 'Timisoara']
        elif(state == 'Sibiu'):
            ans = ['Oradea', 'Arad', 'Rimnicu Vilcea', 'Fagaras']
        elif(state == 'Fagaras'):
            ans = ['Sibiu', 'Bucharest']
        elif(state == 'Rimnicu Vilcea'):
            ans = ['Sibiu', 'Pitesti', 'Craiova']
        elif(state == 'Timisoara'):
            ans = ['Arad', 'Lugoj']
        elif(state == 'Lugoj'):
            ans = ['Timisoara', 'Mehadia']
        elif(state == 'Pitesti'):
            ans = ['Rimnicu Vilcea', 'Craiova', 'Bucharest']
        elif(state == 'Mehadia'):
            ans = ['Lugoj', 'Dobreta']
        elif(state == 'Bucharest'):
            ans = ['Pitesti', 'Fagaras', 'Giurgiu', 'Urziceni']
        elif(state == 'Dobreta'):
            ans = ['Mehadia', 'Craiova']
        elif(state == 'Craiova'):
            ans = ['Dobreta', 'Rimnicu Vilcea', 'Pitesti']
        elif(state == 'Giurgiu'):
            ans = ['Bucharest']
        elif(state == 'Urziceni'):
            ans = ['Bucharest', 'Vaslui', 'Hirsova']
        elif(state == 'Hirsova'):
            ans = ['Urziceni', 'Eforie']
        elif(state == 'Eforie'):
            ans = ['Hirsova']
        elif(state == 'Vaslui'):
            ans = ['Urziceni', 'Iasi']
        elif(state == 'Iasi'):
            ans = ['Vaslui', 'Neamt']
        elif(state == 'Neamt'):
            ans = ['Iasi']
        list = ['go->'+i for i in ans]
        return list

    def Result(self, state, action):
        return action.split('->')[1]

    def GoalTest(self, state):
        if(state == self.destination):
            return True
        return False

    def GoalState(self):
        return self.destination

    def stepCost(self, state, action):
        nextState = action.split('->')[1]
        #print(state, nextState)
        if(state == nextState):
            return 0
        if (state == 'Oradea'):
            if(nextState == 'Zerind'):
                return 71
            elif(nextState == 'Sibiu'):
                return 151
        elif (state == 'Zerind'):
            if(nextState == 'Oradea'):
                return 71
            elif(nextState == 'Arad'):
                return 75
        elif (state == 'Arad'):
            if(nextState == 'Zerind'):
                return 75
            elif(nextState == 'Sibiu'):
                return 140
            elif(nextState == 'Timisoara'):
                return 118
        elif (state == 'Sibiu'):
            if(nextState == 'Oradea'):
                return 151
            elif(nextState == 'Arad'):
                return 140
            elif(nextState == 'Rimnicu Vilcea'):
                return 80
            elif(nextState == 'Fagaras'):
                return 99
        elif (state == 'Fagaras'):
            if(nextState == 'Sibiu'):
                return 99
            elif(nextState == 'Bucharest'):
                return 211
        elif (state == 'Rimnicu Vilcea'):
            if(nextState == 'Sibiu'):
                return 80
            elif(nextState == 'Pitesti'):
                return 97
            elif(nextState == 'Craiova'):
                return 146
        elif (state == 'Timisoara'):
            if(nextState == 'Arad'):
                return 118
            elif(nextState == 'Lugoj'):
                return 111
        elif (state == 'Lugoj'):
            if(nextState == 'Timisoara'):
                return 111
            elif(nextState == 'Mehadia'):
                return 70
        elif (state == 'Pitesti'):
            if(nextState == 'Rimnicu Vilcea'):
                return 97
            elif(nextState == 'Craiova'):
                return 138
            elif(nextState == 'Bucharest'):
                return 101
        elif (state == 'Mehadia'):
            if(nextState == 'Lugoj'):
                return 70
            elif(nextState == 'Dobreta'):
                return 75
        elif (state == 'Bucharest'):
            if(nextState == 'Pitesti'):
                return 101
            elif(nextState == 'Fagaras'):
                return 211
            elif(nextState == 'Giurgiu'):
                return 90
            elif(nextState == 'Urziceni'):
                return 85
        elif (state == 'Dobreta'):
            if(nextState == 'Mehadia'):
                return 75
            elif(nextState == 'Craiova'):
                return 120
        elif (state == 'Craiova'):
            if(nextState == 'Dobreta'):
                return 120
            elif(nextState == 'Rimnicu Vilcea'):
                return 146
            elif(nextState == 'Pitesti'):
                return 138
        elif (state == 'Giurgiu'):
            if(nextState == 'Bucharest'):
                return 90
        elif (state == 'Urziceni'):
            if(nextState == 'Bucharest'):
                return 85
            elif(nextState == 'Vaslui'):
                return 142
            elif(nextState == 'Hirsova'):
                return 98
        elif (state == 'Hirsova'):
            if(nextState == 'Urziceni'):
                return 98
            elif(nextState == 'Eforie'):
                return 86
        elif (state == 'Eforie'):
            if(nextState == 'Hirsova'):
                return 86
        elif (state == 'Vaslui'):
            if(nextState == 'Urziceni'):
                return 142
            elif(nextState == 'Iasi'):
                return 92
        elif (state == 'Iasi'):
            if(nextState == 'Vaslui'):
                return 92
            elif(nextState == 'Neamt'):
                return 87
        elif (state == 'Neamt'):
            if(nextState == 'Iasi'):
                return 87

    def pathCost(self):
        return self.cost


    def H(self, state):
        if(state == self.destination):
            return 0
        problem = RomanianRouting(state, self.destination)
        a, b, c, d, e = Searches.UCSGraph(problem)
        if(b > 211):
            b -= 211
        else:
            b = 0
        return b
