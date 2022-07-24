from time import time
from exchangeRates import exchangeRates
from sys import argv
import math

INF = 10000.0   # Initialize the infinity

def arbitrage(exchangeRates):   # arbitrage function (main function)    

    # CONVERT EXCHANGE RATES TO LOG GRAPH
    logGraph = convertToLogGraph(exchangeRates) # convert exchange rates to log graph

    # RETRIEVES SHORTEST PATH TREE / NONE THROUGH BELLMAN FORD ALGO
    shortestPathTree = bellmanFord(logGraph)    # retrieve shortest path tree

    # RETRIEVES EDGES INVOLVED IN CYCLE IF THERE IS ONE
    return searchForCycle(shortestPathTree)  # retrieve edges involved in cycle

'''
convertToLogGraph:
    - This function takes in a graph of exchange rates, and returns an adjacency list with the same edges, but with every weight having the negative log10 function applied
'''
def convertToLogGraph(exchangeRates):
    logGraph = {}   # Initialize the log graph
    for i in exchangeRates: # for each exchange rate
        logGraph[i] = []    # Initialize the adjacency list 
        for edge in range(len(exchangeRates[i])):   # for each edge in the exchange rate
            src_vertex, dest_vertex, exchangeRate = exchangeRates[i][edge][0],  exchangeRates[i][edge][1], exchangeRates[i][edge][2]    # src_vertex, dest_vertex, exchangeRate
            normalizedExchangeRate = -math.log10(exchangeRate)  # convert to log graph
            logGraph[i].append((src_vertex, dest_vertex, normalizedExchangeRate))   # add edge to log graph
    return logGraph # return the log graph

def bellmanFordHelper(logGraph, source):
    distance, predecessor   = {}, {}     # Initialize the distance tree and predecessor tree
    for vertex in logGraph: # Initialize the distance tree
        distance[vertex] = INF  # Initialize the distance tree
        predecessor[vertex] = None  # Initialize the predecessor tree
    distance[source] = 0    # Initialize the distance tree
    for i in range(len(logGraph)): # relax the edges for each vertex in the graph for each iteration of the Bellman-Ford algorithm (n-1 times)
        for vertex in logGraph: # for each vertex in the graph
            for neighbour in logGraph[vertex]: # for each neighbour of the vertex
                dest_vertex = neighbour[1]  # dest_vertex is the neighbour of the vertex
                relax(vertex, dest_vertex, logGraph, distance, predecessor) # relax the edge
    # Check for negative cycles (if there is one, there is a cycle)
    for vertex in logGraph: # for each vertex in the graph
        for neighbour in logGraph[vertex]:  # for each neighbour of the vertex
            dest_vertex = neighbour[1]  # dest_vertex is the neighbour of the vertex
            edgeWeight = neighbour[2]  # edgeWeight is the weight of the edge
            if distance[vertex] + edgeWeight < distance[dest_vertex]:   # if the distance of the vertex is less than the distance of the neighbour
                return retrace_negative_loop(predecessor, vertex)   # return the negative loop
    return None # if there is no negative cycle, return None

def relax(vertex, dest_vertex, logGraph, distance, predecessor): 
    matchedAdjList = logGraph[vertex]   # matchedAdjList is the adjacency list of the vertex
    for edge in matchedAdjList: # for each edge in the matchedAdjList
        if edge[1] == dest_vertex:  # if the edge is to the dest_vertex
            edgeWeight = edge[2]    # edgeWeight is the weight of the edge
            if distance[vertex] + edgeWeight < distance[dest_vertex]:   # if the distance of the vertex is less than the distance of the neighbour
                distance[dest_vertex] = distance[vertex] + edgeWeight   # update the distance of the neighbour
                predecessor[dest_vertex] = vertex   # update the predecessor of the neighbour

def retrace_negative_loop(p, start):    
	arbitrageLoop = [start] # Initialize the arbitrage loop
	next_node = start   # Initialize the next node
	while True: # while there is a next node
		next_node = p[next_node]    # update the next node
		if next_node not in arbitrageLoop:  # if the next node is not in the arbitrage loop
			arbitrageLoop.append(next_node) # add the next node to the arbitrage loop
		else:   # if the next node is in the arbitrage loop
			arbitrageLoop.append(next_node) # add the next node to the arbitrage loop
			arbitrageLoop = arbitrageLoop[arbitrageLoop.index(next_node):]  # truncate the arbitrage loop to the index of the next node
			return arbitrageLoop[::-1]  # return the arbitrage loop   
            
'''
bellmanFord:
    - This function will take in the logGraph (output of convertToLogGraph function), and returns the shortest path tree    
    - The shortest path tree is essentially an adjacent list made up of the edges involved in the edgeTo list.
'''
def bellmanFord(logGraph):  # Bellman-Ford algorithm    
    shortestPathTree = {vertex:[] for vertex in logGraph} # Initialize the shortest path tree
    source = list(logGraph.keys())[0] # source is the arbitrary first vertex in the log graph
    path = bellmanFordHelper(logGraph, source)  # find the shortest path tree
    if path is not None:    # if there is a negative cycle
        for v in range(len(path)-1):    # for each vertex in the path
            start, target = path[v], path[v+1]  # start, target are the vertices in the path
            for edge in logGraph[start]:    # for each edge in the start vertex
                if edge[0] == start and edge[1] == target:  # if the edge is from the start vertex to the target vertex
                    if edge not in shortestPathTree[start]: # if the edge is not in the shortest path tree
                        shortestPathTree[start].append(edge)    # add the edge to the shortest path tree
    return shortestPathTree # return the shortest path tree

'''
searchForCycle:
    - This function takes in the shortest path tree (output of bellmanFord), and returns a list containing edges (excluding the weights) involved in the negative cycle.
    - For instance, for exchange rates 1, it should return: [('SGD', 'GBP'), ('GBP', 'USD'), ('USD', 'SGD')]

'''
def searchForCycle(shortestPathTree):   # search for negative cycles
    arbitrageLoop = []  # Initialize the arbitrage loop
    for vertex in shortestPathTree: # for each vertex in the shortest path tree
        for edge in shortestPathTree[vertex]:   # for each edge in the shortest path tree
            arbitrageLoop.append((vertex, edge[1])) # add the edge to the arbitrage loop
    return arbitrageLoop    # return the arbitrage loop

def main(): # main function
    try:    # try to open the file
        n = int(argv[1]) - 1    # n is the number of exchange rates
    except: # if the file cannot be opened
        print("No CLA inputted, defaulting to exchangeRate 1")  
        n = 0   # n is the number of exchange rates

    start = time()  # start the timer
    print("Arbitrage: {}".format(arbitrage(exchangeRates[n])))  # print the arbitrage
    end = time()    # end the timer
    print("Time taken for arbitrage function: {}s".format(end - start)) # print the time taken for the arbitrage function


if __name__ == "__main__":  # main function
    main()  