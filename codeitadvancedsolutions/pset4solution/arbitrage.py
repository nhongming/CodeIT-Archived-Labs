from time import time
from exchangeRates import exchangeRates
from sys import argv
import math

INF = 10000.0


def arbitrage(exchangeRates):

    # CONVERT EXCHANGE RATES TO LOG GRAPH
    logGraph = convertToLogGraph(exchangeRates)

    # RETRIEVES SHORTEST PATH TREE / NONE THROUGH BELLMAN FORD ALGO
    shortestPathTree = bellmanFord(logGraph)

    # RETRIEVES EDGES INVOLVED IN CYCLE IF THERE IS ONE
    return searchForCycle(shortestPathTree)


def convertToLogGraph(exchangeRates):
    negLogExchangeRates = {}
    for k in exchangeRates:
        negLogExchangeRates[k] = []
        for rate in exchangeRates[k]:
            newEdge = (rate[0], rate[1],  -math.log10(rate[2]))
            negLogExchangeRates[k].append(newEdge)

    return negLogExchangeRates


def bellmanFord(logGraph):

    distTo = {}
    edgeTo = {}
    count = 0
    for k in logGraph:
        edgeTo[k] = None
        if count == 0:
            distTo[k] = 0
            count += 1
        else:
            distTo[k] = INF

    for k in logGraph:
        for k in logGraph:
            for edge in logGraph[k]:
                src, dest, weight = edge
                if distTo[src] + weight < distTo[dest]:
                    distTo[dest] = distTo[src] + weight
                    edgeTo[dest] = (src, dest, weight)

    spt = {}

    for k in edgeTo:
        if edgeTo[k] is None:
            continue
        src, dest, weight = edgeTo[k]
        if src not in spt:
            spt[src] = []
        if dest not in spt:
            spt[dest] = []
        spt[src].append(edgeTo[k])

    return spt


def searchForCycle(shortestPathTree):

    edgeTo = {}
    onStack = {}
    visited = {}

    for k in shortestPathTree:
        visited[k] = False
        onStack[k] = False

    for k in shortestPathTree:
        if not visited[k]:
            res = dfsForCycle(shortestPathTree, k, edgeTo, onStack, visited)
            if res is not None:
                return res
    return []


def dfsForCycle(shortestPathTree, v, edgeTo, onStack, visited):
    visited[v] = True
    onStack[v] = True

    for edge in shortestPathTree[v]:
        src, dest, weight = edge
        if not visited[dest]:
            edgeTo[dest] = edge
            res = dfsForCycle(shortestPathTree, dest, edgeTo, onStack, visited)
            if res is not None:
                return res

        elif onStack[dest]:
            cycle = []
            f = edge
            while (f[0] != dest):
                cycle.insert(0, (f[0], f[1]))
                f = edgeTo[f[0]]

            cycle.insert(0, (f[0], f[1]))
            return cycle


def main():
    try:
        n = int(argv[1]) - 1
    except:
        print("No CLA inputted, defaulting to exchangeRate 1")
        n = 0

    start = time()
    print(arbitrage(exchangeRates[n]))
    end = time()
    print(end - start)


if __name__ == "__main__":
    main()
