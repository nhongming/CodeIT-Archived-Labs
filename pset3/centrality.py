from sys import argv
import csv
from collections import deque

'''
shortestPaths

    - This function takes in a user (vertex) and the adjacency list, and returns a dictionary for each shortest path that exists from that vertex to any other in the network. For instance, consider the following network:

    - For instance, for network5.csv, shortestPath("Ann", adjList) should return:
        {
        	"Eve": [ "Kim" ],
        	"Max": [ "Kim" ],
        	"Luke": [ "Kim", "Eve" ]
        }
    - This dictionary should not include keys who the start has a direct edge to (e.g. "Kim") and keys who the start has no path to. 
    - When there are multiple shortest paths, always choose the one that has lower alphabetical order
'''
# Recursive function to print the path of given vertex `u` from source vertex `v`
# def printPath(path, v, u, route):
#     if path[v][u] == v:
#         return
#     printPath(path, v, path[v][u], route)
#     route.append(path[v][u])
 
# # Function to print the shortest cost with path
# # information between all pairs of vertices
# def printSolution(path, n, starting_index):

#     for v in range(n):
#         for u in range(n):
#             if u != v and path[v][u] != -1 and v == starting_index and abs(u-v) > 1:
#                 route = [v]
#                 printPath(path, v, u, route)
#                 route.append(u)
#                 print(f'The shortest path from {v} —> {u} is', route)
 
# # Function to run the Floyd–Warshall algorithm
# def floydWarshall(adjMatrix):
 
#     # base case
#     if not adjMatrix:
#         return
 
#     # total number of vertices in the `adjMatrix`
#     n = len(adjMatrix)
 
#     # cost and path matrix stores shortest path
#     # (shortest cost/shortest route) information
 
#     # initially, cost would be the same as the weight of an edge
#     cost = adjMatrix.copy()
#     path = [[None for x in range(n)] for y in range(n)]
 
#     # initialize cost and path
#     for v in range(n):
#         for u in range(n):
#             if v == u:
#                 path[v][u] = 0
#             elif cost[v][u] != float('inf'):
#                 path[v][u] = v
#             else:
#                 path[v][u] = -1
 
#     # run Floyd–Warshall
#     for k in range(n):
#         for v in range(n):
#             for u in range(n):
#                 # If vertex `k` is on the shortest path from `v` to `u`,
#                 # then update the value of cost[v][u] and path[v][u]
#                 if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
#                         and (cost[v][k] + cost[k][u] < cost[v][u]):
#                     cost[v][u] = cost[v][k] + cost[k][u]
#                     path[v][u] = path[k][u]
 
#             # if diagonal elements become negative, the
#             # graph contains a negative-weight cycle
#             if cost[v][v] < 0:
#                 print('Negative-weight cycle found')
#                 return
 
#     # Print the shortest path between all pairs of vertices

#     return cost, path, n

    ### converting adjList to adjMatrix ###
    # k:[1 if x in v else 0 for x in usersList] for k, v in adjList.items()

    # usersList = list(adjList.keys())
    # I = float('inf')
    # adjMatrix = {}

    # for k, v in adjList.items():
    #     adjMatrixArr = []
    #     for x in usersList:
    #         if x in v:
    #             adjMatrixArr.append(1)
    #         elif x == k:
    #             adjMatrixArr.append(0)
    #         else:
    #             adjMatrixArr.append(I)               
    #     adjMatrix[k] = adjMatrixArr

    # adjMatrix2D = list(adjMatrix.values())
    
    ### using Floyd-Warshall Algorithim to churn out the shortest paths problem ###
    ### Here need to scale down the problem from APSP to SSSP ###

    # cost, path, n = floydWarshall(adjMatrix2D)

    # start_index = usersList.index(start)

    # to print the shortest cost with path
    # information between all pairs of vertices

    # existing_shortest_paths = {}
    # for v in range(n):
    #     for u in range(n):
    #         if u != v and path[v][u] != -1 and v == start_index:
    #             route = [v]
    #             printPath(path, v, u, route)
    #             route.append(u)
    #             print(f'The shortest path from {v} —> {u} is', route)

    # return existing_shortest_paths
# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        # print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in sorted(neighbours): ## From node A to node B, if there are multiple shortest paths, always take the path where the name is less in alphabetical order (sort the neighbour Arr in ascending alphabetical order). ##
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    # print("Shortest path = ", *new_path)
                    return new_path
                    
            explored.append(node)

    # Condition when the nodes
    # are not connected
    # print("So sorry, but a connecting"\
    #             "path doesn't exist :(")
    return

