class RomanianRouting:
    def __init__(self, source, destination):
        self.initialState = source
        self.destination = destination
        self.cost = 0


    def getInitialState(self):
        return self.initialState


    def Actions(self, state):
        ans = []
        if(state == 'Ordaea'):
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

    def stepCost(self, state, action):
        nextState = action.split('->')[1]

        if (state == 'Ordaea'):
            if(nextState == 'Zerind'):
                self.cost += 71
            elif(nextState == 'Sibiu'):
                self.cost += 151
        elif (state == 'Zerind'):
            if(nextState == 'Oradea'):
                self.cost += 71
            elif(nextState == 'Arad'):
                self.cost += 75
        elif (state == 'Arad'):
            if(nextState == 'Zerind'):
                self.cost += 75
            elif(nextState == 'Sibiu'):
                self.cost += 140
            elif(nextState == 'Timisoara'):
                self.cost += 118
        elif (state == 'Sibiu'):
            if(nextState == 'Oradea'):
                self.cost += 151
            elif(nextState == 'Arad'):
                self.cost += 140
            elif(nextState == 'Rimnicu Vilcea'):
                self.cost += 80
            elif(nextState == 'Fagaras'):
                self.cost += 99
        elif (state == 'Fagaras'):
            if(nextState == 'Sibiu'):
                self.cost += 99
            elif(nextState == 'Bucharest'):
                self.cost += 211
        elif (state == 'Rimnicu Vilcea'):
            if(nextState == 'Sibiu'):
                self.cost += 80
            elif(nextState == 'Pitesti'):
                self.cost += 97
            elif(nextState == 'Craiova'):
                self.cost += 146
        elif (state == 'Timisoara'):
            if(nextState == 'Arad'):
                self.cost += 118
            elif(nextState == 'Lugoj'):
                self.cost += 111
        elif (state == 'Lugoj'):
            if(nextState == 'Timisoara'):
                self.cost += 111
            elif(nextState == 'Mehadia'):
                self.cost += 70
        elif (state == 'Pitesti'):
            if(nextState == 'Rimnicu Vilcea'):
                self.cost += 97
            elif(nextState == 'Craiova'):
                self.cost += 138
            elif(nextState == 'Bucharest'):
                self.cost += 101
        elif (state == 'Mehadia'):
            if(nextState == 'Lugoj'):
                self.cost += 70
            elif(nextState == 'Dobreta'):
                self.cost += 75
        elif (state == 'Bucharest'):
            if(nextState == 'Pitesti'):
                self.cost += 101
            elif(nextState == 'Fagaras'):
                self.cost += 211
            elif(nextState == 'Giurgiu'):
                self.cost += 90
            elif(nextState == 'Urziceni'):
                self.cost += 85
        elif (state == 'Dobreta'):
            if(nextState == 'Mehadia'):
                self.cost += 75
            elif(nextState == 'Craiova'):
                self.cost += 120
        elif (state == 'Craiova'):
            if(nextState == 'Dobreta'):
                self.cost += 120
            elif(nextState == 'Rimnicu Vilcea'):
                self.cost += 146
            elif(nextState == 'Pitesti'):
                self.cost += 138
        elif (state == 'Giurgiu'):
            if(nextState == 'Bucharest'):
                self.cost += 90
        elif (state == 'Urziceni'):
            if(nextState == 'Bucharest'):
                self.cost += 85
            elif(nextState == 'Vaslui'):
                self.cost += 142
            elif(nextState == 'Hirsova'):
                self.cost += 98
        elif (state == 'Hirsova'):
            if(nextState == 'Urziceni'):
                self.cost += 98
            elif(nextState == 'Eforie'):
                self.cost += 86
        elif (state == 'Eforie'):
            if(nextState == 'Hirsova'):
                self.cost += 86
        elif (state == 'Vaslui'):
            if(nextState == 'Urziceni'):
                self.cost += 142
            elif(nextState == 'Iasi'):
                self.cost += 92
        elif (state == 'Iasi'):
            if(nextState == 'Vaslui'):
                self.cost += 92
            elif(nextState == 'Neamt'):
                self.cost += 87
        elif (state == 'Neamt'):
            if(nextState == 'Iasi'):
                self.cost += 87

    def pathCost(self):
        return self.cost



