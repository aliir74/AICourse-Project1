import eaters, puzzel8, routing, Searches

problem1 = routing.RomanianRouting('Arad', 'Vaslui')
problem2 = puzzel8.Puzzel([[4, 5, 2], [1, 7, 3], [0, 6, 8]])
state = [[1, 2, 3],[4, 5, 6], [0,7,8]]
problem2veryeasy = puzzel8.Puzzel(state)
problem3 = eaters.manEater(['right',[[3,3],[0,0]]])


#print(Searches.BFSTree(problem1)) ok
#print(Searches.DLSTree(problem1, 8)) ok
#print(Searches.Astar(problem1)) ok

print(22222)

#print(Searches.DFSGraph(problem2easy)) ok
#print(Searches.BidrectionalTree(problem2veryeasy)) ok
#print(Searches.Astar(problem2veryeasy)) ok

print(333333)

#print(Searches.BFSTree(problem3))
#print(Searches.IDS(problem3))