def shortestPaths(start, adjList):
    # TO IMPLEMENT    
    existing_shortest_paths = {}

    for users in adjList:
        traversed_shortest_path = BFS_SP(adjList, start, users)
        if traversed_shortest_path == None:
            continue
        else:
            if len(traversed_shortest_path) > 2:
                bridging_shortest_path = traversed_shortest_path[1:len(traversed_shortest_path)-1]
                existing_shortest_paths[users] = bridging_shortest_path

    return existing_shortest_paths

    # existing_shortest_paths = {}

    # visited = {users:False for users in adjList}

    # pQueue = []
    # pQueue.append(start)
    # visited[start] = True
    # visited_vertices_ordering = [start]
    
    # while ( len(pQueue) != 0 ):
    #     v = pQueue.pop(0)
    #     for dest in adjList[v]:
    #         if not visited[dest]:
    #             visited_vertices_ordering.append(dest)
    #             visited[dest] = True
    #             pQueue.append(dest)
    
    # print(visited_vertices_ordering)   

    # return existing_shortest_paths

    ## modified version BFS tracking the predecessor ##

    # S = []
    # P = {}
    # for v in adjList:
    #     P[v] = []
    # sigma = dict.fromkeys(adjList, 0.0)  # sigma[v]=0 for v in G
    # D = {}
    # sigma[start] = 1.0
    # D[start] = 0
    # Q = deque([start])
    # while Q:  # use BFS to find shortest paths
    #     v = Q.popleft()
    #     S.append(v)
    #     Dv = D[v]
    #     sigmav = sigma[v]
    #     for w in adjList[v]:
    #         if w not in D:
    #             Q.append(w)
    #             D[w] = Dv + 1
    #         if D[w] == Dv + 1:  # this is a shortest path, count paths
    #             sigma[w] += sigmav
    #             P[w].append(v)  # predecessors

    # # return S, P, sigma, D
    # print(S)
    # print(P)
    # print(sigma)
    # print(D)

'''
    from the shortest dist(u, v), check if dist(u, intermediate) 
    + dist(intermediate, v) == dist(u, v)... 
    if so then intermediate should have it's betweenness centrality 
    count increased by 1
'''

'''
betweennessCentrality 

    - This function takes in the adjacency list and returns a dictionary where each vertex is a key and it's betweenness centrality is the value
    - It should make use of the shortestPaths function
    - For instance: betweennessCentrality(adjList) for the above network should return: {'Ann': 0, 'Kim': 3, 'Eve': 2, 'Max': 0, 'Luke': 0}
'''
def betweennessCentrality(adjList):
    # TO IMPLEMENT

    # Initialize the betweeness centrality values to be ZERO 
    # for all users vertices present in the adjacency list

    betweennessCentralityResult = dict((v,0) for v in adjList)

    # iterating through all user vertices to retrieve immediate users for all possible ( starting user && destination user ) pairing
    for startUser in adjList:
        shortestPathsInput = shortestPaths(startUser, adjList)
        for destUser in shortestPathsInput:
            immediateUserArr = shortestPathsInput[destUser]
            if len(immediateUserArr) != 0: # presence of immediate users
                for immediateUser in immediateUserArr:
                    ### from the shortest dist(u, v), check if dist(u, intermediate) 
                    # + dist(intermediate, v) == dist(u, v)... 
                    # if so then intermediate should have it's betweenness centrality count increased by 1 ###
                    if immediateUser in betweennessCentralityResult:
                        betweennessCentralityResult[immediateUser] += 1 # a valid immediate user identified increment the betweeness centrality score

    return betweennessCentralityResult

    # betweennessCentralityOutput = dict((v,0) for v in adjList)

    # for user in adjList:
    #     #SSSP Problem

    #     #Initialization
    #     P = dict((w,[]) for w in adjList)
    #     S = []
    #     g = dict((t,0) for t in adjList); g[user] = 1
    #     d = dict((t,-1) for t in adjList); d[user] = 0
    #     Q = deque([])
    #     Q.append(user)
    #     while Q:
    #         v = Q.popleft()
    #         S.append(v)
    #         for w in adjList[v]:
    #             # path discovery
    #             if d[w] < 0:
    #                 Q.append(w)
    #                 d[w] = d[v] + 1
    #             # path counting
    #             if d[w] == d[v] + 1:
    #                 g[w] = g[w] + g[v]
    #                 P[w].append(v)
    #     #Accumulation back-propogation of dependencies
    #     e = dict((v, 0) for v in adjList)
    #     while S:
    #         w = S.pop()
    #         if w in P:
    #             for v in P[w]:
    #                     e[v] = e[v] + (g[v]/g[w]) * (1 + e[w])
    #         if w != user:
    #             betweennessCentralityOutput[w] = betweennessCentralityOutput[w] + 2 * e[w]
        
    # return betweennessCentralityOutput

    # usersList = list(adjList.keys())
    # I = float('inf')
    # adjMatrix = {}

    # for k, v in adjList.items():
    #     adjMatrixArr = []
    #     for x in usersList:
    #         if x in v:
    #             adjMatrixArr.append(1)
    #         elif x == k:
    #             adjMatrixArr.append(0)
    #         else:
    #             adjMatrixArr.append(I)               
    #     adjMatrix[k] = adjMatrixArr

    # adjMatrix2D = list(adjMatrix.values())


'''
    - In main, we help you to read from the csv file, through a command line argument, and create the adjacency list for the edges. This is stored in a dictionary where each key is a vertex in the network and value is a list of edges for that vertex. 
    - To test, for instance, network5.csv, you may run `python centrality.py network5.csv`
'''
def main():

    if len(argv) < 2:
        print("Require network file to load edges")
        return

    adjList = {}
    with open("networks/" + argv[1], "r") as csv_file:
        myReader = csv.reader(csv_file)
        for row in myReader:
            u, v = row[0], row[1]
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []
            adjList[u].append(v)

    # print(shortestPaths("Ann", adjList)) ## Test Case 1
    # print(shortestPaths("Draco", adjList)) ## Test Case 3
    # print(shortestPaths("Shawn", adjList)) ## Test Case 5
    # print(shortestPaths("Jake", adjList)) ## Test Case 7
    # print(adjList)
    print(shortestPaths("Noah", adjList)) ## Test Case 9
    print(betweennessCentrality(adjList)) 

if __name__ == "__main__":
    main()
