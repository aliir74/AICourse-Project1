class RomanianRouting:
    def __init__(self, source, destination):
        self.initialState = source
        self.destination = destination

    def getInitialState(self):
        return self.initialState


    def Actions(self, currentNode):
        ans = []
        if(currentNode == 'Ordaea'):
            ans = ['Zerind', 'Sibiu']
        elif(currentNode == 'Zerind'):
            ans = ['Oradea', 'Arad']
        elif(currentNode == 'Arad'):
            ans = ['Zerind', 'Sibiu', 'Timisoara']
        elif(currentNode == 'Sibiu'):
            ans = ['Oradea', 'Arad', 'Rimnicu Vilcea', 'Fagaras']
        elif(currentNode == 'Fagaras'):
            ans = ['Sibiu', 'Bucharest']
        elif(currentNode == 'Rimnicu Vilcea'):
            ans = ['Sibiu', 'Pitesti', 'Craiova']
        elif(currentNode == 'Timisoara'):
            ans = ['Arad', 'Lugoj']
        elif(currentNode == 'Lugoj'):
            ans = ['Timisoara', 'Mehadia']
        elif(currentNode == 'Pitesti'):
            ans = ['Rimnicu Vilcea', 'Craiova', 'Bucharest']
        elif(currentNode == 'Mehadia'):
            ans = ['Lugoj', 'Dobreta']
        elif(currentNode == 'Bucharest'):
            ans = ['Pitesti', 'Fagaras', 'Giurgiu', 'Urziceni']
        elif(currentNode == 'Dobreta'):
            ans = ['Mehadia', 'Craiova']
        elif(currentNode == 'Craiova'):
            ans = ['Dobreta', 'Rimnicu Vilcea', 'Pitesti']
        elif(currentNode == 'Giurgiu'):
            ans = ['Bucharest']
        elif(currentNode == 'Urziceni'):
            ans = ['Bucharest', 'Vaslui', 'Hirsova']
        elif(currentNode == 'Hirsova'):
            ans = ['Urziceni', 'Eforie']
        elif(currentNode == 'Eforie'):
            ans = ['Hirsova']
        elif(currentNode == 'Vaslui'):
            ans = ['Urziceni', 'Iasi']
        elif(currentNode == 'Iasi'):
            ans = ['Vaslui', 'Neamt']
        elif(currentNode == 'Neamt'):
            ans = ['Iasi']
        return ans

    def GoalTest(self, currentNode):
        if(currentNode == self.destination):
            return True
        return False

